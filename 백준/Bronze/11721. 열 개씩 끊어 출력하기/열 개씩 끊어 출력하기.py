in_word=input()
n=len(in_word) # 19

for elem in range(0, n, 10):
    print(in_word[elem:elem+10])