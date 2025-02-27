import itertools

def palindromes_between_indices(s):
    letters = [char for char in s[6:9] if char.isalpha()]
    if len(letters) < 4:
        return set()
    unique_letters = set(letters)
    if len(unique_letters) < 2:
        return set()
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in itertools.permutations(letters, length):
            perm_str = ''.join(perm).lower()
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes