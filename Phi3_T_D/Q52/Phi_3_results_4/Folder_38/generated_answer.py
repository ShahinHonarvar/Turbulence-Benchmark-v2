def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 38] for i in range(len(s) - 37) if all((s[i + j] == s[i + 37 - j] for j in range(19)))}