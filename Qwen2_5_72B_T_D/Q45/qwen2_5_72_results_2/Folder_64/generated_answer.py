from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:10]
    letter_counts = Counter(filter(str.isalpha, substring.lower()))
    even_counts = {char: count for char, count in letter_counts.items() if count % 2 == 0}
    odd_counts = {char: count for char, count in letter_counts.items() if count % 2 != 0}
    if len(odd_counts) > 1:
        return set()
    half_palindrome = ''.join((char * (count // 2) for char, count in even_counts.items()))
    if odd_counts:
        middle_char = ''.join((char for char, count in odd_counts.items()))
    else:
        middle_char = ''
    palindromes = {half_palindrome[:i] + middle_char + half_palindrome[i:][::-1] for i in range(len(half_palindrome) + 1)}
    return {palindrome for palindrome in palindromes if len(palindrome) >= 5}