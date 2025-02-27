def palindrome_of_length_n(s):
    substrings = {s[i:i + 77] for i in range(len(s) - 76)}
    palindromes = {substring for substring in substrings if substring == substring[::-1] and substring.isalpha()}
    return palindromes