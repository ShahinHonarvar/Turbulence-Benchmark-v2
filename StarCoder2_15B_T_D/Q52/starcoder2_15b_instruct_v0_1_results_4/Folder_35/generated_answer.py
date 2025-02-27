def palindrome_of_length_n(s):
    substrings = [s[i:i + 116] for i in range(len(s) - 115)]
    palindromes = [substring for substring in substrings if substring == substring[::-1]]
    return set(palindromes)