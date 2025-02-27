def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    result = set()
    for i in range(n - 407 + 1):
        substring = s[i:i + 407]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result