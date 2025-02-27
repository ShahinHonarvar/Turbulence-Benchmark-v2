def palindromes_of_specific_lengths(s):
    s = s[18:89].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 12, min(i + 15, len(s)) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result