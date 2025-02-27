import re

def palindromes_of_specific_lengths(string):
    """
    Finds all palindromes of specific lengths in a given string. Only palindromes
    occurring in the substring from index 10 to 75, both inclusive, are considered.
    Only palindromes of lengths between 10 to 20 (both inclusive) are considered.
    Each palindrome should only consist of English letters. The function should
    return an empty set if no such palindrome with the length specified occurs
    in the specified index range. The function finds the palindromes in a
    case-insensitive manner.
    """
    palindromes = set()
    for length in range(10, 21):
        for i in range(10, 76 - length + 1):
            substring = string[i:i + length]
            reversed_substring = substring[::-1]
            if re.match('^[a-zA-Z]+$', substring) and substring.lower() == reversed_substring.lower():
                palindromes.add(substring)
    return palindromes