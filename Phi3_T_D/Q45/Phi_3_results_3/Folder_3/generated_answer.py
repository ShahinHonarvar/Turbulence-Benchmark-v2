from itertools import permutations

def palindromes_between_indices(input_string):
    start, end = (7, 9)
    possible_chars = [char.lower() for char in input_string[start:end + 1]]
    palindromes = set()
    for length in range(3, len(possible_chars) + 1):
        for perm in permutations(possible_chars, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes