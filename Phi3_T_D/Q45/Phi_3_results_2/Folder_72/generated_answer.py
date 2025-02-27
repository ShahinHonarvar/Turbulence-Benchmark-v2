from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:8].lower()
    letter_counts = {}
    for c in substring:
        if c.isalpha():
            letter_counts[c] = letter_counts.get(c, 0) + 1

    def can_form_palindrome(counts):
        odd_count = sum((count % 2 for count in counts.values()))
        return odd_count <= 1
    potential_palindromes = set()
    for length in range(6, len(substring) + 1):
        for perm in permutations(substring, length):
            perm_set = set(perm)
            if len(perm) - len(perm_set) >= 2 and can_form_palindrome(dict(zip(perm_set, map(perm.count, perm_set)))):
                potential_palindromes.add(''.join(perm))
    return set((p for p in potential_palindromes if p == p[::-1]))