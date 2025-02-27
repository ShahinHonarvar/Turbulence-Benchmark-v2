from itertools import permutations

def palindromes_between_indices(s):
    string_slice = s[2:7]
    unique_chars = set(string_slice.lower())
    palindromes = set()
    for length in range(4, len(string_slice) + 1):
        if length % 2 == 0:
            cycle_length = length // 2
            for perm in permutations(unique_chars, cycle_length):
                palindrome = ''.join(perm) + ''.join(reversed(perm))
                palindromes.add(palindrome)
        else:
            cycle_length = length // 2
            for perm in permutations(unique_chars, cycle_length):
                mid_char = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')[length % 2]
                palindrome = ''.join(perm) + mid_char + ''.join(reversed(perm))
                palindromes.add(palindrome)
    return palindromes