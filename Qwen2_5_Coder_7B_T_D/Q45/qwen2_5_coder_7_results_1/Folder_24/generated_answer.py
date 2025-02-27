def palindromes_between_indices(s):
    s = s[2:10].lower()
    letters = set(s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 4, len(s) + 1):
            for p in permutations(s[i:j]):
                if p == p[::-1]:
                    palindromes.add(''.join(p))
    return palindromes