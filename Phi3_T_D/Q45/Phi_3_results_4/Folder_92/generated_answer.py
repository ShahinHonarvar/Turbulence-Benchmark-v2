from collections import Counter
    import itertools

def palindromes_between_indices(s):
    substring = s[3:8].lower()

    def can_form_palindrome(counter):
        odd_count = sum((1 for count in counter.values() if count % 2))
        return odd_count <= 1
    letter_count = Counter(substring)
    if not can_form_palindrome(letter_count):
        return set()
    center = [k for k, v in letter_count.items() if v % 2]
    chars = ''.join((k * (v // 2) for k, v in letter_count.items()))
    palindromes = set()
    for p in itertools.permutations(chars):
        for c in center:
            if not center:
                palindromes.add(''.join(p))
            else:
                palindromes.update(''.join(p) + c + ''.join(p[::-1]))
    return {p for p in palindromes if len(p) >= 4}