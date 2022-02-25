from sys import stdin, stdout

def read_all():
	return stdin.readlines()

def readln():
	return stdin.readline().rstrip()

def outln(n):
	stdout.write(str(n) + "\n")

if __name__ == '__main__':
	time_now = 0
	total_time = 0

	for _ in range(int(readln())):
		arival, duration = list(map(int, readln().split()))
		#print(f"res: total ->{total_time}\n     now ->{time_now}")
		#print(f"in: arive ->{arival}\n    duration ->{duration}")

		if arival > time_now:
			total_time += (arival-time_now) + duration
			time_now = arival + duration
		else:
			time_now += duration
			total_time += duration
	#print(f"res: total ->{total_time}\n     now ->{time_now}")
	#outln("")
	outln(total_time)