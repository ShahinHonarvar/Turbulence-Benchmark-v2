from itertools import permutations

def palindromes_between_indices(s):
    start, end = (3, 7)
    letters = s[start:end + 1].lower()
    letter_counts = {}
    for letter in letters:
        if letter.isalpha():
            letter_counts[letter] = letter_counts.get(letter, 0) + 1

    def can_form_palindrome(sub_letters):
        odd_count = sum((1 for letter, count in sub_letters.items() if count % 2 == 1))
        return odd_count <= 1

    def permutations_generator(sub_letters, prefix='', length=4):
        if length == 0:
            if can_form_palindrome({key: sub_letters.get(key, 0) for key in sub_letters}):
                yield prefix
        for letter, count in sub_letters.items():
            if count > 0:
                new_sub_letters = sub_letters.copy()
                new_sub_letters[letter] -= 1
                yield from permutations_generator(new_sub_letters, prefix=prefix + letter, length=length - 1)
    all_palindromes = set(permutations_generator(letter_counts))
    return {palindrome[:len(palindrome) // 2] + palindrome[len(palindrome) // 2:][::-1] for palindrome in all_palindromes if len(palindrome) >= 4}