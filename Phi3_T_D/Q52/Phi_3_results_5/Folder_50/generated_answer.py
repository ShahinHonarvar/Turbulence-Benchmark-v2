def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 40] for i in range(len(s) - 39) if s[i:i + 40] == s[i:i + 40][::-1]}