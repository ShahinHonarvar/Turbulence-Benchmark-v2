import itertools
from collections import Counter

def palindromes_between_indices(s):
    substring = s[3:7]
    letters_count = Counter(substring.lower())
    palindromes = set()
    for counts in itertools.permutations(letters_count.elements(), 4):
        letters = {}
        for c in counts:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1
        odd_found = False
        palindrome = []
        for letter, count in letters.items():
            if count % 2 != 0:
                if odd_found:
                    break
                odd_found = True
            for _ in range(count // 2):
                palindrome.append(letter)
        if len(palindrome) >= 2:
            first_half = ''.join(palindrome)
            second_half = first_half[::-1]
            palindromes.add(first_half + (letter if odd_found else '') + second_half)
    return palindromes