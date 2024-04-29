from functools import partial
from TestcaseGenerator import GenerateTestcases, GenerateRandomInt, GenerateRandomIntArray, IntArrayToString

DIRECTORY = "8-A"

s1 = """3 0
"""

s2 = """3 1
2
"""

s3 = """200000 10
50000 20000 90000 30000 70000 40000 60000 10000 80000 100000
"""

s4 = """1 1
1
"""

s5 = """2 2
1 2
"""

def s(x):
    return x

def gen_f():
    N = GenerateRandomInt(1, 200000)
    K = GenerateRandomInt(0, N, weight = -30)
    arr = GenerateRandomIntArray(K, 1, N, duplicate = False)
    return IntArrayToString([N, K]) + IntArrayToString(arr)

GenerateTestcases(1, DIRECTORY, partial(s, x = s1))
GenerateTestcases(2, DIRECTORY, partial(s, x = s2))
GenerateTestcases(3, DIRECTORY, partial(s, x = s3))
GenerateTestcases(4, DIRECTORY, partial(s, x = s4))
GenerateTestcases(5, DIRECTORY, partial(s, x = s5))
GenerateTestcases((6, 20), DIRECTORY, gen_f)