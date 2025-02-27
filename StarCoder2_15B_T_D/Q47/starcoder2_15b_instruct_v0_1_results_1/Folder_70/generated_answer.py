def palindromes_of_specific_lengths(string):
    """
    Find all palindromes of specific lengths in a given string.
    Only considers palindromes in the substring from index 10 to 70, both inclusive.
    Only considers palindromes of lengths between 24 to 52, both inclusive.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, returns an empty set.
    """
    result = set()
    substring = string[10:71]
    for length in range(24, 53):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                result.add(palindrome)
    return result