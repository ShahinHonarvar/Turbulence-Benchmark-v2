from itertools import permutations

def palindromes_between_indices(input_string):
    substring = input_string[1:8].lower()
    unique_letters = set(substring)
    palindromes = set()
    for r in range(3, len(unique_letters) + 1):
        for perm in permutations(unique_letters, r):
            middle = None
            if r % 2 == 1:
                middle = perm[r // 2]
                perm = perm[:r // 2] + perm[r // 2 + 1:]
            half_palindrome = ''.join(perm)
            full_palindrome = half_palindrome + (middle if middle else '') + half_palindrome[::-1]
            palindromes.add(full_palindrome)
    return palindromes