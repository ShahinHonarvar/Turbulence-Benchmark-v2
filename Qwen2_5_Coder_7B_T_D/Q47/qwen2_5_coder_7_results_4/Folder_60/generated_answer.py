def palindromes_of_specific_lengths(s):
    result = set()
    s = s[23:83].lower()
    for i in range(len(s)):
        for j in range(i + 32, min(i + 35, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result