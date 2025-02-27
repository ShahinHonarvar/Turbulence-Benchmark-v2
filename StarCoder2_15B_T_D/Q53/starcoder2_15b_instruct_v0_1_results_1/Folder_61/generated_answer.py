def palindrome_of_length_at_least_n(string):
    """Finds the set of all palindromes of length greater than or equal to 5 in a given string."""
    palindromes = set()
    for i in range(len(string) - 4):
        for j in range(i + 5, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes