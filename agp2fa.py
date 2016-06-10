#!/usr/bin/python
from __future__ import print_function
from Bio import SeqIO
import sys

def concatenate(line):
    ctype=line[4]
    entry=line[5]
    global last
    if ctype!="U":
        start=int(line[6])
        end=int(line[7])
        sequence=records[entry].seq[start-1:end]
    else:
        totns=int(line[2])-int(line[1])
        sequence="N"*totns
    while len(sequence)>0:
        print(sequence[:60-last],end="",file=z)
        lunghezza=len(sequence[:60-last])
        if len(sequence[:60-last])+last!=60:
            last=len(sequence[:60-last])+last
        else:
            last=0
            print("",sep="",end="\n",file=z)
        if len(sequence)>60:
            sequence=sequence[lunghezza:]
        else:
            sequence=""

records=SeqIO.index(sys.argv[1],"fasta")
z=open(sys.argv[2][:-3]+"fasta","w")

lastid=""
with open(sys.argv[2],"rU") as a:
    for line in a:
        line=line.strip().split()
        seqid=line[0]
        if seqid!=lastid:
            if lastid=="":
                print(">",seqid,sep="",file=z)
            else:
                print("\n>",seqid,sep="",file=z)
            last=0
        concatenate(line)
        lastid=seqid
