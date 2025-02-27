from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:5] if c.isalpha()]
    palindromes = set()
    length = len(letters)
    if length < 3:
        return palindromes
    count = Counter(letters)
    mid = ''
    sides = []
    for char, freq in count.items():
        if freq % 2 == 1:
            if mid == '':
                mid = char
            else:
                return palindromes
        sides.extend(char * (freq // 2))
    for side in set(permutations(sides)):
        palindrome = ''.join(side) + mid + ''.join(reversed(side))
        palindromes.add(palindrome)
    return palindromes