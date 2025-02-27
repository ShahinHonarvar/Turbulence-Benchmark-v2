def palindromes_of_specific_lengths(s):
    s = s[15:87].lower()
    result = set()
    for i in range(len(s) - 50):
        for j in range(i + 50, min(i + 60, len(s)) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result