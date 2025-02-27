def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 35] for i in range(len(s) - 34) if s[i:i + 35] == s[i:i + 35][::-1]}