def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 20] for i in range(len(s) - 19) if s[i:i + 20].isalpha() and s[i:i + 20] == s[i:i + 20][::-1]}