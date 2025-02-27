def palindrome_of_length_n(s):
    length = 4
    s = s.lower()
    return {s[i:i + length] for i in range(len(s) - length + 1) if s[i:i + length] == s[i:i + length][::-1]}