from collections import Counter
from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:7]
    counter = Counter(substring.lower())
    middle = [char for char, count in counter.items() if count % 2 != 0]
    half_palindrome = ''.join([char * (count // 2) for char, count in counter.items()])
    possible_palindromes = set()
    if len(middle) <= 1 and sum(counter.values()) >= 7:
        for i in range(len(half_palindrome) + 1):
            for comb in set([''.join(p) for p in permutations(half_palindrome, i)]):
                final_palindrome = comb + (middle[0] if middle else '') + comb[::-1]
                if len(final_palindrome) >= 7:
                    possible_palindromes.add(final_palindrome)
    return possible_palindromes