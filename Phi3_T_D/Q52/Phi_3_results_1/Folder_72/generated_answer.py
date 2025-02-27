def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 16] for i in range(len(s) - 15) if s[i:i + 16] == s[i:i + 16][::-1]}