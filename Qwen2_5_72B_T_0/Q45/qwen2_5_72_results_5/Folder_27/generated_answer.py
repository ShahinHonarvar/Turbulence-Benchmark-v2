from collections import Counter

def palindromes_between_indices(s):
    substring = s[2:9].lower()
    letter_counts = Counter(substring)
    even_letters = [letter for letter, count in letter_counts.items() if count % 2 == 0]
    odd_letters = [letter for letter, count in letter_counts.items() if count % 2 != 0]
    if len(odd_letters) > 1:
        return set()
    half_palindrome = ''.join((even_letters * (letter_counts[letter] // 2) for letter in even_letters))
    if odd_letters:
        half_palindrome += odd_letters[0]
    palindromes = set()
    if len(half_palindrome) * 2 >= 6:
        palindromes.add(half_palindrome + half_palindrome[::-1])
    return palindromes