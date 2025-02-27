import re

def palindromes_of_specific_lengths(string):
    """
    Returns the set of all palindromes with the following requirements:
    1. Only palindromes occurring in the substring from index 1 to index 8, both inclusive, should be considered.
    2. Only palindromes of lengths between 3 to 4 (both inclusive) should be considered.
    3. Each palindrome should only consist of English letters.
    4. If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    5. The function should find the palindromes in a case-insensitive manner.
    """
    substring = string[1:9]
    pattern = '[a-zA-Z]{' + str(3) + ',' + str(4) + '}'
    regex = re.compile(pattern, re.IGNORECASE)
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 3, min(i + 5, len(substring) + 1)):
            if substring[i:j] == substring[i:j][::-1]:
                match = regex.search(substring[i:j])
                if match:
                    palindromes.add(match.group().lower())
    return palindromes