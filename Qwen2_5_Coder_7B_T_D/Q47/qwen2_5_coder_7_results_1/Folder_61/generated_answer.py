def palindromes_of_specific_lengths(s):
    s = s[:31].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 20, min(len(s), i + 31)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha() and (20 <= len(substring) <= 30):
                result.add(substring)
    return result