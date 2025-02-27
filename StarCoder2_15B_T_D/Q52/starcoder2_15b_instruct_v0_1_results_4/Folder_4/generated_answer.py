def palindrome_of_length_n(string):
    """
    Finds the set of all palindromes of length 15 as substrings of the given string.
    Palindromes should only consist of English letters and should be found in a
    case-insensitive manner.
    """
    results = set()
    n = len(string)
    for i in range(n - 14):
        for j in range(i + 14, n):
            substring = string[i:j + 1]
            if len(substring) == 15 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                results.add(substring)
    return results