from itertools import permutations

def palindromes_between_indices(input_string):

    def is_palindrome(s):
        return s.lower() == s[::-1].lower()
    substring = input_string[6:10].lower()
    letters = ''.join(filter(str.isalpha, substring))
    palindrome_set = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            if is_palindrome(''.join(perm)):
                palindrome_set.add(''.join(perm))
    return palindrome_set