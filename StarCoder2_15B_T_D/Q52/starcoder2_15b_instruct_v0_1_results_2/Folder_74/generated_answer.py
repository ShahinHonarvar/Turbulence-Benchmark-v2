def palindrome_of_length_n(string):
    """
    This function takes a string as an argument and returns the set of all
    palindromes of the length equal to 96, where each palindrome is a substring
    of the given string. Each palindrome should only consist of English letters.
    If there is no palindrome of the specified length as a substring of the given
    string, the function should return an empty set. The function should find the
    palindromes in a case-insensitive manner.
    """
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 96 + 1):
        substring = string[i:i + 96]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes