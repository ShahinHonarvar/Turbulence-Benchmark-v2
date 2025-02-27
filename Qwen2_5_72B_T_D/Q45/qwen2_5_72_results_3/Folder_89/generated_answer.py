from itertools import permutations

def palindromes_between_indices(s):
    substr = s[5:10].lower()
    letter_count = {}
    for char in substr:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    def can_form_palindrome(counts):
        odd_counts = sum((1 for count in counts.values() if count % 2 != 0))
        return odd_counts <= 1
    possible_palindromes = set()
    if can_form_palindrome(letter_count):
        for perm in set(permutations(substr)):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1] and len(perm_str) >= 6:
                possible_palindromes.add(perm_str)
    return possible_palindromes