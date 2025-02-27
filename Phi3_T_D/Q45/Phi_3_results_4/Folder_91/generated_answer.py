from itertools import permutations

def palindromes_between_indices(input_string):
    substring = input_string[2:7].lower()
    palindromes = set()
    for i in range(3, len(substring) + 1):
        for perm in permutations(substring, i):
            potential_palindrome = ''.join(perm)
            if potential_palindrome == potential_palindrome[::-1]:
                palindromes.add(potential_palindrome)
    return palindromes