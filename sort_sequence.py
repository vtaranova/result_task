def sort(sequence):
    length = len(sequence)
    if length == 0:
        return []
    tmp = sequence[0]
    for i in range(0, length):
        for j in range(i + 1, length):
            if sequence[j] < sequence[i]:
                tmp = sequence[j]
                sequence[j] = sequence[i]
                sequence[i] = tmp
    return sequence

