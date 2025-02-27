from collections import Counter

def palindromes_between_indices(s):
    substring = s[2:7]
    counter = Counter(filter(str.isalpha, substring.lower()))
    palindrome_set = set()

    def generate_palindrome(current, remaining):
        if len(current) >= 5 and current == current[::-1]:
            palindrome_set.add(current)
        for char in remaining:
            if remaining[char] > 0:
                remaining[char] -= 1
                generate_palindrome(current + char, remaining)
                remaining[char] += 1
    generate_palindrome('', counter)
    return palindrome_set