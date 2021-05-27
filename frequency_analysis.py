# read from file 
# sample : python3 frequency_analysis.py [filename.txt]
import sys,os

letter_count={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0,}
alphabet = "abcdefghijklmnopqrstuv"
filename = sys.argv[1]

with open(filename,'r') as f:
    for i in f.read().lower():
        if i in alphabet:
            letter_count[i] += 1

print("++++++++++++++++++++++")
print("    times")

for i in letter_count:
    print(i," : ",letter_count[i])

# ToDo : sort by dictionary value not abcdefg..
