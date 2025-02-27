from collections import Counter

def palindromes_between_indices(s):
    substring = s[2:10]
    counter = Counter(substring.lower())
    middle_chars = [char for char, count in counter.items() if count % 2 != 0]
    half_palindrome = ''.join([char * (count // 2) for char, count in counter.items()])
    if len(middle_chars) > 1 or len(half_palindrome) < 3:
        return set()
    palindromes = set()
    if len(middle_chars) == 1:
        middle_char = middle_chars[0]
    else:
        middle_char = ''
    for permutation in set([''.join(p) for p in permutations(half_palindrome)]):
        palindrome = permutation + middle_char + permutation[::-1]
        if len(palindrome) >= 6:
            palindromes.add(palindrome)
    return palindromes