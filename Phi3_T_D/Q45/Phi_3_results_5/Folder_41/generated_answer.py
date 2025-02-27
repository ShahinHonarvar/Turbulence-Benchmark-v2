from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:4].lower()
    unique_chars = set(substring)
    result_set = set()
    for length in range(3, len(substring) + 1):
        for perm in permutations(unique_chars, length):
            center = perm[(length - 1) // 2]
            palindrome_candidate = ''.join(perm)
            if palindrome_candidate == palindrome_candidate[::-1]:
                result_set.add(palindrome_candidate)
    return result_set