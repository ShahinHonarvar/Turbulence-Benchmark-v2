import itertools
    from collections import Counter

def palindromes_between_indices(s):
    s = s[3:8].lower()
    letters = set(s)
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for combination in itertools.permutations(letters, length):
            half = ''.join(combination[:length // 2])
            if length % 2 == 1:
                palindromes.add(half + half[-2::-1].lower())
            else:
                palindromes.add(half + half[::-1].lower())
    return palindromes