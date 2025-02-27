def palindromes_between_indices(s):
    s = s[1:8].lower()
    chars = set(s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                for perm in permutations(substr):
                    if len(set(perm)) == len(perm):
                        palindromes.add(''.join(perm))
    return palindromes