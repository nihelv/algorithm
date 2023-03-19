def solution(array):
    answer = 0

    freq = {}

    for num in array:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    max_freq = max(freq.values())

    if list(freq.values()).count(max_freq) > 1:
        answer = -1
    else:
        answer = max(freq, key=freq.get)

    return answer