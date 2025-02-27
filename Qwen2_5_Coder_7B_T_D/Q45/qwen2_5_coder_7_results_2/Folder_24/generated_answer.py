from itertools import permutations

def palindromes_between_indices(s):
    letters = s[2:10]
    letters = ''.join(filter(str.isalpha, letters)).lower()
    unique_letters = set(letters)
    if len(unique_letters) < 2:
        return set()
    palindromes = set()
    for length in range(4, len(unique_letters) + 1):
        for perm in permutations(unique_letters, length):
            half = ''.join(perm)
            if half == half[::-1]:
                palindromes.add(half + half[::-1][1:])
    return palindromes