def palindromes_of_specific_lengths(s):
    s = s[:10].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 3, min(i + 6, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result