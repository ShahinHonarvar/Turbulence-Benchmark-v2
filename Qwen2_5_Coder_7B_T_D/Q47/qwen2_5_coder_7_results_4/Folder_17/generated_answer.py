def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    for i in range(22, 96):
        for j in range(i + 52, min(i + 56, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result