def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 206] for i in range(len(s) - 205) if s[i:i + 206] == s[i:i + 206][::-1]}