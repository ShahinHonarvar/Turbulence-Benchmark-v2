def palindrome_of_length_n(string):
    substrings = [string[i:i + 45] for i in range(len(string) - 44)]
    palindromes = [substr for substr in substrings if substr == substr[::-1]]
    filtered_palindromes = list(filter(lambda x: x.isalpha(), palindromes))
    return set(filtered_palindromes)