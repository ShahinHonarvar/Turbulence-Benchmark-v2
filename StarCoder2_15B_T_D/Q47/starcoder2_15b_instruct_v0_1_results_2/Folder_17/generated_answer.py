import re

def palindromes_of_specific_lengths(string):
    """
    Returns the set of all palindromes with the following requirements:
    - Only palindromes occurring in the substring from index 22 to index 95, both inclusive, should be considered.
    - Only palindromes of lengths between 52 to 55 (both inclusive) should be considered.
    - Each palindrome should only consist of English letters.
    - If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    - The function should find the palindromes in a case-insensitive manner.
    """
    substring = string[22:96]
    pattern = re.compile('[a-zA-Z]{52,55}')
    palindromes = set()
    for i in range(len(substring) - 55):
        match = pattern.search(substring[i:])
        if match:
            palindrome = match.group()
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes