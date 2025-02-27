def palindrome_of_length_at_least_n(string):
    """
    Returns the set of all palindromes of the length greater than or equal to 59 that exist in the given string.
    Each palindrome should only consist of English letters. If no such palindromes exist in the given string,
    the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
    """
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 59):
        window = string[i:i + 59]
        if window == window[::-1]:
            palindromes.add(window)
    return palindromes