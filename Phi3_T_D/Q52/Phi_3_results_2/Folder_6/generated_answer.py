def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i - 237:i + 238] for i in range(237, len(s)) if s[i:i + 474] == s[i:i + 474][::-1]}