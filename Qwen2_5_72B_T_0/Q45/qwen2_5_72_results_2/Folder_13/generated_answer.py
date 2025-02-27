from collections import Counter

def palindromes_between_indices(s):
    substring = s[3:10].lower()
    letter_counts = Counter(substring)
    even_counts = {char: count for char, count in letter_counts.items() if count % 2 == 0}
    odd_counts = {char: count for char, count in letter_counts.items() if count % 2 != 0}
    if sum(odd_counts.values()) > 1:
        return set()
    palindromes = set()
    if odd_counts:
        middle_char = next(iter(odd_counts))
        odd_counts[middle_char] -= 1
        if odd_counts[middle_char] == 0:
            del odd_counts[middle_char]
    else:
        middle_char = ''

    def generate_palindromes(half, remaining):
        if not remaining:
            palindromes.add(half + middle_char + half[::-1])
            return
        for char, count in remaining.items():
            if count >= 2:
                new_remaining = remaining.copy()
                new_remaining[char] -= 2
                if new_remaining[char] == 0:
                    del new_remaining[char]
                generate_palindromes(half + char, new_remaining)
    generate_palindromes('', even_counts)
    return {p for p in palindromes if len(p) >= 5}