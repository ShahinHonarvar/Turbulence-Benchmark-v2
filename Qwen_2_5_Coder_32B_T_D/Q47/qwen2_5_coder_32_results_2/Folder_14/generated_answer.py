def palindromes_of_specific_lengths(s):
    s = s[10:75].lower()
    result = set()
    for i in range(len(s) - 5):
        for l in range(6, 9):
            if i + l <= len(s):
                substring = s[i:i + l]
                if substring.isalpha() and substring == substring[::-1]:
                    result.add(substring)
    return result