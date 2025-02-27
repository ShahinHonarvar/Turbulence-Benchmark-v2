from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:4].lower()
    unique_chars = set(substring)
    palindromes = set()
    for chars in permutations(unique_chars, len(unique_chars)):
        for length in range(4, len(substring) * 2 + 1):
            half = length // 2
            candidate = chars[:half]
            if length % 2 == 0:
                palindrome = candidate + candidate[::-1]
            else:
                palindrome = candidate + chars[half] + candidate[::-1]
            if len(palindrome) >= 4 and all((palindrome.count(char) <= substring.count(char) for char in set(palindrome))):
                palindromes.add(palindrome)
    return palindromes