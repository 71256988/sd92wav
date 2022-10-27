#Usage: sd92wav.py file.sd9
import sys

content = []
inputfile = str(sys.argv[1])

f = open(inputfile, 'rb')
f.seek(32)
content+=f.read()
f.close()

outputfile = open((inputfile[:-3] + "wav"),'wb')
outputfile.write(bytes(content))
outputfile.close()
