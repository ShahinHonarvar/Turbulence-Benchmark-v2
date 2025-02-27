def palindromes_of_specific_lengths(s):
    s = s[26:91].lower()
    palindromes = set()
    for i in range(len(s)):
        for l in range(27, 59):
            if i + l <= len(s):
                substring = s[i:i + l]
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes