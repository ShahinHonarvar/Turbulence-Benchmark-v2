from itertools import permutations

def palindromes_between_indices(s):
    letters = s[1:5].lower()
    unique_letters = set(letters)
    if len(unique_letters) < 3:
        return set()
    palindromes = set()
    for r in range(3, len(unique_letters) + 1):
        for perm in permutations(unique_letters, r):
            candidate = ''.join(perm) + ''.join(perm[::-1])
            if candidate[:len(candidate) // 2].lower() == candidate[:len(candidate) // 2][::-1].lower():
                palindromes.add(candidate)
    return palindromes