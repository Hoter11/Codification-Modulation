# -*- coding: utf-8 -*-

# Author: Roc Granada Verdú
# RocGranada_Cod_Mod.py

"""
Given a sequence of bits and a choosen codification/modulation model
apply it to the previous sequence and return the result.
"""
SEQUENCE = 01001110101

#Dictionary that has all the models names and an id associated
models = {}
#Prints for the menu
header = "\n*** Welcome, choose the option you prefere ***"
options = """\t1. Nonreturn to Zero-Level (NRZ-L)
\t2. Nonreturn to Zero Inverted (NRZI)
\t3. Bipolar - AMI
"""
input_sequence = "Enter your sequence: (blank for predefined one)"

class Model:
    """Class that englovates the information necessary for the codification/modulation"""
    def __init__(self):
        self.option = 1
        self.sequence = 1
        #Normal comment

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
        model.setSequence(seq_in)
    except SyntaxError:
        model.setSequence(SEQUENCE)

def main(model):
    """Method that codifies/modulates the sequence in the given option"""
    return 0

model = Model()
askData(model)
print "Choosen model: ", model.option
print "Sequence at begining: ", model.sequence
print "Sequence result: ", main(model.sequence)
