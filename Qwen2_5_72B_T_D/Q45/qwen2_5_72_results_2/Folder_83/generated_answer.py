from collections import Counter

def palindromes_between_indices(s):
    substring = s[2:10]
    letters = [ch.lower() for ch in substring if ch.isalpha()]
    letter_counts = Counter(letters)
    odd_count_letters = [letter for letter, count in letter_counts.items() if count % 2 != 0]
    possible = set()
    if len(odd_count_letters) <= 1:
        half_palindrome = ''.join([letter * (count // 2) for letter, count in letter_counts.items()])
        for i in range(len(half_palindrome) + 1):
            for odd_letter in odd_count_letters:
                palindrome = half_palindrome[:i] + odd_letter + half_palindrome[i:]
                if len(palindrome) >= 7:
                    possible.add(palindrome + palindrome[:len(palindrome) // 2][::-1])
    return possible