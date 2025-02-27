def palindromes_between_indices(s):
    """
    Returns the set of all palindromes of the length of at least 4 such that each
    palindrome is created from any possible arrangement of the English letters in the
    given string that occur between index 1 to index 4, both inclusive.
    """
    filtered_letters = [letter for letter in s if letter.isalpha()]
    unique_letters = set(filtered_letters)
    palindromes = set()
    for letter in unique_letters:
        for permutation in itertools.permutations(unique_letters, len(letter)):
            palindrome = ''.join(permutation)
            if len(palindrome) >= 4:
                palindromes.add(palindrome)
    return palindromes