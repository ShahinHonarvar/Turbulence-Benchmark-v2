from itertools import permutations

def palindromes_between_indices(s):
    required_letters = s[6:10]
    unique_chars = sorted(set(required_letters.lower()))
    palindromes = set()
    for i in range(len(unique_chars)):
        for j in range(i + 3, len(unique_chars) + 1):
            for perm in permutations(unique_chars[i:j]):
                palindrome_candidate = (''.join(perm) + ''.join(reversed(perm)))[3:]
                if palindrome_candidate == palindrome_candidate[::-1]:
                    palindromes.add(palindrome_candidate)
    return palindromes