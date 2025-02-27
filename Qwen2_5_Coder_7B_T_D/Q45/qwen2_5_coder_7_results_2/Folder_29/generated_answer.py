def palindromes_between_indices(s):
    s = s[2:10]
    letters = set(s.lower())
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for comb in combinations(letters, length):
            for perm in permutations(comb):
                palindrome = ''.join(perm) + ''.join(perm[::-1][1:])
                if len(palindrome) == 2 * length and palindrome.lower() in s:
                    palindromes.add(palindrome)
    return palindromes