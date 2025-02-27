def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    result = set()
    for i in range(n - 86):
        substring = s[i:i + 87]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result