from collections import Counter

def palindromes_between_indices(s):
    substring = s[5:10].lower()
    letter_counts = Counter(substring)
    odd_counts = [char for char, count in letter_counts.items() if count % 2 != 0]
    if len(odd_counts) > 1:
        return set()
    else:
        half_palindrome = ''.join([char * (count // 2) for char, count in letter_counts.items()])
        if odd_counts:
            middle_char = odd_counts[0]
        else:
            middle_char = ''
        full_palindrome = half_palindrome + middle_char + half_palindrome[::-1]
        if len(full_palindrome) < 5:
            return set()
        else:
            return {full_palindrome}