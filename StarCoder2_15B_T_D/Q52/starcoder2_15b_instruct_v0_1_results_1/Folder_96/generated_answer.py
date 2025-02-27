def palindrome_of_length_n(string):
    substrings = [string[i:i + 83] for i in range(len(string) - 82)]
    palindromes = [substring for substring in substrings if substring == substring[::-1]]
    filtered_palindromes = [palindrome for palindrome in palindromes if palindrome.isalpha()]
    return set(filtered_palindromes)