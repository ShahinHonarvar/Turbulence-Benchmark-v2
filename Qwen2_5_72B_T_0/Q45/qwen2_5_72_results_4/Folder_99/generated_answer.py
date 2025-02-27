from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:9].lower()
    letter_counts = Counter(substring)
    odd_counts = [char for char, count in letter_counts.items() if count % 2 != 0]
    if len(odd_counts) > 1:
        return set()
    palindromes = set()

    def generate_palindromes(current, remaining):
        if not remaining:
            if len(current) >= 3:
                palindromes.add(current)
            return
        for char in remaining:
            if remaining[char] > 1:
                next_remaining = remaining.copy()
                next_remaining[char] -= 2
                if next_remaining[char] == 0:
                    del next_remaining[char]
                generate_palindromes(char + current + char, next_remaining)
    if len(odd_counts) == 1:
        center = odd_counts[0]
        letter_counts[center] -= 1
        if letter_counts[center] == 0:
            del letter_counts[center]
        generate_palindromes(center, letter_counts)
    else:
        generate_palindromes('', letter_counts)
    return palindromes