from collections import Counter

def palindromes_between_indices(s):
    substring = s[6:10].lower()
    letter_counts = Counter(substring)
    odd_counts = [char for char, count in letter_counts.items() if count % 2 != 0]
    if len(odd_counts) > 1:
        return set()
    palindromes = set()

    def generate_palindromes(half, full_length):
        if len(half) * 2 == full_length:
            if len(odd_counts) == 1:
                half += odd_counts[0]
            palindromes.add(half + half[::-1])
        else:
            for char in letter_counts:
                if letter_counts[char] > 1:
                    letter_counts[char] -= 2
                    generate_palindromes(half + char, full_length)
                    letter_counts[char] += 2
    for length in range(3, 11, 2):
        if length <= len(substring):
            generate_palindromes('', length)
    return palindromes