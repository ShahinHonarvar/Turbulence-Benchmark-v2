def find_subset_of_length_n(elements):
    result = 0
    n = len(elements)
    for i in range(2 ** n):
        if bin(i).count('1') == 180:
            result += 1
    return result