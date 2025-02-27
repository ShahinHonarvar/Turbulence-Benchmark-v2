from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[2:8]

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    char_set = set([c for c in sub_str.lower() if c.isalpha()])
    palindrome_set = set()
    for length in range(3, len(char_set) + 1):
        for perm in permutations(char_set, length):
            if is_palindrome(''.join(perm)):
                palindrome_set.add(''.join(perm))
    return palindrome_set