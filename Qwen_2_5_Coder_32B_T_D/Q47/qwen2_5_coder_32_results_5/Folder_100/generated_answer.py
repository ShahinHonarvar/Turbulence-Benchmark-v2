def palindromes_of_specific_lengths(s):
    s = s[29:97].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 11, min(i + 19, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result