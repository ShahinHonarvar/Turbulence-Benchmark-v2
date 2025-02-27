def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 149
    result = set()
    for start in range(len(s)):
        for end in range(start + n, len(s) + 1):
            substring = s[start:end]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result