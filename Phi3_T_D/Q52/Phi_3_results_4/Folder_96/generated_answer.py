def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 83] for i in range(len(s) - 82) if s[i:i + 83].isalpha() and s[i:i + 83] == s[i:i + 83][::-1]}