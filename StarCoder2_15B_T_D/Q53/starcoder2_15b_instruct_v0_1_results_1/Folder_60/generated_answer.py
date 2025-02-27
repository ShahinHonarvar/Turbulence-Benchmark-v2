def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    n = 80
    for i in range(len(s) - n + 1):
        for j in range(i + n - 1, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1]:
                result.add(substring)
    return result