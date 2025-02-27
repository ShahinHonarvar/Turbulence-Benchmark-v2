from collections import Counter

def palindromes_between_indices(s):
    substring = s[3:7]
    letter_counts = Counter(filter(str.isalpha, substring.lower()))
    even_counts = {char: count for char, count in letter_counts.items() if count % 2 == 0}
    odd_chars = [char for char, count in letter_counts.items() if count % 2 != 0]
    if len(odd_chars) > 1:
        return set()
    half_palindrome = ''.join([char * (count // 2) for char, count in even_counts.items()])
    if odd_chars:
        half_palindrome += odd_chars[0]
    palindromes = set()
    for permutation in set((''.join(p) for p in itertools.permutations(half_palindrome))):
        if len(permutation) >= 2:
            palindrome = permutation + permutation[:-1][::-1] if odd_chars else permutation + permutation[::-1]
            palindromes.add(palindrome)
    return palindromes