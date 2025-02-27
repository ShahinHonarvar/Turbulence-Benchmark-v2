def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 53] for i in range(len(s) - 52) if s[i:i + 53] == s[i:i + 53][::-1] and s[i:i + 53].isalpha()}