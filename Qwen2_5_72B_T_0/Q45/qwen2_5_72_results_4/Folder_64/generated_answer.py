from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:10].lower()
    letter_counts = Counter(substring)
    even_counts = {char: count for char, count in letter_counts.items() if count % 2 == 0}
    odd_counts = {char: count for char, count in letter_counts.items() if count % 2 != 0}
    if len(odd_counts) > 1:
        return set()
    palindromes = set()
    if len(odd_counts) == 1:
        middle_char = ''.join(odd_counts.keys())
    else:
        middle_char = ''
    for length in range(5, 11):
        half_length = length // 2
        for combination in combinations_with_replacement(even_counts.keys(), half_length):
            counter = Counter(combination)
            for char in counter:
                if counter[char] > even_counts[char] // 2:
                    break
            else:
                half_palindrome = ''.join(combination)
                palindrome = half_palindrome + middle_char + half_palindrome[::-1]
                palindromes.add(palindrome)
    return palindromes