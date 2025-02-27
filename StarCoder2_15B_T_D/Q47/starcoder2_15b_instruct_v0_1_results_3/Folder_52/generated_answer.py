def palindromes_of_specific_lengths(text):
    """Returns the set of all palindromes in the substring from index 44 to 99,
    each consisting of only English letters, and with lengths between 13 and 42,
    inclusive. Only palindromes of such lengths are considered."""
    palindromes = set()
    text = text[44:100]
    for length in range(13, 43):
        for i in range(len(text) - length + 1):
            substring = text[i:i + length]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes