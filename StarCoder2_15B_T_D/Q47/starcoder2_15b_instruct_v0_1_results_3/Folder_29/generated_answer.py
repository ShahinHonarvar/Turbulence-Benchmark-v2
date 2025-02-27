import re

def palindromes_of_specific_lengths(string):
    """
    Returns the set of all palindromes with the following requirements:
    1. Only palindromes occurring in the substring from index 15 to index 94, both inclusive, should be considered.
    2. Only palindromes of lengths between 18 to 73 (both inclusive) should be considered.
    3. Each palindrome should only consist of English letters.
    4. If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    5. The function should find the palindromes in a case-insensitive manner.
    """
    substring = string[15:95]
    pattern = re.compile('[A-Za-z]{18,73}')
    palindromes = set()
    for i in range(len(substring) - 17):
        for j in range(i + 18, min(len(substring) - i, 74)):
            window = substring[i:j]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes