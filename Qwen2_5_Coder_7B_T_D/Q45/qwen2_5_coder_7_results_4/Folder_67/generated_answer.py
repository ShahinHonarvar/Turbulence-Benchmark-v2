import itertools

def palindromes_between_indices(s):
    letters = set(s[2:7].lower())
    length = 5
    palindromes = set()
    while length <= len(letters):
        for p in itertools.permutations(letters, length):
            candidate = ''.join(p)
            if candidate == candidate[::-1] and len(candidate) >= length:
                palindromes.add(candidate)
        length += 1
    return palindromes