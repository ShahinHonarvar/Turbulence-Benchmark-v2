from itertools import permutations

def palindromes_between_indices(s):
    letters = s[:7].lower()
    unique_letters = set(letters)
    palindromes = set()
    for length in range(7, len(unique_letters) + 1):
        for p in permutations(unique_letters, length):
            half = ''.join(p[:length // 2])
            if length % 2 == 0:
                palindrome = half + half[::-1]
            else:
                palindrome = half + unique_letters[length // 2] + half[::-1]
            palindromes.add(palindrome)
    return palindromes