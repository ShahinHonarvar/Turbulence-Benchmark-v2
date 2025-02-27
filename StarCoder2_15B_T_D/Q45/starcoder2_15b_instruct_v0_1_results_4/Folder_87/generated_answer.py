def palindromes_between_indices(string: str) -> set:
    """
    Given a string, returns the set of all palindromes of length at least 3 that can be formed from any possible arrangement
    of the English letters in the given string that occur between indices 3 and 9, both inclusive. If no such palindromes can
    be formed, returns an empty set.
    """

    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    def case_insensitive_palindromes(s: str) -> set:
        palindromes = set()
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j + 1]
                if is_palindrome(substring):
                    palindromes.add(substring)
        return palindromes
    letters_in_range = [c for c in string if c.isalpha() and 3 <= string.index(c) <= 9]
    palindromes = case_insensitive_palindromes(''.join(letters_in_range))
    return {p for p in palindromes if len(p) >= 3}