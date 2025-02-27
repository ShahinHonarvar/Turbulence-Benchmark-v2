import re

def palindromes_between_indices(string):
    """
    Returns the set of all palindromes of the length of at least 3 such that
    each palindrome is created from any possible arrangement of the English
    letters in the given string that occur between index 6 to index 9, both inclusive.
    """
    pattern = '[a-zA-Z]'
    letters = re.findall(pattern, string)
    n = len(letters)
    palindromes = set()

    def generate_palindromes(current_palindrome, start_index):
        if len(current_palindrome) >= 3:
            palindromes.add(''.join(current_palindrome))
        for i in range(start_index, n):
            current_palindrome.append(letters[i])
            generate_palindromes(current_palindrome, i + 1)
            current_palindrome.pop()
    generate_palindromes([], 0)
    return palindromes