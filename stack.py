EXIT = '-1'

def main():
	stack = []
	while True:
		your_words = input('Your words: ')
		if your_words == EXIT:
			break
		stack.append(your_words)
	while len(stack) != 0:
		ele = stack.pop()
		print(ele)




if __name__ == '__main__':
	main()