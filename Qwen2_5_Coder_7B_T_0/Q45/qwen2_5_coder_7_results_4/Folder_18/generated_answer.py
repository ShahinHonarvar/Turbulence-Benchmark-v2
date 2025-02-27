def palindromes_between_indices(s):
    s = s[1:7].lower()
    letters = set(s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            sub = ''.join(sorted(s[i:j]))
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes