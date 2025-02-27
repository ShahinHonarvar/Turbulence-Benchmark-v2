def palindrome_of_length_n(s):
    """
    Finds all palindromes of length n in a given string.
    """
    n = 27
    res = set()
    for i in range(len(s) - n + 1):
        window = s[i:i + n]
        if window == window[::-1]:
            res.add(window)
    return res