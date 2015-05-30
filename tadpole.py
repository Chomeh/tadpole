import yaml
import sys
import getopt
from tests.DummyTests import *

def useage():
    return "useage: python tadpole.py -f <tests>"

try:
    opts, args = getopt.getopt(sys.argv[1:], "f:")

    dict_opts = dict(opts)
    if "-f" not in dict_opts:
        print(useage())
        sys.exit(2)

except getopt.GetoptError as err:
    # print help information and exit:
    print(err) # will print something like "option -a not recognized"
    print(useage())
    sys.exit(2)

filename = dict_opts["-f"]
tests = yaml.load(open(filename))

passed = 0
for test in tests:
    try:
        if test.run():
            print(test.get_name() + " ... passed")
            passed += 1
        else:
            print(test.get_name() + " ... failed")
    except: #catch all exceptions
        print(test.get_name() + " ... error")

print("total passed " + str(passed) + "/" + str(len(tests)))

