def palindromes_of_specific_lengths(string):
    """
    Returns a set of all palindromes that occur in the substring from index 23 to 77, both inclusive,
    with lengths between 13 and 40 (both inclusive), consisting only of English letters, in a case-insensitive manner.
    """

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    substring = string[23:78]
    for length in range(13, 41):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if is_palindrome(window) and window.isalpha():
                palindromes.add(window)
    return palindromes