def palindrome_of_length_at_least_n(string: str) -> set:
    """
    Finds all palindromes of length at least 38 in a given string.
    """
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 37):
        for j in range(i + 38, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes