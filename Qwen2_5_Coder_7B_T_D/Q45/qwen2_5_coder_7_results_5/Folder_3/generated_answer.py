from itertools import permutations

def palindromes_between_indices(s):
    result = set()
    substring = s[7:10].lower()
    chars = list(substring)
    for length in range(3, len(chars) + 1):
        for perm in permutations(chars, length):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                result.add(palindrome)
    return result