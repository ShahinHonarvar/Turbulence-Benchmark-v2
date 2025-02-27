def palindrome_of_length_n(string):
    """
    Write a function called 'palindrome_of_length_n' that takes one argument, a string,
    and returns the set of all palindromes of the length equal to 445, where each palindrome
    is a substring of the given string. Each palindrome should only consist of English letters.
    If there is no palindrome of the specified length as a substring of the given string,
    the function should return an empty set. The function should find the palindromes in a
    case-insensitive manner.
    """
    palindromes = set()
    for i in range(len(string) - 444):
        substring = string[i:i + 445]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes