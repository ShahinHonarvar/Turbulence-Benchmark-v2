def palindromes_of_specific_lengths(s):
    result = set()
    s = s[10:60].lower()
    for i in range(len(s)):
        for j in range(i, min(i + 37, len(s))):
            substring = s[i:j + 1]
            if substring == substring[::-1] and len(substring) >= 18 and (len(substring) <= 36) and substring.isalpha():
                result.add(substring)
    return result