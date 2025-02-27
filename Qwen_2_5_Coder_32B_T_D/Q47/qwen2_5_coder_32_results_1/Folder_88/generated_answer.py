def palindromes_of_specific_lengths(s):
    s = s[11:88].lower()
    result = set()
    for i in range(len(s) - 3):
        for l in range(4, 6):
            if i + l <= len(s):
                substring = s[i:i + l]
                if substring.isalpha() and substring == substring[::-1]:
                    result.add(substring)
    return result