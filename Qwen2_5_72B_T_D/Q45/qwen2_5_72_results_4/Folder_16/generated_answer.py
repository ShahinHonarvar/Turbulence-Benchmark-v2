from collections import Counter

def palindromes_between_indices(s):
    substring = s[6:10]
    char_count = Counter(substring.lower())
    odds = sum((1 for count in char_count.values() if count % 2 != 0))
    possible_palindrome_length = sum((count // 2 for count in char_count.values())) * 2 + (1 if odds > 0 else 0)
    if possible_palindrome_length < 5:
        return set()
    palindromes = set()

    def generate_palindrome(current, remaining):
        if len(current) >= 5:
            palindromes.add(current + current[:len(current) // 2][::-1])
        for char in remaining:
            if remaining[char] > 1:
                remaining[char] -= 2
                generate_palindrome(current + char, remaining)
                remaining[char] += 2
            if remaining[char] == 1 and (not current):
                remaining[char] = 0
                generate_palindrome(char, remaining)
                remaining[char] = 1
    generate_palindrome('', char_count)
    return palindromes