def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    n = len(s)
    l = 338
    for i in range(n - l + 1):
        substring = s[i:i + l]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result