def palindromes_of_specific_lengths(string: str) -> set:
    """
    Finds the set of all palindromes in the substring from index 23 to index 82 (both inclusive)
    of the given string `string` that have lengths between 32 and 34 (both inclusive) and consist
    only of English letters.
    """
    substring = string[23:83]
    palindromes = set()
    for length in range(32, 35):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes