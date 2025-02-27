import re

def palindromes_of_specific_lengths(string):
    """
    Returns the set of all palindromes with the following requirements:
    1. Only palindromes occurring in the substring from index 41 to index 89, both inclusive, should be considered.
    2. Only palindromes of lengths between 23 to 38 (both inclusive) should be considered.
    3. Each palindrome should only consist of English letters.
    4. If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    5. The function should find the palindromes in a case-insensitive manner.
    """
    sub_string = string[41:90]
    regex = re.compile('[a-zA-Z]{23,38}')
    palindromes = set()
    for i in range(len(sub_string)):
        for j in range(i + 1, len(sub_string) + 1):
            palindrome = sub_string[i:j]
            if regex.match(palindrome) and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes