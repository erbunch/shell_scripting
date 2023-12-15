#!/usr/bin/env python

import sys


def mk_files(file):
    data = file.read()
    genes = data.split('>')
    for gene in genes:
        seq = gene.split()
        seqoutput = open(seqoutput.txt, 'w')
        print(seq, file=seqoutput)
        new_file = open(seq[0] + '.fasta', 'w')
        new_file.write(seq[0] + seq[1] + seq[2] + '\n' +  seq[3])
        new_file.close()
    return

def count_seqs(file):
    count_seqs = 0
    count_base = 0
    data = file.read()
    genes = file1.split('<')
    for gene in genes:
        count += 1
        seq = gene.split('\n')
        count_base += len(seq[1])
    print("There are " + count_seqs + "genes in the file " + file + "and " + count_base + "bases", file=log.txt)
    return

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as ex1:
        with open(sys.argv[2], 'r') as ex2:
            mk_files(ex1)
            mk_files(ex2)
            count_seqs(ex1)
            count_seqs(ex2)


