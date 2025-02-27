def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = {s[i:i + 18] for i in range(len(s) - 17) if s[i:i + 18] == s[i:i + 18][::-1] and s[i:i + 18].isalpha()}
    return palindromes