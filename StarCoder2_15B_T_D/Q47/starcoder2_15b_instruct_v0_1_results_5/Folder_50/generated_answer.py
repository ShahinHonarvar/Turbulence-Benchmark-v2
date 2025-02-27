def palindromes_of_specific_lengths(string):
    """
    Returns the set of all palindromes with the following requirements:
    1. Only palindromes occurring in the substring from index 36 to index 92, both inclusive, should be considered.
    2. Only palindromes of lengths between 10 to 35 (both inclusive) should be considered.
    3. Each palindrome should only consist of English letters.
    4. If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    5. The function should find the palindromes in a case-insensitive manner.
    """

    def is_palindrome(s):
        return s == s[::-1]

    def is_english_letter(c):
        return c.isalpha()
    palindromes = set()
    substring = string[36:93]
    for length in range(10, 36):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate) and all((is_english_letter(c) for c in candidate)):
                palindromes.add(candidate)
    return palindromes