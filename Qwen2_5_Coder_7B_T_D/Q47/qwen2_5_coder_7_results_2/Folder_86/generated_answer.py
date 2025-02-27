def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    for i in range(30, 96):
        for j in range(i, 96):
            substring = s[i:j + 1]
            if len(substring) >= 34 and len(substring) <= 55 and (substring == substring[::-1]) and substring.isalpha():
                result.add(substring)
    return result