from itertools import permutations

def palindromes_between_indices(s):
    letters = s[2:5].lower()
    letters_set = set(letters)
    palindromes = set()
    for length in range(4, len(letters_set) + 1):
        for perm in permutations(letters_set, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes