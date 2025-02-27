import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:9] if c.isalpha()]
    palindromes = set()
    for perm in set(itertools.permutations(letters, min(7, len(letters)))):
        perm_str = ''.join(perm)
        for i in range(len(perm_str) - 6):
            candidate = perm_str[i:i + 7]
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes