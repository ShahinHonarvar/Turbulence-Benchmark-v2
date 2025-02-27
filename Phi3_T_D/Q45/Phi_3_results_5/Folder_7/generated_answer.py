from itertools import permutations

def palindromes_between_indices(s):
    filtered_letters = [char.lower() for char in s[1:10] if char.isalpha()]
    letter_counts = {letter: filtered_letters.count(letter) for letter in set(filtered_letters)}

    def is_palindrome(permutation):
        return permutation == permutation[::-1]
    palindromes = set()
    for length in range(7, len(filtered_letters) + 1):
        for perm in permutations(filtered_letters, length):
            if is_palindrome(perm):
                palindromes.add(''.join(perm).lower())
    return palindromes