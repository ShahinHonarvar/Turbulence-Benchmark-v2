from itertools import permutations

def palindromes_between_indices(s):
    substring = s.lower()[:6]
    char_count = {}
    for char in substring:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    palindromes = set()
    for length in range(4, len(substring) + 1):
        for perm in permutations(char_count.keys(), length):
            left = ''.join(perm[:length // 2])
            right = ''.join(perm[length // 2:][::-1]) if length % 2 == 0 else ''.join(perm[length // 2 + 1:][::-1]) + perm[length // 2]
            possible_palindrome = left + right
            if (possible_palindrome, possible_palindrome.upper()) not in palindromes:
                palindromes.add((possible_palindrome, possible_palindrome.upper()))
    return {p[0] for p in palindromes}