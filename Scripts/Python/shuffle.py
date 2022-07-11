#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#This will need a pickled dict or a dict in one format or another. The dict's key-value pair should have 
#the onekp alphabetical code as the keys and the respective names of the species as the value pairs.

#The script should be supplied with some params in the form of sysargv.

#The following sysargs should be supplied for the script to work:

#1. -dict - This is the pickled dict or the path to the pickled dict that has the onekp alphabetical code as the keys and the species names as the values.
#2. -loc_one - This is the path to the directory that has the first .faa.tar.bz2 files
#3. -loc_two - This is the location where the name changed files will be shifted to


# In[1]:


# these are the libraries that we will need to finish the job
import pickle # this is what we will use to pickle the final output 
import os # this is what we will use to parse the os tree
import shutil # this is what move the files
import argparse # this is what we will use to get the right params for the task


# In[5]:


parser = argparse.ArgumentParser(description="This script does not create directories if they do not exist, please only supply directories that already exist. This will need a pickled dict or a dict in one format or another. The dict's key-value pair should have the onekp alphabetical code as the keys and the respective names of the species as the value pairs.The script should be supplied with some params in the form of sysargv. Since the list only contains the species we are interested in we do not need to bother with copying over everyfile, rather only the ones we are interested in.")


# In[ ]:


parser.add_argument('--pickle', nargs='?', const="bar", default=False, help="Please, when you supply paths make note of exteaneous slashes.This is the path to the pickle that holds the connection between the coded names and real species names")
parser.add_argument('--loc_one', nargs='?', const="bar", default=False, help ="Please, when you supply paths make note of exteaneous slashes.This is the location where the faa.tar.bz2 files have been downloaded.")
parser.add_argument('--loc_two', nargs='?', const="bar", default=False, help="Please, when you supply paths make note of exteaneous slashes.This is where the new files will go after being renamed.")
args = parser.parse_args()


# In[ ]:


with open(args.pickle, 'rb') as handle: # this assumes that your dict has been python pickled and is available for use
    dict_one = pickle.load(handle)


# In[ ]:


os.chdir(args.loc_one) # this makes parsing thorugh the file tree easier


# In[ ]:


filename_list = []
for filename in os.listdir(args.loc_one):
    filename_list.append((filename.split('.')[0]))


# In[ ]:


n=0
os.chdir(args.loc_one)
for key in dict_one:
    if key in filename_list:
        origin = f'{args.loc_one}/{key}.faa.tar.bz2'
        destination = f'{args.loc_two}/{dict_one[key]}.faa.tar.bz2'
        if os.path.isfile(destination):
            n += 1
            destination = f'{args.loc_two}/{dict_one[key]}_{n}.faa.tar.bz2'
            shutil.move(origin, destination)
        else:
            shutil.move(origin, destination)


# In[ ]:


#What the above code achieves is that it takes only the species that are in the current dict that you supplied.

