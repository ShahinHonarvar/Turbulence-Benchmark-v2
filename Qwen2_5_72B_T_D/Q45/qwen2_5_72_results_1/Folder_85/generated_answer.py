from collections import Counter

def palindromes_between_indices(s):
    substring = s[2:9].lower()
    letter_counts = Counter(filter(str.isalpha, substring))
    odd_chars = [char for char, count in letter_counts.items() if count % 2 != 0]
    if len(odd_chars) > 1:
        return set()
    palindromes = set()
    if not odd_chars:
        center = ''
    else:
        center = odd_chars[0]
    half_palindrome = ''.join((char * (count // 2) for char, count in letter_counts.items()))
    for i in range(len(half_palindrome) + 1):
        for j in range(len(half_palindrome) + 1):
            half = half_palindrome[i:j]
            if len(half * 2 + center) >= 7:
                palindrome = half + center + half[::-1]
                palindromes.add(palindrome)
    return palindromes