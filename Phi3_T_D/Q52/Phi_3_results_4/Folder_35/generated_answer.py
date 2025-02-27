def palindrome_of_length_n(s):
    pa = set()
    s = s.lower()
    length = 116
    for i in range(len(s) - length + 1):
        if s[i:i + length] == s[i:i + length][::-1]:
            pa.add(s[i:i + length].lower())
    return pa