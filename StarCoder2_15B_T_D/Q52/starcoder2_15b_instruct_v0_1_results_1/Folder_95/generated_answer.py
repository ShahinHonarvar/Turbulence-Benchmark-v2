def palindrome_of_length_n(text):
    """
    Returns a set of all palindromes of length 87 as substrings of the given text.
    """
    n = 87
    text = text.lower()
    result = set()
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if substring == substring[::-1]:
            result.add(substring)
    return result