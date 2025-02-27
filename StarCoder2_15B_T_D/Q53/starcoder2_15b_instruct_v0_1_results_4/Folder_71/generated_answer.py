def palindrome_of_length_at_least_n(s):
    """
    Find all palindromes of length greater than or equal to 87 in a given string.
    Args:
        s (str): The input string.
    Returns:
        set: A set of all palindromes of length greater than or equal to 87.
    """
    s = s.lower()
    palindromes = set()
    n = 87
    for i in range(len(s) - n + 1):
        window = s[i:i + n]
        if window == window[::-1]:
            palindromes.add(window)
    return palindromes