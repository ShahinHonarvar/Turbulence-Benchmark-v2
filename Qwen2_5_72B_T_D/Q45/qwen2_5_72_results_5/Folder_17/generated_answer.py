import itertools

def palindromes_between_indices(s):
    substring = s[2:7].lower()
    valid_chars = ''.join([char for char in substring if char.isalpha()])
    palindromes = set()
    for length in range(4, len(valid_chars) + 1):
        for perm in itertools.permutations(valid_chars, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes