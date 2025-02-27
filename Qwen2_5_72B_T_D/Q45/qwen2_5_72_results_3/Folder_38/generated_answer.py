from collections import Counter

def palindromes_between_indices(s):
    substring = s[3:9]
    letter_counts = Counter(filter(str.isalpha, substring.lower()))
    palindrome_set = set()

    def can_form_palindrome(counts):
        odd_counts = sum((1 for count in counts.values() if count % 2 != 0))
        return odd_counts <= 1

    def generate_palindromes(counts, half_str, pos=0):
        if pos == len(half_str):
            middle = ''.join(half_str)
            palindrome = middle + middle[::-1]
            if len(palindrome) >= 5:
                palindrome_set.add(palindrome)
            return
        for char, count in counts.items():
            if count >= 2:
                half_str[pos] = char
                counts[char] -= 2
                generate_palindromes(counts, half_str, pos + 1)
                counts[char] += 2
    if can_form_palindrome(letter_counts):
        half_length = sum(letter_counts.values()) // 2
        if half_length < 3:
            return set()
        half_str = [None] * half_length
        generate_palindromes(letter_counts, half_str)
    return palindrome_set