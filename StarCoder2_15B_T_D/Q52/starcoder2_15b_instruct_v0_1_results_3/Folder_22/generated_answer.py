def palindrome_of_length_n(string):
    substrings = [string[i:i + 20] for i in range(len(string) - 19)]
    palindromes = [substring for substring in substrings if substring == substring[::-1]]
    uppercase_palindromes = {palindrome.upper() for palindrome in palindromes}
    return uppercase_palindromes