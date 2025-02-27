from index 10 to 59 of the given string, considering only palindromes that consist

def palindromes_of_specific_lengths(string: str) -> set:
    """
    Returns a set of palindromes of lengths between 18 and 36 in the substring
    of English letters and are found in a case-insensitive manner.
    """
    palindromes = set()
    substring = string[10:60]
    for length in range(18, 37):
        for start in range(len(substring) - length + 1):
            window = substring[start:start + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes