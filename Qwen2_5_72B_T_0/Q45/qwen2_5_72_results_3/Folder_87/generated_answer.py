from collections import Counter

def palindromes_between_indices(s):
    substring = s[3:10].lower()
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

    def backtrack(half, full, remaining):
        if len(half) == (len(substring) - len(odd_counts)) // 2:
            generate_palindrome(half, full)
            return
        for char in remaining:
            if remaining[char] > 1:
                remaining[char] -= 2
                backtrack(half + char, full, remaining)
                remaining[char] += 2
    backtrack('', '', letter_counts)
    return {palindrome for palindrome in palindromes if len(palindrome) >= 3}