def palindrome_of_length_n(text):
    """
    Finds all palindromes of length 72 in the given text and returns them as a set.
    """
    palindromes = set()
    text = text.lower()
    for i in range(len(text) - 72 + 1):
        substring = text[i:i + 72]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes