def palindrome_of_length_at_least_n(string):
    """
    Find all palindromes of length greater than or equal to 70 in a given string.
    """
    palindromes = set()
    for i in range(len(string) - 69):
        substring = string[i:i + 70]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes