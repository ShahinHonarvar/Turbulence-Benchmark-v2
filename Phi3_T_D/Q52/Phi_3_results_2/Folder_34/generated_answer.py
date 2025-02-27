def palindrome_of_length_n(s):
    s = s.lower()
    result = {s[i:i + 33] for i in range(len(s) - 32) if s[i:i + 33] == s[i:i + 33][::-1] and s[i:i + 33].isalpha()}
    return result