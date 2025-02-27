def palindrome_of_length_n(s):
    n = 25
    s = s.lower()
    result = set()
    for i in range(len(s) - n + 1):
        if s[i:i + n] == s[i:i + n][::-1] and s[i:i + n].isalpha():
            result.add(s[i:i + n])
    return result