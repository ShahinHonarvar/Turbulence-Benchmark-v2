def palindrome_of_length_n(s):
    palindromes = {s[i:i + 445] for i in range(len(s) - 444) if s[i:i + 445].upper() == s[i:i + 445][::-1].upper() and s[i:i + 445].isalpha()}
    return palindromes