def palindromes_of_specific_lengths(s):
    s = s[26:91].lower()
    result = set()
    for i in range(len(s)):
        for j in range(27, 59):
            if i + j <= len(s):
                substring = s[i:i + j]
                if substring.isalpha() and substring == substring[::-1]:
                    result.add(substring)
    return result