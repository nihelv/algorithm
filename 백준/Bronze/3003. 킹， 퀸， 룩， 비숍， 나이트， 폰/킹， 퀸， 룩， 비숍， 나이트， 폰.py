pieces = [1, 1, 2, 2, 2, 8]
input_pieces = list(map(int, input().split()))

result = [str(pieces[i] - input_pieces[i]) for i in range(6)]

print(' '.join(result))
