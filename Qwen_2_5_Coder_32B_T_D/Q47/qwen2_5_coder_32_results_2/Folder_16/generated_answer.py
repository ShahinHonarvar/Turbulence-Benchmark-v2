def palindromes_of_specific_lengths(s):
    s = s[15:87].lower()
    result = set()
    for i in range(len(s) - 50):
        for j in range(51, 61):
            if i + j <= len(s):
                substring = s[i:i + j]
                if substring.isalpha() and substring == substring[::-1]:
                    result.add(substring)
    return result