def palindrome_of_length_n(s):
    s = s.lower()
    result = {s[i:i + 4] for i in range(len(s) - 3) if s[i] == s[i + 3] and s[i + 1] == s[i + 2]}
    return result