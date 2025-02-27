def palindrome_of_length_n(s):
    length = 223
    s = s.lower()
    palindromes = {s[i:i + length] for i in range(len(s) - length + 1) if s[i:i + length].isalpha() and s[i:i + length] == s[i + length - 1:i - 1:-1]}
    return palindromes