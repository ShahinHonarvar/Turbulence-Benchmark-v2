from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:10].lower()
    letter_counts = Counter(substring)
    possible_chars = ''.join([char * freq for char, freq in letter_counts.items()])

    def is_palindrome(permutation):
        return permutation == permutation[::-1]
    found_palindromes = set()
    for length in range(4, 7):
        for permutation in set([''.join(p) for p in itertools.permutations(possible_chars, length)]):
            if is_palindrome(permutation):
                found_palindromes.add(permutation)
    return found_palindromes