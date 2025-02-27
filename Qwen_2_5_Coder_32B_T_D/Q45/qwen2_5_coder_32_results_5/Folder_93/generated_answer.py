import itertools
    from collections import Counter

def palindromes_between_indices(s):
    s = s[2:8].lower()
    letters = ''.join([char for char in s if char.isalpha()])
    count = Counter(letters)
    mid, sides = ('', '')
    for char in count:
        if count[char] % 2:
            mid += char
            count[char] -= 1
        sides += char * (count[char] // 2)
    if len(mid) > 1:
        return set()
    palindromes = set()
    for side in set(itertools.permutations(sides)):
        side = ''.join(side)
        palindrome = side + mid + side[::-1]
        if len(palindrome) >= 6:
            palindromes.add(palindrome)
    return palindromes