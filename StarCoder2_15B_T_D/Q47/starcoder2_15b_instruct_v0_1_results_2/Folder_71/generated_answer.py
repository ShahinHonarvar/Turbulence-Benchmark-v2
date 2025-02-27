from index 18 to index 65, both inclusive, in the given string `s`.

def palindromes_of_specific_lengths(s: str) -> set:
    """
    Finds and returns the set of all palindromes in the substring
    Only palindromes of lengths between 23 to 36 (both inclusive) are considered.
    Each palindrome must consist of only English letters.
    The palindromes are found in a case-insensitive manner.
    If no such palindrome occurs, an empty set is returned.
    """
    palindromes = set()
    substring = s[18:66]
    for length in range(23, 37):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window.lower() == window[::-1].lower():
                if window.isalpha():
                    palindromes.add(window)
    return palindromes