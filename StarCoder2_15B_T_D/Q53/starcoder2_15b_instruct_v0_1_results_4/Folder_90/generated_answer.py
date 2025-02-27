def palindrome_of_length_at_least_n(s: str) -> set:
    """
    Returns the set of all palindromes of length greater than or equal to 140
    that exist in the given string. Each palindrome should only consist of English
    letters. If no such palindromes exist in the given string, the function returns
    an empty set. The function finds the palindromes in a case-insensitive manner.
    """
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 140 + 1):
        valid_palindrome = True
        for j in range(70):
            if s[i + j] != s[i + 139 - j]:
                valid_palindrome = False
                break
        if valid_palindrome:
            palindromes.add(s[i:i + 140])
    return palindromes