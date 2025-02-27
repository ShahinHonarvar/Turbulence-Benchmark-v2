def palindrome_of_length_n(string):
    """
    Finds the set of all palindromes of length n in a given string.
    """
    n = 29
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes