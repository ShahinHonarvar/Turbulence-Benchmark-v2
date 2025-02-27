def palindromes_of_specific_lengths(s):
    s = s[125:284].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 109, min(i + 127, len(s)) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result