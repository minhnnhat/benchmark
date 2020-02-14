tokens = []
with open('token.txt', 'r') as lines:
	tokens = [line.strip() for line in lines if len(line.strip()) > 20]


print(tokens)
