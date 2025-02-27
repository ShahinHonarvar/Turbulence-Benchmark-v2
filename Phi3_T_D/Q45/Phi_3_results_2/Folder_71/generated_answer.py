from itertools import permutations

def palindromes_between_indices(input_string):
    substring = input_string[1:4].lower()
    unique_chars = set(substring)
    palindromes = set()
    for perm in permutations(unique_chars):
        candidate_palindrome = ''.join(perm)
        if candidate_palindrome == candidate_palindrome[::-1] and len(candidate_palindrome) >= 4:
            palindromes.add(candidate_palindrome)
    return palindromes