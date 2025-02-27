def palindromes_between_indices(s):
    letters = set(s[:7].lower())
    if len(letters) < 7:
        return set()
    palindrome_set = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            for perm in set(permutations(letters, j)):
                perm_str = ''.join(perm)
                if perm_str == perm_str[::-1]:
                    palindrome_set.add(perm_str)
    return palindrome_set