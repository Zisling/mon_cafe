import os
import subprocess
import shlex
import sys
verbose = len(sys.argv) > 1 and sys.argv[1] == '-v'
if(verbose):
    import difflib
cwd = os.getcwd()

def runTest(folderName):
    # example: run the line: python3 initiate.py "test 3"/config.txt in a new terminal
    config = subprocess.Popen(shlex.split('python3 initiate.py "'+folderName+'"/config.txt'), cwd=cwd)
    config.communicate() # waits for the command to finish running
    # example: run the line: python3 action.py "test 3"/action.txt in a new terminal
    actions = subprocess.Popen(shlex.split('python3 action.py "'+folderName+'"/action.txt'), stdout=subprocess.PIPE, cwd=cwd)
    # gets the output of the command and turns it from bytes to string
    out = actions.communicate()[0].decode('utf-8')
    # checks the relevant expected output from the folder's expectedOut.txt file
    expectedOut = open(folderName+'/expectedOut.txt').read()
    if(out != expectedOut):
        # printn a wrong answer message if needed
        print("Test "+folderName[5:]+" returned unexpected output")
        # if the user added the tag -v in the call to this it will print
        # the difference between the output and the expected output
        if(verbose):
            print("Output was: "+out)
            print("----------\nDifference is: ")
            for i,s in enumerate(difflib.ndiff(expectedOut, out)):
                if s[0]==' ': continue
                elif s[0]=='-':
                    print(u'Output missing "{}" from position {}'.format(s[-1],i))
                elif s[0]=='+':
                    print(u'Output added "{}" in position {}'.format(s[-1],i))    
    else:
        print("Test "+folderName[5:]+" Passed!")


for folder in os.listdir(cwd):
    if(folder[0:5] == "test "):
        runTest(folder)