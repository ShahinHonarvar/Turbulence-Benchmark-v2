from collections import Counter

def palindromes_between_indices(s):
    substring = s[2:10]
    counter = Counter(substring.lower())
    odd_chars = [char for char, count in counter.items() if count % 2 != 0]
    if len(odd_chars) > 1:
        return set()
    half_palindrome = ''.join((char * (count // 2) for char, count in counter.items()))
    palindromes = set()
    for i in range(6, 11):
        if i % 2 == 0 or (i % 2 != 0 and len(odd_chars) == 1):
            for perm in set((''.join(p) for p in permutations(half_palindrome, i // 2))):
                if i % 2 == 0:
                    palindromes.add(perm + perm[::-1])
                else:
                    palindromes.add(perm + odd_chars[0] + perm[::-1])
    return palindromes