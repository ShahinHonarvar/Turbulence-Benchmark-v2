def palindromes_of_specific_lengths(s):
    result = set()
    s = s[26:85].lower()
    for i in range(len(s)):
        for j in range(i + 30, min(len(s), i + 47) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result