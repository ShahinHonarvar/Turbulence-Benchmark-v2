from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:10]
    letter_counts = Counter(filter(str.isalpha, substring.lower()))
    palindrome_set = set()
    for length in range(7, 10):
        for palindrome in generate_palindromes(letter_counts, length):
            palindrome_set.add(palindrome)
    return palindrome_set

def generate_palindromes(letter_counts, length):
    letters = ''.join([letter * count for letter, count in letter_counts.items()])
    half_length = length // 2
    for half in permutations(letters, half_length):
        half = ''.join(half)
        if length % 2 == 0:
            palindrome = half + half[::-1]
        else:
            for middle in letters:
                palindrome = half + middle + half[::-1]
                yield palindrome
    return set()