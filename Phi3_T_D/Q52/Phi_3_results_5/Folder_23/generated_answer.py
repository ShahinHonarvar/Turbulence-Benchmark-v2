def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 69] for i in range(len(s) - 68) if s[i:i + 69] == s[i:i + 69][::-1] and s[i:i + 69].isalpha()}