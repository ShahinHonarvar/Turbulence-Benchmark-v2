from collections import Counter

def palindromes_between_indices(s):
    substring = s[2:6].lower()
    char_count = Counter(substring)
    odd_char = [char for char, count in char_count.items() if count % 2 != 0]
    if len(odd_char) > 1:
        return set()
    palindromes = set()

    def generate_palindrome(current, remaining):
        if not any(remaining.values()):
            if len(current) >= 5:
                palindromes.add(current)
            return
        for char in list(remaining.keys()):
            if remaining[char] > 1:
                remaining[char] -= 2
                generate_palindrome(char + current + char, remaining)
                remaining[char] += 2
    if len(odd_char) == 1:
        for char in list(char_count.keys()):
            if char_count[char] > 1:
                char_count[char] -= 2
                generate_palindrome(odd_char[0], char_count)
                char_count[char] += 2
    else:
        generate_palindrome('', char_count)
    return palindromes