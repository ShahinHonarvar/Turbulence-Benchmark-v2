from itertools import combinations, permutations

def palindromes_between_indices(text):

    def is_palindrome(s):
        return s == s[::-1]
    letters = [char.lower() for char in text[3:9]]
    letters_set = set(filter(str.isalpha, letters))
    palindromes = set()
    for number_of_letters in range(7, len(letters_set) + 1):
        for letter_group in combinations(letters_set, number_of_letters):
            for perm in permutations(letter_group, number_of_letters):
                candidate = ''.join(perm) + ''.join(perm[::-1])
                if is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes