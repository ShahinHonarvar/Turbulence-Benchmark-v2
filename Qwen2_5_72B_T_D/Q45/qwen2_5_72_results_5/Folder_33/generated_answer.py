from itertools import permutations

def palindromes_between_indices(s):
    substring = s[7:10].lower()
    possible_palindromes = set([''.join(p) for p in permutations(substring, 3)])
    valid_palindromes = set()
    for pp in possible_palindromes:
        for i in range(1, 5):
            for j in range(i + 3, 6):
                candidate = pp[i - 1:j]
                if candidate == candidate[::-1]:
                    valid_palindromes.add(candidate)
    return valid_palindromes