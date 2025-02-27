def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 76] for i in range(len(s) - 75) if s[i:i + 76] == s[i:i + 76][::-1]}