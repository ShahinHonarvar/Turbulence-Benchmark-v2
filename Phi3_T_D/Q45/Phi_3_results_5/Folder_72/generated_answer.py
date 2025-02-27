from itertools import permutations

def palindromes_between_indices(s):
    start, end = (1, 7)
    letters = [char.lower() for char in s[start:end + 1] if char.isalpha()]
    unique_letters = set(letters)

    def is_palindrome(word):
        return word == word[::-1]
    results = set()
    for middle_letters_length in range(0, (end - start) // 2):
        for perm in permutations(unique_letters, middle_letters_length):
            left_half = ''.join(perm)
            right_half = left_half[::-1]
            middle_letter_count = len(unique_letters) - len(perm)
            if middle_letter_count % 2 == 0:
                palindrome = left_half + str(middle_letter_count // 2) + right_half
            else:
                palindrome = left_half + str(middle_letter_count // 2) + unique_letters.pop() + right_half
            if is_palindrome(palindrome):
                results.add(palindrome)
    return results