from collections import Counter
    import itertools

def palindromes_between_indices(s):
    start, end = (4, 8)
    char_counts = Counter(s[start:end].lower())

    def is_palindrome(s):
        return s == s[::-1]
    possible_strings = set((''.join(p) for p in itertools.product(s[start:end].lower(), repeat=end - start)))
    half_length = (end - start) // 2
    palindromes = {s for s in possible_strings if all((char_counts[char] >= s.count(char) for char in set(s[::2])))}
    mid_chars_count = sum((1 for char, count in char_counts.items() if count % 2 != 0))
    for s in palindromes:
        if mid_chars_count == sum((s.count(char) % 2 for char in set(s[::2]))):
            palindromes.add(s)
    palindromes = {s for s in palindromes if len(s) >= 4 and is_palindrome(s)}
    return palindromes