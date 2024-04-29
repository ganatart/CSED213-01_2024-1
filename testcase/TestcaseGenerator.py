import os
import random
from typing import Any, Callable
from subprocess import Popen, PIPE

# fix random seed
SEED = 42
random.seed(42)

# solver path
SOLVER_PATH = "C:\\Users\\qjatn\\Desktop\\PS\\bin\\Debug\\PS.exe"


def GenerateTestcases(index: int | tuple[int, int], dir: str, gen_f: Callable[[None], str], solver: str = SOLVER_PATH) -> None:
	"""
		Generate testcase input files

		Parameters
		----------
		index: tupe[int, int]
			Index of testcase file
			Includes end range
		dir: str
			Folder directory to generate testcase file
		gen_f: Callable[[None], str]
			Function that generates input
		solver: str
			Solver EXE file path
			This solver should receive input by STDIN and
			print output by STDOUT
	"""
	if type(index) == int:
		index = (index, index)
	
	# make directory to dir
	os.makedirs(dir, exist_ok = True)

	# save input and output files
	for i in range(index[0], index[1] + 1):
		# generate random input
		input = gen_f()
		input = input.strip() + "\n"

		# run solver
		p = Popen([solver], stdin = PIPE, stdout = PIPE)
		output = p.communicate(input = input.encode())[0].decode()
		output = output.strip()
		output = output.splitlines()
		output = [l.strip() + "\n" for l in output]

		# write input file
		with open(os.path.join(dir, str(i) + ".in"), "w") as f:
			f.write(input)
			f.close()
		
		# write output file
		with open(os.path.join(dir, str(i) + ".out"), "w") as f:
			f.writelines(output)
			f.close()

def GenerateRandomInt(MIN: int, MAX: int, weight: int = 0) -> int:
	"""
		Generate random int with given weight.
		Higher weight denotes higher probability for closer to max and
		lower weight denotes higher probability for close to min

		Parameters
		----------
		MIN: int
			Minimum value of element
		MAX: int
			Maximum value of element
		weight: int
			Weight to adjust probability

		Returns
		-------
		res: int
			Generated randon int value
	"""

	res = random.randint(MIN, MAX)
	while weight > 0:
		weight -= 1
		res = max(res, random.randint(MIN, MAX))
	while weight < 0:
		weight += 1
		res = min(res, random.randint(MIN, MAX))
	
	return res

def GenerateRandomIntArray(N: int, MIN: int, MAX: int, weight: int = 0, duplicate: bool = True) -> list[int]:
	"""
		Generate Array of length N with random elements

		Parameters
		----------
		N: int
			Length of array to generate.
		min: int 
			Minimum value of array element
		MAX: int
			Maximum value of array element
		weight: int
			Weight to adjust probability
		duplicate: bool
			Allow duplicated value in array if True

		Returns
		-------
		res: list[int]
			Randomly generated array
	"""
	if duplicate:
		# Generate array with random elements
		res = [GenerateRandomInt(MIN, MAX, weight) for _ in range(N)]
	else:
		# Generete array with target elements
		if MAX - MIN < 100000 or 3 * N >= MAX - MIN:
			elements = list(range(MIN, MAX + 1))
			random.shuffle(elements)
			
			if weight > 0:
				for _ in range(weight * len(elements)):
					i = GenerateRandomInt(0, len(elements) - 1)
					j = GenerateRandomInt(0, len(elements) - 1)
					i, j = min(i, j), max(i, j)
					elements[i], elements[j] = max(elements[i], elements[j]), min(elements[i], elements[j])
			if weight < 0:
				for _ in range(-weight * len(elements)):
					i = GenerateRandomInt(0, len(elements) - 1)
					j = GenerateRandomInt(0, len(elements) - 1)
					i, j = min(i, j), max(i, j)
					elements[i], elements[j] = min(elements[i], elements[j]), max(elements[i], elements[j])
		else:
			elements = [GenerateRandomInt(MIN, MAX, weight) for _ in range(3 * N)]
			elements = list(set(elements))
			random.shuffle(elements)
		res = elements[:N]
	
	return res

def GenerateRandomInt2DArray(H: int, W:int, MIN: int, MAX: int, weight = 0) -> list[list[int]]:
	"""
		Generate 2D Array of shape H x W with random elements

		Parameters
		----------
		H: int
			Height of array
		W: int
			Width of array
		min: int 
			Minimum value of array element
		MAX: int
			Maximum value of array element
		weight: int
			Weight to adjust probability
		
		Returns
		-------
		res: list[int]
			Randomly generated array
	"""
	res = [GenerateRandomIntArray(W, MIN, MAX, weight) for _ in range(H)]
	
	return res

def IntArrayToString(arr: list[int], split: str = " ") -> str:
	"""
		Convert int array into single string with line break

		Parameters
		----------
		arr: list[int]
			Int array to convert to string
		split: str
			Split each element by "split"
		
		Returns
		-------
		res: str
			String converted from int array
	"""
	arr = [str(i) for i in arr]
	res = split.join(arr) + "\n"
	return res

def Int2DArrayToString(arr: list[list[int]]) -> str:
	"""
		Convert 2D int array into single string with line break

		Parameters
		----------
		arr: list[list[int]]
			Int array to convert to string
		
		Returns
		-------
		res: str
			String converted from int array
	"""
	arr = [IntArrayToString(a) for a in arr]
	res = "".join(arr) + "\n"
	return res