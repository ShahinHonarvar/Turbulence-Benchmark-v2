def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 6, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                result.add(substring)
    return result