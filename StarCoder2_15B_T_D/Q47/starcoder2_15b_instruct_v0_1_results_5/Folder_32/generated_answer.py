def palindromes_of_specific_lengths(text):
    """
    Find palindromes in a case-insensitive manner in the substring from index 16 to 77,
    only including palindromes of lengths between 43 and 47.
    """
    palindromes = set()
    text = text.lower()
    for length in range(43, 48):
        for start in range(16, 78 - length + 1):
            substring = text[start:start + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes