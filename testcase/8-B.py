from functools import partial
from TestcaseGenerator import GenerateTestcases, GenerateRandomInt, GenerateRandomIntArray, IntArrayToString

DIRECTORY = "8-B"

s1 = """3
"""

s2 = """10
"""

s3 = """1000000000
"""

def s(x):
    return x

def gen_f():
    N = GenerateRandomInt(1, 1000000000)
    return IntArrayToString([N])

GenerateTestcases(1, DIRECTORY, partial(s, x = s1))
GenerateTestcases(2, DIRECTORY, partial(s, x = s2))
GenerateTestcases(3, DIRECTORY, partial(s, x = s3))
GenerateTestcases((4, 20), DIRECTORY, gen_f)