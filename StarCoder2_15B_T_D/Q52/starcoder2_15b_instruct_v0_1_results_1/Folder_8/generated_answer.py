def palindrome_of_length_n(string):
    """
    Finds all palindromes of length 49 as substrings of the given string.
    """
    palindromes = set()
    for i in range(len(string) - 48):
        substring = string[i:i + 49]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes