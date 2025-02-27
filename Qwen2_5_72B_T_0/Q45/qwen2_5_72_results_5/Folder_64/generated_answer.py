from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:10].lower()
    letter_counts = Counter(substring)
    even_counts = {char: count for char, count in letter_counts.items() if count % 2 == 0}
    odd_counts = {char: count for char, count in letter_counts.items() if count % 2 != 0}
    if len(odd_counts) > 1:
        return set()
    palindromes = set()
    if len(odd_counts) == 1:
        middle_char = ''.join(odd_counts.keys())
    else:
        middle_char = ''
    for length in range(5, 11):
        half_length = length // 2
        half_palindrome = ''
        for char, count in even_counts.items():
            half_palindrome += char * (count // 2)
        for i in range(len(half_palindrome) + 1):
            for char in odd_counts:
                candidate = half_palindrome[:i] + middle_char + half_palindrome[i:]
                if len(candidate) == half_length:
                    palindromes.add(candidate + candidate[:-1][::-1])
                elif len(candidate) == half_length + 1:
                    palindromes.add(candidate + candidate[::-1])
    return palindromes