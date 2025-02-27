from collections import Counter

def palindromes_between_indices(s):
    substring = s[6:10].lower()
    letter_counts = Counter(substring)
    odd_chars = [char for char, count in letter_counts.items() if count % 2 != 0]
    if len(odd_chars) > 1:
        return set()
    half_palindrome = ''.join((char * (count // 2) for char, count in letter_counts.items()))
    palindromes = set()
    if len(half_palindrome) * 2 + len(odd_chars) >= 5:
        if odd_chars:
            for i in range(len(half_palindrome) + 1):
                palindrome = half_palindrome[:i] + odd_chars[0] + half_palindrome[i:]
                palindromes.add(palindrome + palindrome[::-1][1:])
        else:
            palindromes.add(half_palindrome + half_palindrome[::-1])
    return palindromes