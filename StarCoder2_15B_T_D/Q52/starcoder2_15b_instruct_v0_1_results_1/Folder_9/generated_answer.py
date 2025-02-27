def palindrome_of_length_n(string: str) -> set:
    """
    Returns the set of all palindromes of length 72 as substrings of the given string,
    where each palindrome only consists of English letters and is case-insensitive.
    """
    if len(string) < 72:
        return set()
    result = set()
    for i in range(len(string) - 72 + 1):
        substring = string[i:i + 72]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result