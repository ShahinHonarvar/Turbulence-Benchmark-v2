def palindromes_of_specific_lengths(s):
    s = s[10:60].lower()
    palindromes = set()
    for i in range(len(s)):
        for length in range(18, 37):
            if i + length <= len(s):
                substring = s[i:i + length]
                if substring.isalpha() and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes