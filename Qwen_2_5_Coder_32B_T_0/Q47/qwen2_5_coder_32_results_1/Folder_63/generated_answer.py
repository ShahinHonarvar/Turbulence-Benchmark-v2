def palindromes_of_specific_lengths(s):
    s = s[33:86].lower()
    result = set()
    for i in range(len(s) - 25):
        for j in range(i + 26, min(i + 32, len(s)) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result