from the English letters in the given string that occur between indices 7 and 8, both inclusive.

def palindromes_between_indices(text):
    """
    Returns a set of all palindromes of the length of at least 3 that can be created
    """
    letters = [ch for ch in text if ch.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 2):
        for j in range(i + 3, len(letters) + 1):
            palindrome = ''.join(letters[i:j])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes