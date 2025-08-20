import sys

ORIGEM = "facebook.com"
DESTINO = "http://google.com"

def main():
	while True:
		line = sys.stdin.readline()
		if not line:
			break

		line = line.stip()
		parts = line.split()

		if len(parts) < 1:
			print()
			sys.stdout.flush()
			continue

		url = parts[0]

		if ORIGEM in url:
			print(f"{url} 301: {DESTINO}")
		else:
			print()

		sys.stdout.flush()

if __name__ == "__main__":
	main()
