def palindrome_of_length_n(string):
    substrings = [string[i:i + 16] for i in range(len(string) - 15)]
    palindromes = [substring for substring in substrings if substring == substring[::-1]]
    filtered_palindromes = filter(lambda x: x.isalpha(), palindromes)
    return set(filtered_palindromes)