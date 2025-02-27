def palindrome_of_length_n(string):
    """
    Finds all palindromes of length 366 in a given string.
    """
    palindromes = set()
    for i in range(len(string) - 366 + 1):
        substring = string[i:i + 366]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes