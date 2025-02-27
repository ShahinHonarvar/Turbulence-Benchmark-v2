from collections import Counter

def palindromes_between_indices(s):
    substring = s[1:7].lower()
    letter_counts = Counter(substring)
    middle = [char for char, count in letter_counts.items() if count % 2 != 0]
    half_palindrome = ''.join([char * (count // 2) for char, count in letter_counts.items()])
    if len(middle) <= 1 and len(half_palindrome) * 2 + len(middle) >= 7:
        permutations = set([''.join(p) for p in set(itertools.permutations(half_palindrome))])
        palindromes = set()
        for p in permutations:
            if middle:
                palindrome = p + middle[0] + p[::-1]
            else:
                palindrome = p + p[::-1]
            if len(palindrome) >= 7:
                palindromes.add(palindrome)
        return palindromes
    return set()