from os import listdir
from os.path import isfile, join

mypath = 'cities/'

files = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
