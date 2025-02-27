from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:10]]
    letter_counts = {}
    for letter in letters:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    def make_palindrome(length, letters):
        half_palindrome = []
        odd_char = ''
        for letter, count in letters.items():
            half_palindrome.extend([letter] * (count // 2))
            if count % 2 != 0:
                odd_char = letter
        if length % 2 == 0:
            assert odd_char == '', 'Cannot form palindrome of even length with odd letter counts'
            palindromes = set((''.join(p) for p in permutations(''.join(half_palindrome))))
        else:
            other_half = half_palindrome.copy()
            if odd_char:
                other_half.remove(odd_char)
            palindromes = set((''.join((odd + ''.join(p) + odd for p in permutations(''.join(other_half)))) for odd in (odd_char, '')))
        return {''.join(p + p[::-1]) for p in palindromes}
    length = 3
    palindromes = set()
    while length <= len(letters):
        palindromes |= make_palindrome(length, {letter: letter_counts[letter] for letter in letters} if length % 2 == 0 else {letter: letter_counts[letter] + (1 if letters.count(letter) % 2 else 0) for letter in letters})
        length += 1
    return palindromes