def palindrome_of_length_n(string):
    """
    Find all palindromes of length 85 as substrings of the given string.
    """
    palindromes = set()
    for i in range(len(string) - 84):
        substring = string[i:i + 85]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes