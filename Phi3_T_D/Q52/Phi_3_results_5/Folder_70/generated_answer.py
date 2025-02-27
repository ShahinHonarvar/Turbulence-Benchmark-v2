def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 401] for i in range(len(s) - 399) if s[i:i + 401] == s[i:i + 401][::-1]}