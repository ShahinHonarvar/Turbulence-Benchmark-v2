from collections import Counter

def palindromes_between_indices(s):
    chars = s[7:9]
    char_count = Counter(chars.lower())
    odd_counts = sum((1 for count in char_count.values() if count % 2 != 0))
    possible_palindromes = set()
    if odd_counts <= 1 and any((char.isalpha() for char in chars)):
        for length in range(3, 10, 2):
            if all((count // 2 >= (length - 1) // 2 for count in char_count.values())):
                for center in char_count.keys():
                    palindrome = center
                    for _ in range((length - 1) // 2):
                        for char, count in char_count.items():
                            if count > 0 and char != center:
                                palindrome = char + palindrome + char
                                char_count[char] -= 1
                                break
                    possible_palindromes.add(palindrome)
                    for c in palindrome:
                        char_count[c] += 1
    return possible_palindromes