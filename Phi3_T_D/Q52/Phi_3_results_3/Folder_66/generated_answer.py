def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = {s[i:i + 25] for i in range(len(s) - 24) if s[i:i + 25].isalpha() and s[i:i + 25] == s[i:i + 25][::-1]}
    return palindromes