def palindrome_of_length_n(s):
    n = 48
    s = s.lower()
    palindromes = {s[i:i + n] for i in range(len(s) - n + 1) if s[i:i + n].isalpha() and s[i:i + n] == s[i:i + n][::-1]}
    return palindromes