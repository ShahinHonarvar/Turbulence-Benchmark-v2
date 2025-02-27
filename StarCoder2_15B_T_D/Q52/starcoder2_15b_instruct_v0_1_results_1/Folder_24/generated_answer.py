def palindrome_of_length_n(s):
    """
    Returns the set of all palindromes of the length equal to 29, where each palindrome is a substring of the given string.
    """
    s = s.lower()
    n = 29
    result = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            result.add(substring)
    return result