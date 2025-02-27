def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    n = len(s)
    for start in range(n):
        for end in range(start + 69, n):
            substring = s[start:end + 1]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result