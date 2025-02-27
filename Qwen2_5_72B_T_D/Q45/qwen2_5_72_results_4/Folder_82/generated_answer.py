from collections import Counter

def palindromes_between_indices(s):
    substring = s[1:7].lower()
    letter_counts = Counter(substring)
    available_letters = ''.join([letter * (count // 2) for letter, count in letter_counts.items()])
    unique_letters = set(substring)
    odd_count_letters = [letter for letter, count in letter_counts.items() if count % 2 != 0]
    palindromes = set()

    def generate_palindrome(half, odd_char=''):
        return half + odd_char + half[::-1]

    def backtrack(path='', remaining=available_letters):
        if len(path) == 3:
            for odd in [''] + odd_count_letters:
                palindrome = generate_palindrome(path, odd)
                palindromes.add(palindrome)
        else:
            for letter in unique_letters:
                if letter in remaining:
                    next_remaining = remaining.replace(letter, '', 1)
                    backtrack(path + letter, next_remaining)
    backtrack()
    return palindromes