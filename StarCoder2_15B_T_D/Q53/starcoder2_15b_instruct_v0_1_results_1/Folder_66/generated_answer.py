def palindrome_of_length_at_least_n(string):
    """
    Find all palindromes of length greater than or equal to 76 in a given string.
    """

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    for i in range(len(string) - 75):
        for j in range(i + 76, len(string) + 1):
            if is_palindrome(string[i:j]):
                palindromes.add(string[i:j])
    return palindromes