import re

def palindromes_of_specific_lengths(string):
    """
    Returns a set of all palindromes with the following requirements:
    1. Only palindromes occurring in the substring from index 10 to index 59, both inclusive, should be considered.
    2. Only palindromes of lengths between 18 to 36 (both inclusive) should be considered.
    3. Each palindrome should only consist of English letters.
    4. If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    5. The function should find the palindromes in a case-insensitive manner.
    """
    pattern = '[a-zA-Z]{' + str(18) + ',' + str(36) + '}'
    substring = string[10:60]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 1, len(substring)):
            if substring[i:j].lower() == substring[i:j][::-1].lower():
                if re.match(pattern, substring[i:j]):
                    palindromes.add(substring[i:j])
    return palindromes