def palindromes_between_indices(s):
    letters = s[2:6]
    letters = letters.lower()
    unique_letters = set(letters)
    palindromes = set()
    for i in range(len(unique_letters)):
        for j in range(i + 1, len(unique_letters) + 1):
            for perm in itertools.permutations(unique_letters, j):
                perm_str = ''.join(perm)
                if perm_str == perm_str[::-1] and len(perm_str) >= 4:
                    palindromes.add(perm_str)
    return palindromes