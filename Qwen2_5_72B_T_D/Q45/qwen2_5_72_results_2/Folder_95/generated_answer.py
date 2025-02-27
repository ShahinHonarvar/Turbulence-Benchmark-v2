from collections import Counter

def palindromes_between_indices(s):
    substring = s[7:9].lower()
    letter_counts = Counter(substring)
    palindromes = set()

    def generate_palindromes(available, length, prefix):
        if length == 0:
            palindromes.add(prefix + prefix[::-1])
            return
        for letter, count in available.items():
            if count >= 2:
                new_available = available.copy()
                new_available[letter] -= 2
                generate_palindromes(new_available, length - 2, prefix + letter)
    for length in range(3, 9, 2):
        generate_palindromes(letter_counts, length, '')
    return palindromes