def palindromes_of_specific_lengths(text):
    """
    Returns the set of all palindromes with the following requirements:
    - Only palindromes occurring in the substring from index 15 to index 95, both inclusive, should be considered.
    - Only palindromes of lengths between 20 to 66 (both inclusive) should be considered.
    - Each palindrome should only consist of English letters.
    - If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    - The function should find the palindromes in a case-insensitive manner.
    """
    palindromes = set()
    for length in range(20, 67):
        for start in range(15, 96 - length + 1):
            substring = text[start:start + length]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes