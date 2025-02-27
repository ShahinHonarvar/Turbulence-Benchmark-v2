from collections import Counter

def palindromes_between_indices(s):
    substring = s[2:9].lower()
    chars = Counter(substring)
    palindromes = set()

    def generate_palindrome(current, remaining):
        if len(current) >= 4 and current == current[::-1]:
            palindromes.add(current)
        for char in remaining:
            if remaining[char] > 0:
                remaining[char] -= 1
                generate_palindrome(current + char, remaining)
                remaining[char] += 1
    generate_palindrome('', chars)
    return palindromes