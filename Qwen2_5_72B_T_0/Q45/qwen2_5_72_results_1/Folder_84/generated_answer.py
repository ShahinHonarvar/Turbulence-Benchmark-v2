from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:10].lower()
    letter_counts = Counter(substring)
    odd_counts = [char for char, count in letter_counts.items() if count % 2 != 0]
    if len(odd_counts) > 1:
        return set()
    palindromes = set()

    def generate_palindrome(half, full):
        if not any(letter_counts.values()):
            if len(full) >= 3:
                palindromes.add(full)
            return
        for char in letter_counts.copy():
            if letter_counts[char] > 1:
                letter_counts[char] -= 2
                generate_palindrome(half + char, char + full + char)
                letter_counts[char] += 2
    if len(odd_counts) == 1:
        odd_char = odd_counts[0]
        letter_counts[odd_char] -= 1
        generate_palindrome('', odd_char)
    else:
        generate_palindrome('', '')
    return palindromes