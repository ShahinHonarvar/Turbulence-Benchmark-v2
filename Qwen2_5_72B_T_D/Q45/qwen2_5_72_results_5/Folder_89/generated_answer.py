from collections import Counter

def palindromes_between_indices(s):
    substring = s[5:10]
    letter_counts = Counter(filter(str.isalpha, substring.lower()))
    middle = ''
    palindrome_parts = {''}
    for letter, count in letter_counts.items():
        if count % 2 and (not middle):
            middle = letter
        palindrome_parts = {part + letter * (count // 2) for part in palindrome_parts}
    all_palindromes = {part + middle + part[::-1] for part in palindrome_parts}
    return {palindrome for palindrome in all_palindromes if len(palindrome) >= 6}