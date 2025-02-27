def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 31):
        for j in range(i + 31, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1] and len(substring) >= 32:
                result.add(substring)
    return result