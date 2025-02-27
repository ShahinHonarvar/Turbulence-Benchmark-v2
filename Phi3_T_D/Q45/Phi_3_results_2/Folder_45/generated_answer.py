from itertools import permutations

def palindromes_between_indices(s):
    possible_letters = ''.join(sorted(set(s[5:10].lower())))
    palindrome_set = set()
    for length in range(4, len(possible_letters) + 1):
        for p in permutations(possible_letters, length):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                palindrome_set.add(candidate)
    return palindrome_set