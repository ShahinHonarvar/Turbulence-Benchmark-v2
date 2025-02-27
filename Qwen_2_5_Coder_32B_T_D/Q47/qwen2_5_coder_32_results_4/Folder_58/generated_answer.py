def palindromes_of_specific_lengths(s):
    s = s[125:284].lower()
    palindromes = set()
    for start in range(len(s) - 108):
        for length in range(109, 127):
            if start + length <= len(s):
                substring = s[start:start + length]
                if substring.isalpha() and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes