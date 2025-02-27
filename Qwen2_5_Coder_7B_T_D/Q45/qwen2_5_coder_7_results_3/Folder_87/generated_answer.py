def palindromes_between_indices(s):
    substring = s[3:10].lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = set()
    for length in range(3, len(substring) + 1):
        for perm in permutations(alphabet, length):
            perm_str = ''.join(perm)
            if perm_str in substring and perm_str == perm_str[::-1]:
                result.add(perm_str)
    return result