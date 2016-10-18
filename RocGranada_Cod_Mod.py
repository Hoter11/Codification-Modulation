# -*- coding: utf-8 -*-

# Author: Roc Granada Verdú
# RocGranada_Cod_Mod.py

"""
Given a sequence of bits and a choosen codification/modulation model
apply it to the previous sequence and return the result.
"""
SEQUENCE = 0x01001110101

#Prints for the menu
header = "\n*** Welcome, choose the option you prefere ***"
options = """\t1. Nonreturn to Zero-Level (NRZ-L)
\t2. Nonreturn to Zero Inverted (NRZI)
\t3. Bipolar - AMI
\t4. Pseudoternary
\t5. Manchester
\t6. Differential Manchester
\t7. B8ZS
\t8. HDB3
"""
input_sequence = "Enter your sequence: (blank for predefined one)"

class Model:
    """Class that englovates the information necessary for the codification/modulation"""
    def __init__(self):
        self.option = 1
        self.sequence = 1

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
    try:
        seq_in = input()
        model.setSequence(int(seq_in,2))
    except SyntaxError:
        model.setSequence(SEQUENCE)

#1:NRZ-L,2:NRZI,3:AMI,4:Pseudoternary,5:Manchester,6:Diff_manchester,7:B8ZS,8:HDB3
def NRZ_L(seq):
    return seq

def NRZI(seq):
    return seq

def AMI(seq):
    return seq

def Pseudoternary(seq):
    return seq

def Manchester(seq):
    return seq

def Diff_manchester(seq):
    return seq

def B8ZS(seq):
    return seq

def HDB3(seq):
    return seq

#Dictionary that has all the models names and an id associated
models = {1:NRZ_L,2:NRZI,3:AMI,4:Pseudoternary,5:Manchester,6:Diff_manchester,7:B8ZS,8:HDB3}

def main(model):
    """Method that codifies/modulates the sequence in the given option"""
    func = models[model.getOption()]
    return func(model.getSequence())

model = Model()
askData(model)
print "Choosen model: ", model.option
print "Sequence at begining: ", model.sequence
print "Sequence result: ", main(model)
