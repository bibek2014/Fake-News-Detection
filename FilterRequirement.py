import sys
fp=open(sys.argv[1],"r")
fp1=open(sys.argv[2],"w")
for l in fp:
	if "@" in l: continue
	fp1.write(l.strip()+"\n")
fp.close()
fp1.close()