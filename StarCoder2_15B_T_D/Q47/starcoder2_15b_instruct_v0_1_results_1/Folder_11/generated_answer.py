def palindromes_of_specific_lengths(string):
    """
    Finds palindromes in a given string that satisfy the following conditions:
    1. Only palindromes occurring in the substring from index 24 to index 97, both inclusive, should be considered.
    2. Only palindromes of lengths between 10 to 36 (both inclusive) should be considered.
    3. Each palindrome should only consist of English letters.
    4. The function should find the palindromes in a case-insensitive manner.

    Args:
        string (str): The given string.

    Returns:
        set: A set of palindromes that satisfy the conditions.
    """
    palindromes = set()
    substring = string[24:98]
    for length in range(10, 37):
        for start in range(len(substring) - length + 1):
            window = substring[start:start + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes