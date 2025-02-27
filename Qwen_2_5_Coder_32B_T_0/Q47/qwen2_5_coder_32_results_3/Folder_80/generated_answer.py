def palindromes_of_specific_lengths(s):
    s = s[35:89].lower()
    result = set()
    for i in range(len(s) - 23):
        for j in range(i + 24, min(i + 34, len(s)) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result