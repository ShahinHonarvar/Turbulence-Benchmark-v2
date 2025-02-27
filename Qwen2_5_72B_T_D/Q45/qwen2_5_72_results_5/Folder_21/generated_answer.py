from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    substr = s[1:9]
    letter_count = {}
    for char in substr:
        if char.isalpha():
            letter_count[char.lower()] = letter_count.get(char.lower(), 0) + 1
    half_palindrome = ''
    middle_char = ''
    odd_counts = sum((1 for count in letter_count.values() if count % 2 != 0))
    if odd_counts > 1:
        return set()
    for char, count in sorted(letter_count.items()):
        half_palindrome += char * (count // 2)
        if count % 2 != 0 and (not middle_char):
            middle_char = char
    all_palindromes = set()
    for perm in permutations(half_palindrome):
        possible_palindrome = ''.join(perm) + middle_char + ''.join(reversed(perm))
        if len(possible_palindrome) >= 7 and is_palindrome(possible_palindrome):
            all_palindromes.add(possible_palindrome)
    return all_palindromes