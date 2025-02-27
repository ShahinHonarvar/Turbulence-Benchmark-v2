def palindrome_of_length_at_least_n(s: str, n: int=36) -> set:
    """
    Finds all palindromes of length greater than or equal to n in a given string.
    """
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result