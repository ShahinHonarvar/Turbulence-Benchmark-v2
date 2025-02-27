def palindrome_of_length_n(string):
    """
    Returns the set of all palindromes of length 43 as substrings of the given string.
    Each palindrome should only consist of English letters.
    If there is no palindrome of the specified length as a substring, returns an empty set.
    """
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 42):
        substring = string[i:i + 43]
        if substring == substring[::-1]:
            if all((ch.isalpha() for ch in substring)):
                palindromes.add(substring)
    return palindromes