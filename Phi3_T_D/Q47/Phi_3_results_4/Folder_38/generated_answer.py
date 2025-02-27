def palindromes_of_specific_lengths(s):
    s = s[18:88]
    s = s.lower()
    palindromes = set()
    for i in range(38, 61):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if all((c.isalpha() for c in substring)) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes