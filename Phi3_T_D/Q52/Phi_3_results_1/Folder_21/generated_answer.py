def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 407] for i in range(len(s) - 406) if s[i:i + 407] == s[i:i + 407][::-1] and all((c.isalpha() for c in s[i:i + 407]))}