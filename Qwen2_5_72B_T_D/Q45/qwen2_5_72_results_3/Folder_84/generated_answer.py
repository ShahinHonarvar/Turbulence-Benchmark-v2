from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:10].lower()
    counter = Counter(substring)
    middle_chars = [char for char, count in counter.items() if count % 2 != 0]
    half_palindrome = ''.join([char * (count // 2) for char, count in counter.items()])
    results = set()
    if len(middle_chars) <= 1:
        _generate_palindromes(half_palindrome, middle_chars, results)
    return results

def _generate_palindromes(half, middle, results):
    if len(middle) == 1:
        results.add(half + middle[0] + half[::-1])
    elif len(half) >= 1:
        results.add(half + half[::-1])
    for i in range(len(half)):
        new_half = half[:i] + half[i + 1:]
        new_middle = middle + half[i]
        _generate_palindromes(new_half, new_middle, results)