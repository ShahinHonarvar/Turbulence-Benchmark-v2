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
            for j in range(len(half_palindrome) + 1):
                candidate = half_palindrome[:i] + half_palindrome[j:]
                if len(candidate) >= 3:
                    palindromes.add(candidate + candidate[::-1])
    else:
        odd_char = list(odd_counts.keys())[0]
        half_palindrome = ''.join([char * (count // 2) for char, count in even_counts.items()])
        for i in range(len(half_palindrome) + 1):
            for j in range(len(half_palindrome) + 1):
                candidate = half_palindrome[:i] + half_palindrome[j:]
                if len(candidate) >= 3:
                    palindromes.add(candidate + odd_char + candidate[::-1])
    return {palindrome for palindrome in palindromes if len(palindrome) >= 6}