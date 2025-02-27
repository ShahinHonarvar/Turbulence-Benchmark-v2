def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 255] for i in range(len(s)) if s[i:i + 255][:255] == s[i:i + 255][:255][::-1] and all((c.isalpha() for c in s[i:i + 255]))}