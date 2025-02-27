from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:7].lower()
    found_palindromes = set()
    for permutation in permutations(substring):
        candidate = ''.join(permutation)
        if candidate == candidate[::-1]:
            for length in range(4, 8):
                if len(candidate) <= length:
                    candidate_palindrome = candidate * (length // len(candidate))
                    if length % 2 == 0:
                        candidate_palindrome = candidate_palindrome[:length // 2] + candidate_palindrome[length // 2 - 1::-1]
                    else:
                        candidate_palindrome = candidate_palindrome[:length // 2] + candidate_palindrome[length // 2] + candidate_palindrome[length // 2 - 1::-1]
                    if candidate_palindrome not in found_palindromes:
                        found_palindromes.add(candidate_palindrome)
    return found_palindromes