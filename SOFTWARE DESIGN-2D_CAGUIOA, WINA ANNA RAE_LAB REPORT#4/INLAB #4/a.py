def find_min(sequence,y):

    if y == 1:
        return sequence[0]
    return min(sequence[y-1],find_min(sequence, y-1))

def find_max(sequence,y):
    if y == 1:
        return sequence[0]
    return max(sequence[y-1],find_max(sequence,y-1))

if __name__ == '__main__':
    sequence = [0,11,19,28,4,33,1,3]
    y = len(sequence)
    print("The miniminum number in the sequence: ", find_min(sequence,y))
    print("The maximum number in the sequence: ", find_max(sequence,y))