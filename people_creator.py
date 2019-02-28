# import os
# Importing Libraries
import names
from urllib.request import urlretrieve as ur
import numpy as np 

#Source to get the images
urlSource = "https://thispersondoesnotexist.com/image"


#Getting total number of humans
numbers = input("Let's make humans. How many of em'? :")

#Making array of numbers and images
images_array = np.arange(int(numbers))
images_names = []

#Generating images with the specific names generated from names library
for x in images_array:
	images_names.append(names.get_full_name())
	ur(urlSource,images_names[x]+".jpeg")
	# os.system('curl --output {}.jpeg {}'.format(images_names[x],urlSource))
	print("Human {} created. Name: {}".format(x+1,images_names[x]))
