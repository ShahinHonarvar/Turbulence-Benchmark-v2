def palindromes_of_specific_lengths(s):
    s = s[119:257].lower()
    palindromes = set()
    for start in range(len(s)):
        for length in range(104, 124):
            if start + length <= len(s):
                substring = s[start:start + length]
                if substring.isalpha() and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes