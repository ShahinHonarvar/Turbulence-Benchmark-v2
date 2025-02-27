def palindromes_of_specific_lengths(s):
    s = s[119:257].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 104, min(i + 124, len(s)) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result