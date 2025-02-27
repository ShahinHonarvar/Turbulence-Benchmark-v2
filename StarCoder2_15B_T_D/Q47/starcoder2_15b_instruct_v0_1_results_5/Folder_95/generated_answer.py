def palindromes_of_specific_lengths(string):
    """
    Returns a set of all palindromes of specific lengths in a given string.
    Only palindromes occurring in the substring from index 12 to 56, both inclusive,
    are considered. Only palindromes of lengths between 20 to 21 (both inclusive)
    are considered. Each palindrome must consist of English letters. If no such
    palindrome with the length specified occurs in the specified index range,
    an empty set is returned. The function finds the palindromes in a case-insensitive manner.
    """
    sub_string = string[12:57]
    palindromes = set()
    for i in range(len(sub_string) - 20):
        for j in range(i + 20, i + 22):
            substring = sub_string[i:j]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
    return palindromes