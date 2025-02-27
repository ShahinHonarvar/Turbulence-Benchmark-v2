def palindrome_of_length_n(s):
    s = s.lower()
    charset = set('abcdefghijklmnopqrstuvwxyz')
    result = set()
    for i in range(len(s) - 27):
        substring = s[i:i + 28]
        if all((c in charset for c in substring)):
            if substring == substring[::-1]:
                result.add(substring)
    return result