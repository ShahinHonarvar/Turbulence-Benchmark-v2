from itertools import combinations

def palindromes_of_specific_lengths(s):
    s = s[1:300].lower()
    palindromes = set()
    for length in range(3, 11):
        substrings = [''.join(comb) for comb in combinations(s, length)]
        for substr in substrings:
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes