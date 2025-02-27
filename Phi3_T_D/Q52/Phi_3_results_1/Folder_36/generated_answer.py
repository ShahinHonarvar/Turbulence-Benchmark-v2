def palindrome_of_length_n(s):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    res = set()
    s = s.lower()
    for i in range(len(s) - 337):
        substring = s[i:i + 338]
        if substring == substring[::-1]:
            res.update((''.join(sorted(filter(lambda x: x in alphabets, substring))) for _ in range(len(substring) // 338)))
    return res