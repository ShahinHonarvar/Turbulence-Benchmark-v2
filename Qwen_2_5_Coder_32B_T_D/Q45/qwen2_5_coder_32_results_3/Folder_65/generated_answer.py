from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:7])).lower()
    counter = Counter(letters)

    def can_form_palindrome(counter):
        odd_count = sum((1 for c in counter if counter[c] % 2 != 0))
        return odd_count <= 1
    if not can_form_palindrome(counter):
        return set()
    half_length = 2
    palindromes = set()
    for perm in permutations(letters, half_length):
        half_palindrome = ''.join(perm)
        middle = min(counter, key=lambda x: counter[x] if counter[x] % 2 != 0 else float('inf'))
        full_palindrome = half_palindrome + (middle if middle in counter and counter[middle] % 2 != 0 else '') + half_palindrome[::-1]
        if len(full_palindrome) >= 5:
            palindromes.add(full_palindrome)
    return palindromes