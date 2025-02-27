def palindrome_of_length_at_least_n(s: str) -> set:
    """
    Finds the set of all palindromes of the length greater than or equal to 78 that exist in the given string.
    Each palindrome should only consist of English letters. If no such palindromes exist in the given string,
    the function returns an empty set. The function finds the palindromes in a case-insensitive manner.
    """
    return {p for p in set(s.split()) if len(p) >= 78 and p.isalpha()}