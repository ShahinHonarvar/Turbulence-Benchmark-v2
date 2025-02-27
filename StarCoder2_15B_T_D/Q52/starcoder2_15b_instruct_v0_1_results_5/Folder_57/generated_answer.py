def palindrome_of_length_n(string):
    """
    Returns the set of all palindromes of the length equal to 92,
    where each palindrome is a substring of the given string.
    If there is no palindrome of the specified length as a substring,
    the function returns an empty set.
    """
    palindromes = set()
    for i in range(len(string) - 91):
        substring = string[i:i + 92]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes