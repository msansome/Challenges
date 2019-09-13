questions ={
1:('''
The capital of France is:
1. London
2. Rome
3. Paris
4. Berlin
''',3),
2:('''
Hesham's favourite subject is:
1. Mathematics
2. Computer Science
3. Geography
4. Domestic Science
''',2)
}

total =0
numQs = len(questions)

for i in range (1,numQs+1):
	print('Question',i, ':\n',questions[i][0])
	print()
	ans = int(input())
	if ans == questions[i][1]:
		total += 1
		print("Well done! That's right. Your score so far is",total)
	else:
		print("Sorry, that's wrong. Your score so far is",total)
print("\nYou scored", total, "out of a possible", numQs)

