from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:10].lower()
    letter_counts = Counter(substring)
    odd_counts = [char for char, count in letter_counts.items() if count % 2 != 0]
    if len(odd_counts) > 1:
        return set()
    palindromes = set()

    def generate_palindrome(half, full):
        if not odd_counts:
            palindromes.add(full + half[::-1])
        else:
            for odd in odd_counts:
                palindromes.add(full + odd + half[::-1])

    def backtrack(half, remaining):
        if len(half) >= 1:
            generate_palindrome(half, remaining)
        for char in list(remaining):
            if remaining[char] > 1:
                remaining[char] -= 2
                backtrack(half + char, remaining)
                remaining[char] += 2
    backtrack('', letter_counts)
    return {palindrome for palindrome in palindromes if len(palindrome) >= 3}