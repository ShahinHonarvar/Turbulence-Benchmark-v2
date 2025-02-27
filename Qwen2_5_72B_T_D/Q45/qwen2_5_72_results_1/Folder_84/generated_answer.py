from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:10].lower()
    letter_counts = Counter(substring)
    middle = [char for char, count in letter_counts.items() if count % 2 != 0]
    half_palindrome = ''.join([char * (count // 2) for char, count in letter_counts.items()])
    palindromes = set()
    if len(middle) <= 1 and len(half_palindrome) >= 1:
        for half in set.permutations(half_palindrome):
            if middle:
                candidate = half + middle[0] + half[::-1]
            else:
                candidate = half + half[::-1]
            if len(candidate) >= 3:
                palindromes.add(candidate)
    return palindromes