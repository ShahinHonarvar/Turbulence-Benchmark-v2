from collections import Counter

def palindromes_between_indices(s):
    substring = s[3:10].lower()
    letter_counts = Counter(substring)
    even_counts = {char: count for char, count in letter_counts.items() if count % 2 == 0}
    odd_chars = [char for char, count in letter_counts.items() if count % 2 != 0]
    palindromes = set()
    if len(odd_chars) > 1:
        return set()
    if len(odd_chars) == 1:
        center_char = odd_chars[0]
    else:
        center_char = ''
    half_palindrome = ''.join([char * (count // 2) for char, count in even_counts.items()])
    for i in range(len(half_palindrome) + 1):
        for j in range(len(center_char) + 1):
            palindrome = half_palindrome[:i] + center_char[:j] + center_char[j:] + half_palindrome[i:][::-1]
            if len(palindrome) >= 5:
                palindromes.add(palindrome)
    return palindromes