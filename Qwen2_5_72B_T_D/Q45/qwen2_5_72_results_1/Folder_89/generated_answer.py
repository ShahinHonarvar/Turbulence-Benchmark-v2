from collections import Counter

def palindromes_between_indices(s):
    substring = s[5:10].lower()
    letter_counts = Counter(substring)
    even_letters = [letter for letter, count in letter_counts.items() if count % 2 == 0 and count > 1]
    odd_letters = [letter for letter, count in letter_counts.items() if count % 2 == 1]
    if len(odd_letters) > 1:
        return set()
    half_palindrome = ''.join(even_letters)
    if odd_letters:
        half_palindrome += odd_letters[0]
    palindrome = half_palindrome + half_palindrome[:-1][::-1]
    if len(palindrome) >= 6:
        return {palindrome}
    else:
        return set()