def palindromes_of_specific_lengths(s):
    s = s[10:60].lower()
    palindromes = set()
    for length in range(18, 37):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes