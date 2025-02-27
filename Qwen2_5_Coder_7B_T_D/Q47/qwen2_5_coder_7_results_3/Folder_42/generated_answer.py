def palindromes_of_specific_lengths(s):
    s = s[43:96]
    s = ''.join(filter(str.isalpha, s.lower()))
    palindromes = set()
    for length in range(18, 48):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes