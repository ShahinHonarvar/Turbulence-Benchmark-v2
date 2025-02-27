def palindromes_of_specific_lengths(s):
    s = s[12:93].lower()
    result = set()
    for i in range(len(s)):
        for l in range(17, 67):
            if i + l <= len(s):
                substring = s[i:i + l]
                if substring.isalpha() and substring == substring[::-1]:
                    result.add(substring)
    return result