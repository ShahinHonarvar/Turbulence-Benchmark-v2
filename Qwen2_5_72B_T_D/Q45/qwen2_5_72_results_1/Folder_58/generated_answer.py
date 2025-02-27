from collections import Counter

def palindromes_between_indices(s):
    substring = s[0:7]
    counter = Counter(filter(str.isalpha, substring.lower()))
    odd_counts = sum((1 for count in counter.values() if count % 2 != 0))
    possible_palindromes = set()
    if odd_counts <= 1:
        half_palindrome = ''.join((char * (count // 2) for char, count in counter.items()))
        permutations = set([''.join(p) for p in itertools.permutations(half_palindrome)])
        for perm in permutations:
            if len(perm) * 2 + (odd_counts == 1) >= 6:
                middle = ''.join((char for char, count in counter.items() if count % 2 != 0))
                possible_palindromes.add(perm + middle + perm[::-1])
    return possible_palindromes