from collections import Counter

def palindromes_between_indices(s):
    substring = s[1:5].lower()
    letters_count = Counter(substring)
    palindromes = set()
    for first in letters_count:
        for second in letters_count:
            if letters_count[first] >= 2 and letters_count[second] >= 2:
                if first == second and letters_count[first] >= 3:
                    palindromes.add(first * 3)
                elif first != second:
                    palindromes.add(first + second + first)
    return palindromes