from PIL import Image
from random import shuffle
import os
import numpy as np
import network


filelist=[]
for root, dirs, files in os.walk('..\data\\faces_4'):
	for fname in files:
		if fname.endswith(".pgm"):
			filelist.append(os.path.join(root,fname))

shuffle(filelist)
len_training=int((len(filelist)*0.8))
training_list=filelist[:len_training]
test_list=filelist[len_training:]

def y_vector(position):
	y=np.zeros((4,1))
	y[position]=1.0
	return y

training_input=[]
for fname in training_list:
	img=Image.open(fname)
	if "up" in fname:
		imgdata=np.asarray(list(img.getdata()))
		training_input.append((np.reshape(imgdata,(960,1)),y_vector(0)))
	elif "straight" in fname:
		imgdata=np.asarray(list(img.getdata()))
		training_input.append((np.reshape(imgdata,(960,1)),y_vector(1)))
	elif "left" in fname:
		imgdata=np.asarray(list(img.getdata()))
		training_input.append((np.reshape(imgdata,(960,1)),y_vector(2)))
	elif "right" in fname:
		imgdata=np.asarray(list(img.getdata()))
		training_input.append((np.reshape(imgdata,(960,1)),y_vector(3)))
	else:
		print "Something wrong with a file name"

test_input=[]
for fname in test_list:
	img=Image.open(fname)
	if "up" in fname:
		imgdata=np.asarray(list(img.getdata()))
		test_input.append((np.reshape(imgdata,(960,1)),0))
	elif "straight" in fname:
		imgdata=np.asarray(list(img.getdata()))
		test_input.append((np.reshape(imgdata,(960,1)),1))
	elif "left" in fname:
		imgdata=np.asarray(list(img.getdata()))
		test_input.append((np.reshape(imgdata,(960,1)),2))
	elif "right" in fname:
		imgdata=np.asarray(list(img.getdata()))
		test_input.append((np.reshape(imgdata,(960,1)),3))
	else:
		print "Something wrong with a file name"


neural_net=network.Network([960,30,4])
neural_net.SGD(training_input,30,10,0.1,test_input)