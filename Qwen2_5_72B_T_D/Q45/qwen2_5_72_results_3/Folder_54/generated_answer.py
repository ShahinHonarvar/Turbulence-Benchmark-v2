from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:10].lower()
    char_count = Counter(substring)
    palindromes = set()

    def generate_palindrome(length, half, second_half, used):
        if length % 2 == 0 and len(half) == length // 2:
            palindromes.add(half + second_half[::-1])
        elif len(half) == length // 2 + 1:
            palindromes.add(half + second_half[::-1])
        for char in char_count:
            if char_count[char] > 1:
                char_count[char] -= 2
                generate_palindrome(length, half + char, second_half + char, used + [char])
                char_count[char] += 2
            elif char_count[char] == 1 and length % 2 != 0 and (char not in used):
                char_count[char] -= 1
                generate_palindrome(length, half, second_half + char, used + [char])
                char_count[char] += 1
    for length in range(4, 7):
        generate_palindrome(length, '', '', [])
    return palindromes