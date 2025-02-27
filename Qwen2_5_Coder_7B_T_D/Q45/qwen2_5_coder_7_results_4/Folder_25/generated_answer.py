def palindromes_between_indices(s):
    letters = s[1:5].lower()
    unique_letters = set(letters)
    palindromes = set()
    for length in range(3, len(unique_letters) + 1):
        for perm in set(permutations(unique_letters, length)):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes