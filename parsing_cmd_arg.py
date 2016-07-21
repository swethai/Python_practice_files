#!/usr/bin/python

#Arguments parsing
#passing input and out files as arguments
#test.py -i <inputfile> -0 <outputfile>

#importing the sys and parser method
import sys, getopt

#defining main, with passing args
def main(argv):

#declaring the variables
    inputfile = ''
    outputfile = ''

#Exception handling
#parsing arguments using getopt method
#getopt method returns two elemnts, first is list of (option,value) pair, 
#second is program arguments let after the option list was stripped
    try:
        opts, args1 = getopt.getopt(argv, "h:i:o:", ["ifile=", "ofile="])
#        print ("opts", opts);
#        print ("args", str(args1));
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)

#looping for the input and output files
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

#pring the input and output files
    print 'input file is "', inputfile
    print 'output file is "', outputfile

#main function delaration
if __name__ == "__main__":
   main(sys.argv[1:]) 
