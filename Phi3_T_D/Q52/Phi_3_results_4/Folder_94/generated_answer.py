def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = {s[i:i + 93] for i in range(len(s) - 92) if s[i:i + 93].isalpha() and s[i:i + 93] == s[i + 92:i:-1]}
    return palindromes