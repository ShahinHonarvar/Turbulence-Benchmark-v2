from collections import Counter
    import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:6])).lower()
    counts = Counter(letters)
    half_length = sum((count // 2 for count in counts.values()))
    if half_length < 1:
        return set()
    mid = [letter for letter, count in counts.items() if count % 2]
    result = set()
    for half in itertools.combinations_with_replacement(sorted(counts), half_length):
        if sum((half.count(x) for x in set(half))) == half_length:
            half_palindrome = ''.join(half)
            for m in mid:
                result.add(half_palindrome + m + half_palindrome[::-1])
            if not mid:
                result.add(half_palindrome + half_palindrome[::-1])
    return result