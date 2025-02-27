def palindrome_of_length_n(text):
    """
    Returns the set of all palindromes of length n in the given text.
    """
    n = 2 ** 10
    palindromes = set()
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if substring == substring[::-1]:
            if all((ch.isalpha() for ch in substring)):
                palindromes.add(substring)
    return palindromes