from collections import Counter

def palindromes_between_indices(s):
    substring = s[3:6].lower()
    counter = Counter(substring)
    palindromes = set()
    for a in counter:
        for b in counter:
            for c in counter:
                if a == c and counter[a] > 0 and (counter[b] > 0):
                    palindrome_candidate = a + b + c
                    palindromes.add(palindrome_candidate)
    return palindromes