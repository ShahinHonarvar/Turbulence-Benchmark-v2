from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(x):
        return str(x) == str(x)[::-1]
    start_index, end_index = (7, 9)
    letters = s[start_index:end_index + 1].lower()
    palindromes_set = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                palindromes_set.add(perm_str)
    return palindromes_set