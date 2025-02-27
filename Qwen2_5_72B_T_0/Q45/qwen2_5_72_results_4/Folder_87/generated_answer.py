from collections import Counter

def palindromes_between_indices(s):
    substring = s[3:10].lower()
    letter_counts = Counter(substring)
    odd_counts = [char for char, count in letter_counts.items() if count % 2 != 0]
    if len(odd_counts) > 1:
        return set()
    palindromes = set()

    def generate_palindrome(half, full_length):
        if len(half) * 2 == full_length:
            palindromes.add(half + half[::-1])
        elif len(half) * 2 + 1 == full_length:
            for odd in odd_counts:
                palindromes.add(half + odd + half[::-1])
        for char in letter_counts:
            if letter_counts[char] > 1:
                letter_counts[char] -= 2
                generate_palindrome(half + char, full_length)
                letter_counts[char] += 2
    for length in range(3, 10):
        if length % 2 == 0 or len(odd_counts) == 1:
            generate_palindrome('', length)
    return palindromes