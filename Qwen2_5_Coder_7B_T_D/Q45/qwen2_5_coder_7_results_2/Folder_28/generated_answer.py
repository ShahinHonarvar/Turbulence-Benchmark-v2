from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]

    def generate_permutations(s, length):
        return set((''.join(p) for p in permutations(s, length)))
    letters = s[1:6]
    unique_letters = set(letters.lower())
    max_length = min(len(unique_letters), 4)
    palindromes = set()
    for length in range(4, max_length + 1):
        for perm in generate_permutations(letters, length):
            if is_palindrome(perm):
                palindromes.add(perm)
    return palindromes