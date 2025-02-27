def palindromes_of_specific_lengths(string: str) -> set:
    """
    Returns the set of all palindromes that satisfy the given requirements.
    Only palindromes occurring in the substring from index 11 to index 97, both inclusive,
    should be considered. Only palindromes of lengths between 29 to 62 (both inclusive)
    should be considered. Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range,
    the function should return an empty set. The function should find the palindromes in a
    case-insensitive manner.
    """
    palindromes = set()
    substring = string[11:98]
    for length in range(29, 63):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                if all((ch.isalpha() for ch in window)):
                    palindromes.add(window)
    return palindromes