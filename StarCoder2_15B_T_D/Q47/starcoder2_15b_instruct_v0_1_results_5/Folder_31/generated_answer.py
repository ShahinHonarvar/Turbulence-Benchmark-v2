def palindromes_of_specific_lengths(s: str) -> set:
    """
    Returns the set of all palindromes of lengths between 37 and 60 (both inclusive)
    that occur within the substring from index 11 to index 83 (both inclusive) of the
    given string `s` in a case-insensitive manner.
    """
    start_index, end_index = (11, 83)
    min_length, max_length = (37, 60)
    palindromes = set()
    for i in range(start_index, end_index - min_length + 1):
        for length in range(min_length, max_length + 1):
            substring = s[i:i + length].lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes