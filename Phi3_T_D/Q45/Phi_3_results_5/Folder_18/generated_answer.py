from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[1:7].lower()
    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
    filtered_set = set(filter(lambda char: char in alphabet_set, s))
    palindromes = set()
    for length in range(3, min(len(filtered_set) + 1, 7)):
        for perm in permutations(filtered_set, length):
            if is_palindrome(''.join(perm)):
                palindromes.add(''.join(perm))
    return palindromes