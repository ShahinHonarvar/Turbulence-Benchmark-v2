import itertools

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[8:10] if char.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in itertools.permutations(letters, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes