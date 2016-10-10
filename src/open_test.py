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


training_input=list()
for fname in training_list:
	img=Image.open(fname)
	if "up" in fname:
		training_input.append((list(img.getdata()),list([[1],[0],[0],[0]])))
	elif "straight" in fname:
		training_input.append((list(img.getdata()),list([0],[1],[0],[0])))
	elif "left" in fname:
		training_input.append((list(img.getdata()),list([[0],[0],[1],[0]])))
	elif "right" in fname:
		training_input.append((list(img.getdata()),list([[0],[0],[0],[1]])))
	else:
		print "Something wrong with a file name"

test_input=list()
for fname in test_list:
	img=Image.open(fname)
	if "up" in fname:
		test_input.append((list(img.getdata()),array([[1],[0],[0],[0]])))
	elif "straight" in fname:
		test_input.append((list(img.getdata()),list([[0],[1],[0],[0]])))
	elif "left" in fname:
		test_input.append((list(img.getdata()),list([[0],[0],[1],[0]])))
	elif "right" in fname:
		test_input.append((list(img.getdata()),list([[0],[0],[0],[1]])))
	else:
		print "Something wrong with a file name"


for i in test_input:
	print i
#neural_net=network.Network([960,30,4])
#neural_net.SGD(training_input,10,100,5,test_input)
