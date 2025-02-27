def palindrome_of_length_n(string):
    """
    Find all palindromes of length 95 in a given string, ignoring case.

    Args:
        string (str): The input string.

    Returns:
        set: A set of all palindromes of length 95 in the given string.
    """
    palindromes = set()
    n = 95
    for i in range(len(string) - n + 1):
        substring = string[i:i + n].lower()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes