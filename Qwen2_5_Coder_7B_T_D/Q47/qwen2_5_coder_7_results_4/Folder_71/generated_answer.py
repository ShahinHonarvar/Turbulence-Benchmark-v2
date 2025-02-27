def palindromes_of_specific_lengths(s):
    s = s[18:66].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 2, min(len(s), i + 37)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha() and (23 <= len(substring) <= 36):
                result.add(substring)
    return result