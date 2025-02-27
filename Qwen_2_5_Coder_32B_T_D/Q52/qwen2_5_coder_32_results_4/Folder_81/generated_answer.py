def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    n = len(s)
    l = 99
    for i in range(n - l + 1):
        substring = s[i:i + l]
        if substring.isalpha() and substring == substring[::-1]:
            result.add(substring)
    return result