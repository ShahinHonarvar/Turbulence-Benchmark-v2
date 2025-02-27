from collections import Counter
    import string
    import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(lambda x: x in string.ascii_letters, s[:9])).lower()
    letter_count = Counter(letters)
    palindromes = set()

    def can_form_palindrome(counter):
        odd_count = sum((1 for count in counter.values() if count % 2 != 0))
        return odd_count <= 1
    if can_form_palindrome(letter_count):
        half_length = 7 // 2
        chars = []
        middle_char = ''
        for char, count in letter_count.items():
            chars.extend(char * (count // 2))
            if count % 2 != 0:
                middle_char = char
        for half in itertools.permutations(chars, half_length):
            half = ''.join(half)
            palindrome = half + middle_char + half[::-1]
            palindromes.add(palindrome)
    return palindromes