def palindrome_of_length_at_least_n(s: str) -> set:
    """
    Finds all palindromes of length greater than or equal to 141 in a given string.
    """
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 141, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes