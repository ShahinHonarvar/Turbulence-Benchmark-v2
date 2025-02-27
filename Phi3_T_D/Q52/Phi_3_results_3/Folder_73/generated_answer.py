def palindrome_of_length_n(s):
    n = 41
    s = s.lower()
    palindromes = set([s[i:i + n] for i in range(len(s) - n + 1) if s[i:i + n] == s[i:i + n][::-1]])
    return palindromes