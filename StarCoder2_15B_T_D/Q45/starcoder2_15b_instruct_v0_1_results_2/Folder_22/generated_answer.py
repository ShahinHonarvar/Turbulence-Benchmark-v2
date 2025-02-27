from the English letters in the specified range [5, 6] (inclusive).

def palindromes_between_indices(s: str) -> set:
    """
    Finds all palindromes of length at least 3 in the given string `s` that are created
    """
    palindromes = set()
    letters = [c for c in s if c.isalpha()]
    for i in range(len(letters) - 2):
        for j in range(i + 2, len(letters)):
            palindrome = ''.join(letters[i:j + 1])
            if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes