from itertools import permutations

def palindromes_between_indices(text):

    def is_palindrome(s):
        return s == s[::-1]
    letters = set(text[1:5].lower())
    palindromes = set()
    for r in range(3, 5):
        for perm in permutations(letters, r):
            possible_palindrome = ''.join(perm) + ''.join(perm[::-1])
            if is_palindrome(possible_palindrome):
                palindromes.add(possible_palindrome)
    return palindromes