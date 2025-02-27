def palindromes_of_specific_lengths(s):
    s = s[18:88].lower()
    result = set()
    for i in range(len(s) - 2):
        for j in range(i + 2, min(len(s), i + 61)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha() and (38 <= len(substring) <= 60):
                result.add(substring)
    return result