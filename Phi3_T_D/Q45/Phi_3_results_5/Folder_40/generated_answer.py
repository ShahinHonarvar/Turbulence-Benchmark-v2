from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    english_letters_in_range = ''.join(sorted(s[4:10].lower()))
    palindromes = set()
    for length in range(7, len(english_letters_in_range) + 1):
        for perm in permutations(english_letters_in_range, length):
            if is_palindrome(''.join(perm)):
                palindromes.add(''.join(perm))
    return palindromes