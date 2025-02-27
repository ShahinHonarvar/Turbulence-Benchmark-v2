def palindrome_of_length_n(s: str) -> set:
    """
    Given a string, returns the set of all palindromes of length 4 as substrings of the given string.
    Each palindrome must consist of only English letters and be case-insensitive.
    """

    def is_palindrome(s: str) -> bool:
        return s == s[::-1]
    palindromes = set()
    for i in range(len(s) - 3):
        substring = s[i:i + 4]
        if is_palindrome(substring) and substring.isalpha():
            palindromes.add(substring)
    return palindromes