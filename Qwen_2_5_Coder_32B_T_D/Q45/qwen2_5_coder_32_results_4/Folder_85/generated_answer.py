import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(lambda x: x.isalpha(), s[2:9])).lower()
    palindromes = set()
    for perm in itertools.permutations(letters, 7):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes