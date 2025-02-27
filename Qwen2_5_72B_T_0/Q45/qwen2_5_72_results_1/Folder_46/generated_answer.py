from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:10].lower()
    letter_counts = Counter(substring)
    even_counts = {char: count for char, count in letter_counts.items() if count % 2 == 0}
    odd_counts = {char: count for char, count in letter_counts.items() if count % 2 != 0}
    if sum(odd_counts.values()) > 1:
        return set()
    palindromes = set()
    if not odd_counts:
        half_palindrome = ''.join([char * (count // 2) for char, count in even_counts.items()])
        for i in range(len(half_palindrome) + 1):
            for j in range(6, len(half_palindrome) * 2 + 1, 2):
                if j <= len(half_palindrome) * 2:
                    palindrome = half_palindrome[:i] + half_palindrome[i:i + j // 2][::-1]
                    if len(palindrome) >= 6:
                        palindromes.add(palindrome)
    else:
        odd_char = list(odd_counts.keys())[0]
        half_palindrome = ''.join([char * (count // 2) for char, count in even_counts.items()])
        for i in range(len(half_palindrome) + 1):
            for j in range(6, len(half_palindrome) * 2 + 2, 2):
                if j <= len(half_palindrome) * 2 + 1:
                    palindrome = half_palindrome[:i] + odd_char + half_palindrome[i:i + (j - 1) // 2][::-1]
                    if len(palindrome) >= 6:
                        palindromes.add(palindrome)
    return palindromes