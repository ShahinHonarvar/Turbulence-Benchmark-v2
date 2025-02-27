def palindrome_of_length_n(s: str) -> set:
    """
    Find the set of all palindromes of length n in the given string s.
    """
    n = 27
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes

def is_palindrome(s: str) -> bool:
    """
    Check whether a string is a palindrome.
    """
    return s.lower() == s.lower()[::-1]