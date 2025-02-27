from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:10].lower()
    letter_counts = Counter(filter(str.isalpha, substring))
    odds = sum((count % 2 for count in letter_counts.values()))
    min_length = 6
    palindromes = set()

    def generate_palindrome(half, remaining):
        if len(half) * 2 + sum(remaining.values()) >= min_length:
            if odds <= 1:
                palindrome = half + half[::-1]
                if len(palindrome) >= min_length:
                    palindromes.add(palindrome)
            for letter, count in list(remaining.items()):
                if count > 1:
                    new_half = half + letter
                    remaining[letter] -= 2
                    generate_palindrome(new_half, remaining)
                    remaining[letter] += 2
    if odds <= 1:
        generate_palindrome('', letter_counts)
    return palindromes