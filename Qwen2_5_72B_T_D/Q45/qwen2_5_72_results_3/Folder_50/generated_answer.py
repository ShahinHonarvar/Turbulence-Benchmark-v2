from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:9].lower()
    letter_counts = Counter(substring)
    even_chars = []
    odd_char = ''
    for char, count in letter_counts.items():
        if count % 2 == 0:
            even_chars.append(char * (count // 2))
        elif odd_char == '':
            odd_char = char * (count // 2 + 1)
        else:
            odd_char = char * (count // 2)
            even_chars.append(odd_char)
            odd_char = ''
    half_palindrome = ''.join(even_chars) + odd_char
    full_palindromes = set()
    if len(half_palindrome) * 2 + (1 if odd_char else 0) >= 5:
        for i in range(len(half_palindrome) + 1):
            for j in range(len(half_palindrome), -1, -1):
                palindrome = half_palindrome[:i] + half_palindrome[j:]
                if len(palindrome) >= 5:
                    full_palindromes.add(palindrome + palindrome[::-1][-(len(palindrome) - (1 if odd_char else 0)):])
    return full_palindromes