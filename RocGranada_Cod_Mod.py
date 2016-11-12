# -*- coding: utf-8 -*-

# Author: Roc Granada Verdú
# RocGranada_Cod_Mod.py
import random
import matplotlib.pyplot as plt

"""
Given a sequence of bits and a choosen codification/modulation model
apply it to the previous sequence and return the result.
"""
SEQUENCE = "01001110101"

#Prints for the menu
header = "\n*** Welcome, choose the option you prefere ***"
options = """\t1. Nonreturn to Zero (NRZ)
\t2. Nonreturn to Zero-Level (NRZ-L)
\t3. Nonreturn to Zero Inverted (NRZI)
\t4. Bipolar - AMI
\t5. Pseudoternary
\t6. Manchester
\t7. Differential Manchester
\t8. B8ZS
\t9. HDB3
"""
input_sequence = "Enter your sequence: (blank for random one)"

class Model:
    """Class that englovates the information necessary for the codification/modulation"""
    def __init__(self):
        self.option = 1
        self.sequence = [0,1,0,1]

    def __str__(self):
        #seq = [int(elem) for elem in self.sequence]
        plt.plot(self.sequence)
        plt.axis([0,len(self.sequence),min(self.sequence)-1,2])
        plt.xlabel("Bits")
        plt.ylabel("Levels")
        plt.show()
        return ""

    # Getters & Setters
    def setOption(self,option):
        self.option = option
    def getOption(self):
        return self.option
    def setSequence(self,sequence):
        self.sequence = sequence
    def getSequence(self):
        return self.sequence

def askData(model):
    """Method to get all the data needed from the user"""
    print header
    print options
    opt_in = input()
    model.setOption(opt_in)
    print input_sequence
    seq_in = raw_input()
    if seq_in != "":
        model.setSequence(seq_in)
    else:
        SEQUENCE = ""
        for i in range(50): SEQUENCE += str(random.randint(0,1))
        model.setSequence(SEQUENCE)

#1:NRZ-L,2:NRZI,3:AMI,4:Pseudoternary,5:Manchester,6:Diff_manchester,7:B8ZS,8:HDB3

def NRZ(model):
    """Nothing to do to the sequence"""
    model.setSequence([int(elem) for elem in model.getSequence()])
    pass

def NRZ_L(model):
    """Invert 1's and 0's levels"""
    dic = {'1':0,'0':1}
    model.setSequence([dic[elem] for elem in model.getSequence()])

def NRZI(model):
    """Change level when 1 found"""
    dic = {1:0,0:1}
    seq = [0]
    for elem in model.getSequence():
        if elem == '1':
            seq.append(dic[seq[-1]])
        else:
            seq.append(seq[-1])
    seq.remove(seq[0])
    model.setSequence(seq)

def AMI(seq):
    """0 always on 0, 1 changes from 1 to -1"""
    last = -1
    seq = []
    for elem in model.getSequence():
        if elem == '1':
            last = last*(-1)
            seq.append(last)
        else:
            seq.append(0)
    model.setSequence(seq)

def Pseudoternary(seq):
    """1 always on 0, 0 changes from 1 to -1"""
    last = -1
    seq = []
    for elem in model.getSequence():
        if elem == '0':
            last = last*(-1)
            seq.append(last)
        else:
            seq.append(0)
    model.setSequence(seq)

def Manchester(seq):
    return seq

def Diff_manchester(seq):
    return seq

def B8ZS(seq):
    return seq

def HDB3(seq):
    return seq

#Dictionary that has all the models names and an id associated
models = {1:NRZ,2:NRZ_L,3:NRZI,4:AMI,5:Pseudoternary,6:Manchester,7:Diff_manchester,8:B8ZS,9:HDB3}

def main(model):
    """Method that codifies/modulates the sequence in the given option"""
    func = models[model.getOption()]
    func(model)
    seq = ""
    for elem in model.getSequence(): seq += str(elem)
    return seq

model = Model()
askData(model)
print "Choosen model: ", model.option
print "Sequence at begining: ", model.sequence
print "Sequence result: ", main(model)
print model
