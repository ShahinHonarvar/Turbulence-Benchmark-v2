def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 6] for i in range(len(s) - 5) if s[i:i + 6].isalpha() and s[i:i + 6] == s[i:i + 6][::-1]}