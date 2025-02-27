from collections import Counter

def palindromes_between_indices(s):
    substring = s[3:8]
    letter_counts = Counter(filter(str.isalpha, substring.lower()))
    odd_counts = [char for char, count in letter_counts.items() if count % 2 != 0]
    even_counts = [char for char, count in letter_counts.items() if count % 2 == 0]
    if len(odd_counts) > 1:
        return set()
    palindromes = set()
    for length in range(6, len(substring) + 1, 2):
        half_length = length // 2
        for comb in combinations_with_replacement(even_counts, half_length):
            half_palindrome = ''.join(comb)
            if all((half_palindrome.count(char) <= letter_counts[char] for char in set(half_palindrome))):
                full_palindrome = half_palindrome + half_palindrome[::-1]
                palindromes.add(full_palindrome)
    return palindromes