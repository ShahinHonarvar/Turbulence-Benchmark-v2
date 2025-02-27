from collections import Counter

def palindromes_between_indices(s):
    substring = s[2:10]
    letter_counts = Counter(filter(str.isalpha, substring.lower()))
    even_counts = {char: count // 2 for char, count in letter_counts.items()}
    odd_chars = [char for char, count in letter_counts.items() if count % 2 != 0]
    if len(odd_chars) > 1:
        return set()
    half_palindrome = ''.join([char * count for char, count in sorted(even_counts.items())])
    if odd_chars:
        middle = odd_chars[0]
    else:
        middle = ''
    full_palindrome = half_palindrome + middle + half_palindrome[::-1]
    if len(full_palindrome) < 4:
        return set()
    palindromes = set((full_palindrome[i:j] for i in range(len(full_palindrome)) for j in range(i + 4, len(full_palindrome) + 1) if full_palindrome[i:j] == full_palindrome[i:j][::-1]))
    return palindromes