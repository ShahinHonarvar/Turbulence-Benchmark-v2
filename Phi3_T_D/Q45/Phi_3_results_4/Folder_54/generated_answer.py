import itertools
from collections import Counter

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    letters = s[4:10].lower()
    counter = Counter(letters)
    unique_letters = ''.join((letter for letter in counter if counter[letter] >= 2))
    if len(unique_letters) < 2:
        return set()
    result = set()
    for i in range(2, len(unique_letters) // 2 + 1):
        for combination in itertools.combinations(unique_letters, i * 2):
            if is_palindrome(''.join(sorted(combination))):
                for center in combination:
                    if combination.count(center) > 1:
                        permutations = itertools.permutations(combination)
                        for perm in permutations:
                            palindrome_candidate = ''.join(perm)
                            if palindrome_candidate not in result and len(palindrome_candidate) >= 4:
                                result.add(palindrome_candidate)
    return result