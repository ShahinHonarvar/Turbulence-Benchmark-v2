def palindrome_of_length_n(s):
    res = set()
    s_upper = s.upper()
    for i in range(len(s_upper) - 39):
        substring = s_upper[i:i + 40]
        if substring == substring[::-1]:
            res.add(substring)
    return res