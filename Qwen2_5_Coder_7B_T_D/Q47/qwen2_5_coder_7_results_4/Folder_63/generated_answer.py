def palindromes_of_specific_lengths(s):
    s = s[33:86].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 2, min(len(s), i + 32)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result