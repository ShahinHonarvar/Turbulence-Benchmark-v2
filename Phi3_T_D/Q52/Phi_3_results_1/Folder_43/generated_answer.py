def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = {s[i:i + 51] for i in range(len(s) - 50) if s[i:i + 51].isalpha() and s[i:i + 51] == s[i:i + 51][::-1]}
    return palindromes