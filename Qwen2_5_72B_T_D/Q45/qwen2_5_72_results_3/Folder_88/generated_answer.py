from collections import Counter

def palindromes_between_indices(s):
    substring = s[3:8].lower()
    letter_counts = Counter(substring)
    available_letters = ''.join([char * freq for char, freq in letter_counts.items()])
    palindromes = set()

    def generate_palindrome(half, length, available_letters):
        if len(half) == length // 2:
            if length % 2 == 0:
                palindrome = half + half[::-1]
            else:
                for middle in available_letters:
                    palindrome = half + middle + half[::-1]
                    palindromes.add(palindrome)
            return
        for i, letter in enumerate(available_letters):
            if i > 0 and letter == available_letters[i - 1]:
                continue
            if letter_counts[letter] > 1:
                letter_counts[letter] -= 2
                generate_palindrome(half + letter, length, available_letters)
                letter_counts[letter] += 2
    for length in range(6, 14):
        if length <= 2 * sum((count // 2 for count in letter_counts.values())):
            generate_palindrome('', length, available_letters)
    return palindromes