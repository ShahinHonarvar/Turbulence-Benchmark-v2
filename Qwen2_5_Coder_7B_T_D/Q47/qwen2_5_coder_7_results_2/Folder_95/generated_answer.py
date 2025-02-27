def palindromes_of_specific_lengths(s):
    result = set()
    s = s[12:57].lower()
    for i in range(len(s)):
        for j in range(i + 2, min(i + 23, len(s)) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result