import re


pattern = re.compile(r'''
             #Don't match begining of string number can start from anywhere
   (\d{3})   #area code is 3 digit
   \D*       #Optional seprator is any number or any digit
   (\d{3})   #Trunk is 3 digit
   \D*       #Optional character
   (\d{4})   #rest no
   \D*       #seprator
   (\d*)     # optional
   $         #end of string
    ''', re.VERBOSE)

print pattern.search('emergency 1-(415) 867.5309 #9999').groups()


import re
import os

def string_replace(fname):

   pattern1 = '<title>\D*\d*\D*\d*2013\D*\d*</title>'
   pattern2 = '2013\D*\d*<g:plusone>'

   fname_new = 'temp'
   f = open(fname, 'r')
   fnew = open(fname_new, 'w')

   for string in f:
      if(re.search(pattern1, string) or re.search(pattern2, string)):
         newline = re.sub('2013', '2014', string)
         fnew.write(newline)
	 print fname, ':' , newline
      else:
         fnew.write(string)

   f.close()
   fnew.close()
   os.remove(fname)
   os.rename(fname_new, fname)


def listFiles(dir):
    basedir = dir
    print 'current basedir=', basedir
    print "Files in ", os.path.abspath(dir), ": "
    subdirlist = []
    for item in os.listdir(dir):
	#print 'checking if item is a file or a dir', item
	fullpath = os.path.join(basedir,item)
        if os.path.isdir(fullpath):
            print  'dir item=',fullpath
	    subdirlist.append(fullpath)
        else:
	    print 'file item=',fullpath
	    if(item.endswith('dummy') or item.endswith('.html')):
	       # print 'file to be processed ********', item
	       print 'file to be processed = ', fullpath
	       string_replace(fullpath)


    print '------ new dir ----'
    print 'subdirlist =', subdirlist
    for subdir in subdirlist:
        listFiles(subdir)

# call this to repalce "2013" with "2014" in *.php or *.html
listFiles('.')

