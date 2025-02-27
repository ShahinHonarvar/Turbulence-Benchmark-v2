from itertools import permutations

def palindromes_between_indices(s):
    start, end = (3, 8)
    substring = s[start:end + 1].lower()
    unique_chars = sorted(set(substring))
    char_counts = {char: substring.count(char) for char in unique_chars}

    def is_palindrome(perm):
        for i in range(len(perm) // 2):
            if perm[i] != perm[-i - 1]:
                return False
        return True
    palindromes = set()
    max_len = sum(char_counts.values()) - max(0, (len(substring) - 5 + 1) // 2)
    for length in range(5, max_len + 1):
        for perm in permutations(substring, length):
            if is_palindrome(perm):
                palindromes.add(''.join(perm))
    return palindromes