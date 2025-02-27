def palindrome_of_length_at_least_n(string):
    """
    Returns the set of all palindromes of length greater than or equal to 78 that exist in the given string.
    Each palindrome should only consist of English letters. If no such palindromes exist in the given string,
    the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
    """
    palindromes = set()
    n = 78
    string = string.lower()
    for i in range(len(string) - n + 1):
        for j in range(i + n - 1, len(string)):
            substring = string[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes