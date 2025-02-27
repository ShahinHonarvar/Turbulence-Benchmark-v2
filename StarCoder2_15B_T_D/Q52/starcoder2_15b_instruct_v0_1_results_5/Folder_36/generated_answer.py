def palindrome_of_length_n(string):
    """
    Find all palindromes of length 338 in a given string.
    """
    palindromes = set()
    for i in range(len(string) - 338 + 1):
        substring = string[i:i + 338]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes