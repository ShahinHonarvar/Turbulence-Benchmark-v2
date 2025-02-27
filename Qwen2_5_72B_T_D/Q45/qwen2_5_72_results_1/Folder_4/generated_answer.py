from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:10]
    letters = ''.join(filter(str.isalpha, substring.lower()))
    palindromes = set()
    for length in range(7, len(letters) + 1):
        for perm in permutations(letters, length):
            if perm == perm[::-1]:
                palindrome = ''.join(perm)
                if len(palindrome) >= 7:
                    palindromes.add(palindrome)
    return palindromes