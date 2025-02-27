from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:8]
    unique_chars = ''.join(set(substring.lower()))
    all_palindromes = set()
    for perm in permutations(unique_chars, len(unique_chars)):
        candidate = ''.join(perm)
        if len(candidate) >= 3:
            for i in range(len(candidate)):
                for j in range(i + 3, len(candidate) + 1):
                    candidate_palindrome = candidate[i:j] + candidate[j - 1:i - 1:-1]
                    if len(candidate_palindrome) >= 6:
                        all_palindromes.add(candidate_palindrome)
    return all_palindromes