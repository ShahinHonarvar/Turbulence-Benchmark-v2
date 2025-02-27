from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c.lower() for c in s[3:9] if c.isalpha()]
    count = Counter(letters)
    usable_letters = ''.join([c * (count[c] // 2) for c in count])
    result = set()
    for i in range(4, len(usable_letters) * 2 + 1, 2):
        for p in permutations(usable_letters, i // 2):
            half = ''.join(p)
            palindrome = half + half[::-1]
            result.add(palindrome)
    return result