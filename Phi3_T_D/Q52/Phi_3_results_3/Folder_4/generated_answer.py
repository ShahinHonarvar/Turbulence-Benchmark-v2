def palindrome_of_length_n(s):
    s = s.lower()
    result = {s[i:i + 15] for i in range(len(s) - 14) if s[i:i + 15] == s[i:i + 15][::-1] and s[i:i + 15].isalpha()}
    return result