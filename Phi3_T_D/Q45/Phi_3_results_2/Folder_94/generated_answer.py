from itertools import permutations

def palindromes_between_indices(s):
    start = 3
    end = 5
    mid = (start + end) // 2
    s_slice = s[start:end + 1].lower()
    unique_chars = set(s_slice)
    palindromes = set()
    for length in range(3, len(unique_chars) + 1):
        for char_permutation in permutations(unique_chars, length):
            palindrome_center = ''.join(char_permutation)[:mid]
            if palindrome_center == palindrome_center[::-1]:
                palindrome = palindrome_center.upper().center(end - start + 1, ' ')[1:-1]
                palindromes.add(palindrome)
    return palindromes