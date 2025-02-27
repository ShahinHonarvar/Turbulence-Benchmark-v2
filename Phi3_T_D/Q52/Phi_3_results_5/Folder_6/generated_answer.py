def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 473):
        if s[i:i + 474] == s[i:i + 474][::-1]:
            result.add(s[i:i + 474])
    return result