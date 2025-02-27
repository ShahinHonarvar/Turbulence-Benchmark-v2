from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:10].lower()
    letter_counts = Counter((char for char in substring if char.isalpha()))
    half_palindrome = ''
    center = ''
    for letter, count in letter_counts.items():
        half_palindrome += letter * (count // 2)
        if count % 2 != 0 and center == '':
            center = letter
    palindromes = set()
    for length in range(5, 11):
        if length % 2 == 0:
            possible_palindrome = half_palindrome[:length // 2] + half_palindrome[:length // 2][::-1]
        else:
            possible_palindrome = half_palindrome[:length // 2] + center + half_palindrome[:length // 2][::-1]
        if len(possible_palindrome) == length:
            palindromes.add(possible_palindrome)
    return palindromes