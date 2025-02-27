import re
    from index 14 to index 90, both inclusive, should be considered. Only palindromes of

def palindromes_of_specific_lengths(string):
    """
    Write a function called 'palindromes_of_specific_lengths' that takes one argument, a string.
    The given string may consist of any character. The function should return the set of all
    palindromes with the following requirements. Only palindromes occurring in the substring
    lengths between 55 to 71 (both inclusive) should be considered. Each palindrome should
    only consist of English letters. If no such palindrome with the length specified occurs in
    the specified index range, the function should return an empty set. The function should
    find the palindromes in a case-insensitive manner.
    """
    pattern = '[a-zA-Z]{' + str(55) + ',' + str(71) + '}'
    palindromes = set()
    for i in range(14, 91):
        for j in range(i + 55, 91):
            substring = string[i:j]
            match = re.search(pattern, substring, re.IGNORECASE)
            if match:
                palindromes.add(match.group().lower())
    return palindromes