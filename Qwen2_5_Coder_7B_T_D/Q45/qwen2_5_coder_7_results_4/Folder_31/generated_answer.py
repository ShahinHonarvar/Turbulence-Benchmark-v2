from itertools import permutations

def palindromes_between_indices(s):
    letters = set(s[1:9].lower())
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for perm in permutations(letters, length):
            half = ''.join(perm)
            if half == half[::-1]:
                palindromes.add(half * 2 if length % 2 == 0 else half + half[-2::-1])
    return palindromes