import sys,os

filenames = []

wordlines = []
for filename in os.listdir("."):
	# print filename[-3:]
	if filename[-3:]=="txt":
		f = open(str(filename))
		lines = f.read().splitlines()
		f.close()


		for i in xrange(len(lines)):
			st = ""
			if lines[i].isalpha():
				st+=str(lines[i])
				st+=" -- "
				i+=1
				while i< len(lines) and lines[i]!="":
					st+=str(lines[i])
					st+=";"
					i+=1
			if len(st):
				st+="\n"
				wordlines.append(st)

f = open("gre","w")
for wordline in wordlines:
    f.write(wordline)
f.close()
