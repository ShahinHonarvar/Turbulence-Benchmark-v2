def palindromes_between_indices(s):
    s = s[1:10].lower()
    letters = set(s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 6, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) >= 7:
                palindromes.add(substring)
    return palindromes