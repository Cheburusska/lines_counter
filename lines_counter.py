import sys
import os.path

path_to_file = sys.argv[1]

def count_lines_in_file (path_to_file):
	if not os.path.exists(path_to_file):
		return None
	counter = 0
	with open(path_to_file) as file:
			for line in file:
				counter +=1
	return counter

if __name__ == '__main__':
	print (count_lines_in_file(path_to_file))
