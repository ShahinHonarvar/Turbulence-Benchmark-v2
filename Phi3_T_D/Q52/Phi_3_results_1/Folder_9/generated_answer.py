def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = {s[i:i + 72] for i in range(len(s) - 71) if s[i:i + 72].isalpha() and s[i:i + 72].replace(' ', '') == s[i:i + 72][::-1]}
    return palindromes