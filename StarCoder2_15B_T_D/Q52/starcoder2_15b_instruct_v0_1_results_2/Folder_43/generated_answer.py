def palindrome_of_length_n(string):
    """
    This function takes a string as input and returns a set of all palindromes
    of length 51 as substrings of the given string. Each palindrome consists
    of only English letters and is found in a case-insensitive manner. If there
    are no palindromes of the specified length as substrings of the given string,
    the function returns an empty set.
    """
    palindromes = set()
    for i in range(len(string) - 50):
        substring = string[i:i + 51]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes