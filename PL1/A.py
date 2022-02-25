from sys import stdin, stdout

def read_all():
	return stdin.readlines()

def readln():
	return stdin.readline().rstrip()

def outln(n):
	stdout.write(str(n) + "\n")

def fairness(data):
	N = len(data)
	for i in range(N):
		j = i + 1
		k = N - 1
		while j < k:
			s = data[i] + data[j] + data[k]
			if s < 0:
				j += 1
			elif s > 0:
				k -= 1
			else:
				return "Fair"
	return "Rigged"

if __name__ == '__main__':
	
	readln()
	
	data = list(map(lambda line: int(line.strip("\n\r ")), read_all() ) )

	while len(data):
		next_ind = data.index(0)
		data_aux = sorted(data[:next_ind])
		outln(fairness(data_aux))
		data = data[next_ind+2:]
