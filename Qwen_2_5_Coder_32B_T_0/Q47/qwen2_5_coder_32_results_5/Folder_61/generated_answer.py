def palindromes_of_specific_lengths(s):
    s = s[:31].lower()
    result = set()
    for i in range(len(s) - 19):
        for j in range(i + 20, min(i + 31, len(s)) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result