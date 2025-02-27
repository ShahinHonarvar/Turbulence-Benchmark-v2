from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:7].lower()
    letter_counts = Counter(s)
    usable_letters = ''.join([c * (v // 2) for c, v in letter_counts.items()])

    def is_palindrome_possible():
        odd_count = sum((1 for c, v in letter_counts.items() if v % 2 != 0))
        return odd_count <= 1
    palindromes = set()
    if is_palindrome_possible():
        for p in permutations(usable_letters):
            half = ''.join(p)
            middle = ''
            for c, v in letter_counts.items():
                if v % 2 != 0:
                    middle = c
                    break
            full_palindrome = half + middle + half[::-1]
            if len(full_palindrome) >= 7:
                palindromes.add(full_palindrome)
    return palindromes