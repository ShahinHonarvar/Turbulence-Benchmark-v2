def palindromes_between_indices(string):
    """
    Creates all possible palindromes of length at least 4 from the given string that occur
    between index 2 and index 9, both inclusive.
    """
    string = string.upper()
    valid_chars = [c for c in string[2:10] if c.isalpha()]
    palindromes = set()
    for i in range(len(valid_chars)):
        for j in range(i + 4, len(valid_chars) + 1):
            palindrome = ''.join(valid_chars[i:j])
            reversed_palindrome = palindrome[::-1]
            if palindrome == reversed_palindrome:
                palindromes.add(palindrome)
    return palindromes