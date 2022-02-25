#importing all the libraies
import pandas as pd
from Bio import SeqIO
import os, sys

# read your postion file which has postion information about genes and which MSA to append it
postion=pd.read_csv("text.csv")

#loop over the list of MSA files
for clst in os.listdir(r"/home/arnav/practice/msa"):
    # Loop over the genes that you have to append
    for gene2 in SeqIO.parse("/home/arnav/practice/protein.fasta","fasta"):
        #comapre the 
        for index, row in postion.iterrows():
            if row['file'] == clst and row['Gene'] == gene2.id:
                f=open(r"/home/arnav/practice/msa/{}".format(row['file']),"a")
                f.write("\n"+">"+gene2.id+"\n")
                f.write(str(gene2.seq))
                f.close()
            else:
                continue
        continue

