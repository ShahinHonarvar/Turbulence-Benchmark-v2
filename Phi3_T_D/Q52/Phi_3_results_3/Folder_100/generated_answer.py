def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:j] for i in range(len(s)) for j in range(i + 91, len(s) + 1) if s[i:j].isalpha() and s[i:j] == s[i:j][::-1]}