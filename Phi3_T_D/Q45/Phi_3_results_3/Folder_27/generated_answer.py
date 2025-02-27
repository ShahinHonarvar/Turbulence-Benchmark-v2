from itertools import permutations

def palindromes_between_indices(s):
    start_index = 2
    end_index = 8
    selected_chars = s[start_index:end_index + 1].lower()
    palindrome_set = set()
    if len(selected_chars) < 6:
        return palindrome_set
    for perm in set(permutations(selected_chars, 6)):
        if perm == perm[::-1]:
            palindrome_set.add(''.join(perm))
    return palindrome_set