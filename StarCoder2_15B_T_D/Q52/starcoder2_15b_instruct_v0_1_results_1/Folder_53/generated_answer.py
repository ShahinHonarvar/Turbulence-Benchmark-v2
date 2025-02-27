def palindrome_of_length_n(string):
    substrings = [string[i:i + 68] for i in range(len(string) - 67)]
    palindromes = [substring for substring in substrings if substring == substring[::-1]]
    return {palindrome for palindrome in palindromes if all((c.isalpha() for c in palindrome))}