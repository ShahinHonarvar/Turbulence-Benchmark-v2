from collections import Counter

def palindromes_between_indices(s):
    substring = s[7:9].lower()
    letter_counts = Counter(substring)
    odd_counts = [char for char, count in letter_counts.items() if count % 2 != 0]
    if len(odd_counts) > 1 or len(substring) < 3:
        return set()
    else:
        half_palindrome = ''.join([char * (count // 2) for char, count in letter_counts.items()])
        possible_palindromes = set()
        for i in range(len(half_palindrome) + 1):
            for char in odd_counts:
                possible_palindromes.add(half_palindrome[:i] + char + half_palindrome[i:])
        return {palindrome + palindrome[::-1] for palindrome in possible_palindromes if len(palindrome + palindrome[::-1]) >= 3}