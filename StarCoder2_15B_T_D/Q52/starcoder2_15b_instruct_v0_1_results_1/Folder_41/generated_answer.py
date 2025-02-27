def palindrome_of_length_n(string):
    """
    Finds all palindromes of length 60 as substrings of the given string.
    """
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 59):
        substring = string[i:i + 60]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes