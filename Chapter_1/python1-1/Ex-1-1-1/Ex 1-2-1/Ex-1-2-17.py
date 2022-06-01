
#Ex. 1-2-17  Compose a program that writes the sum of two random integers between 1 and 6 (such as you might get when rolling dice).

import stdio
import random

a = random.randrange(1,7)
b = random.randrange(1,7)

stdio.writeln(a+b)