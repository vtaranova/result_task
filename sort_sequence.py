def sort(sequence):
    length = len(sequence)
    if length == 0:
        return []
    for i in range(0, length):
        for j in range(i + 1, length):
            if sequence[j] < sequence[i]:
                sequence[j], sequence[i] = sequence[i], sequence[j]
    return sequence

