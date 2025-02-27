def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = {s[i:j] for i in range(len(s)) for j in range(i + 40, len(s) + 1) if s[i:j].isalpha() and s[i:j] == s[j - 1:i - 1:-1]}
    return palindromes