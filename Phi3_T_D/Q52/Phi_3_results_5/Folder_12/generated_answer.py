def palindrome_of_length_n(s):
    s = s.lower()
    length = 23
    return {s[i:i + length] for i in range(len(s) - length + 1) if s[i:i + length] == s[i:i + length][::-1]}