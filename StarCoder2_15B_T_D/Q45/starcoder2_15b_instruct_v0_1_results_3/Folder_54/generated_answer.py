def palindromes_between_indices(string: str) -> set:
    """
    Returns the set of all palindromes of the length of at least 4 such that each palindrome
    is created from any possible arrangement of the English letters in the given string that
    occur between index 4 to index 9, both inclusive. If no such palindromes of the specified
    length can be created from the English letters of the given string that occur in the
    specified range, the function should return an empty set. The function should form each
    palindrome in a case-insensitive manner.
    """
    filtered_chars = [char for char in string if char.isalpha()]
    palindromes = set()
    for i in range(4, len(filtered_chars) - 3):
        for j in range(i + 1, len(filtered_chars) - 2):
            for k in range(j + 1, len(filtered_chars) - 1):
                for l in range(k + 1, len(filtered_chars)):
                    palindrome = filtered_chars[i] + filtered_chars[j] + filtered_chars[k] + filtered_chars[l]
                    if palindrome == palindrome[::-1]:
                        palindromes.add(palindrome)
    return palindromes