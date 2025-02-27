import itertools

def palindromes_between_indices(s):
    s = s[1:4].lower()
    letters = set(s)
    result = set()
    for length in range(4, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            for perm in itertools.permutations(combination):
                palindrome = ''.join(perm)
                if palindrome == palindrome[::-1]:
                    result.add(palindrome)
    return result