def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 54] for i in range(len(s) - 53) if s[i:i + 54] == s[i:i + 54][::-1]}