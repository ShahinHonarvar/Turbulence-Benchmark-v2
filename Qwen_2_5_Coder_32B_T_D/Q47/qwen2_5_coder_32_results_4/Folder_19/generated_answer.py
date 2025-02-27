def palindromes_of_specific_lengths(s):
    s = s[10:56].lower()
    palindromes = set()
    for start in range(len(s) - 2):
        for end in range(start + 3, min(start + 8, len(s)) + 1):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes