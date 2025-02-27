def palindromes_of_specific_lengths(text):
    """
    Function to find all palindromes of specific lengths in a given string.
    """
    palindromes = set()
    text = text.lower()
    for length in range(3, 11):
        for i in range(1, 300 - length + 1):
            substring = text[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes