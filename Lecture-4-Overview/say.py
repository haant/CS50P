import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])

# OR

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])