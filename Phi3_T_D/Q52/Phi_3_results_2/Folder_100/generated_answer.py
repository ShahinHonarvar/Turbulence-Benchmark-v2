def palindrome_of_length_n(s):
    s = s.lower()
    length = 91
    res = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1]:
            res.add(substring)
    return res