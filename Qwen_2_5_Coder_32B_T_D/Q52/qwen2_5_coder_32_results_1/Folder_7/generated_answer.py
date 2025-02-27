def palindrome_of_length_n(s):
    s = s.lower()
    l = set()
    for i in range(len(s) - 415):
        substring = s[i:i + 416]
        if substring.isalpha() and substring == substring[::-1]:
            l.add(substring)
    return l