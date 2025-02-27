from itertools import product

def palindromes_of_specific_lengths(s):

    def is_palindrome_permutation(sub):
        letters = [c.lower() for c in sub if c.isalpha()]
        letter_counts = {letter: letters.count(letter) for letter in set(letters)}
        odd_count = sum((1 for count in letter_counts.values() if count % 2 != 0))
        return odd_count <= 1
    sub = s[36:93]
    palindromes = set()
    for length in range(10, 36):
        for indices in product(range(93 - length + 1), repeat=length):
            substr = ''.join((sub[i] for i in indices))
            if is_palindrome_permutation(substr):
                palindromes.add(substr)
    return palindromes