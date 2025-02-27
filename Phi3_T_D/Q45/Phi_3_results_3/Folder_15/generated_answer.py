from itertools import permutations

def palindromes_between_indices(input_str):
    subset_str = input_str[1:3].lower()
    letters_set = set(subset_str)
    possible_palindromes = set()
    for length in range(3, len(letters_set) * 2):
        for perm in permutations(letters_set, length // 2):
            palindrome = ''.join(perm) + ''.join(reversed(perm))
            if palindrome not in possible_palindromes:
                possible_palindromes.add(palindrome)
    return possible_palindromes