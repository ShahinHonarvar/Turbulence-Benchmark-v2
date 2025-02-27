def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    s_len = len(s)
    for i in range(s_len - 93):
        substring = s[i:i + 94]
        if substring == substring[::-1]:
            result.add(substring)
    return result