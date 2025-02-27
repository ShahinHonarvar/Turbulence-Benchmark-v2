def palindrome_of_length_n(s):
    s = s.lower()
    len_s = len(s)
    result = set()
    for i in range(len_s - 115):
        if s[i:i + 116] == s[i:i + 116][::-1]:
            result.add(s[i:i + 116])
    return result