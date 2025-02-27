def palindromes_between_indices(s):
    s = s[5:10].lower()
    letters = set(s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 4, len(s) + 1):
            candidate = ''.join(sorted(s[i:j]))
            if candidate == candidate[::-1] and candidate not in palindromes:
                palindromes.add(candidate)
    return palindromes