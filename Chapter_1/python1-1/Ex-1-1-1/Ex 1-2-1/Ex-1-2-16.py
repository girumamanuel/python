
#Compose a program that takes two integers a and b from the command line and writes a random integer between a and b.

import stdio
import sys
import random

a = int(sys.argv[1])
b = int(sys.argv[2])

stdio.writeln(random.randrange(a,b+1))