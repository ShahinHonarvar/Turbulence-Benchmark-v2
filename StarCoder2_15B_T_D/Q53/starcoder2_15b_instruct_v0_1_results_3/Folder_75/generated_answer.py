def palindrome_of_length_at_least_n(s):
    """
    Returns the set of all palindromes of the length greater than or equal to 40
    that exist in the given string. Each palindrome should only consist of English
    letters. If no such palindromes exist in the given string, the function should
    return an empty set. The function should find the palindromes in a case-insensitive
    manner.
    """
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 40, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes