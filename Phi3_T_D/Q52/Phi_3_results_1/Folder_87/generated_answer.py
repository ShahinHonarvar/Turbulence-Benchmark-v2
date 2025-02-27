def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 57] for i in range(len(s) - 56) if s[i:i + 57] == s[i:i + 57][::-1] and all((c.isalpha() for c in s[i:i + 57]))}