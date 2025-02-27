def palindrome_of_length_n(s):
    s = s.lower()
    P = set()
    n = 45
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring.isalpha() and substring == substring[::-1]:
            P.add(substring)
    return P