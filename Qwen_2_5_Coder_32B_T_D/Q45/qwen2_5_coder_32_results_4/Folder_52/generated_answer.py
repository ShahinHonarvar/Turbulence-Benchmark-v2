from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):
    s = s[:8].lower()
    letters = [c for c in s if c.isalpha()]
    letter_count = Counter(letters)
    used_letters = {k: v // 2 * 2 for k, v in letter_count.items() if v >= 2}
    mid_letter = [k for k, v in letter_count.items() if v % 2 == 1]
    half_palindromes = set()
    for r in range(1, len(used_letters) // 2 + 1):
        for p in permutations(used_letters, r):
            half_palindrome = ''.join(p)
            half_palindromes.add(half_palindrome)
    palindromes = set()
    for hp in half_palindromes:
        full_palindrome = hp + (mid_letter[0] if mid_letter else '') + hp[::-1]
        if len(full_palindrome) >= 6:
            palindromes.add(full_palindrome)
    return palindromes