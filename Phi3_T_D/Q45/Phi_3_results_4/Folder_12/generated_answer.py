from itertools import permutations

def palindromes_between_indices(s):
    start, end = (3, 8)
    selected_chars = s[start:end + 1].lower()
    palindromes = set()
    for length in range(4, len(selected_chars) + 1, 2):
        for perm in permutations(selected_chars, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes