from itertools import permutations, combinations

def palindromes_between_indices(s):
    letters = s[1:6].lower()
    unique_letters = set(letters)
    possible_palindromes = set()
    for r in range(6, len(unique_letters) * 2 + 1):
        for comb in combinations(unique_letters, r):
            for perm in permutations(comb):
                half = ''.join(perm[:r // 2])
                palindrome = half + half[::-1]
                if len(palindrome) >= 6:
                    possible_palindromes.add(palindrome)
    return possible_palindromes