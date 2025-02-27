from collections import Counter

def palindromes_between_indices(s):
    substring = s[2:10]
    letter_counts = Counter(filter(str.isalpha, substring.lower()))
    possible_palindromes = set()
    for length in range(6, 10):
        half_length = length // 2
        palindrome_half = ''
        for letter, count in letter_counts.items():
            palindrome_half += letter * (count // 2)
            if len(palindrome_half) >= half_length:
                break
        for i in range(len(palindrome_half) - half_length + 1):
            candidate = palindrome_half[i:i + half_length]
            if length % 2 == 1:
                for center in letter_counts:
                    if letter_counts[center] % 2 == 1:
                        palindrome = candidate + center + candidate[::-1]
                        if len(palindrome) == length:
                            possible_palindromes.add(palindrome)
            else:
                palindrome = candidate + candidate[::-1]
                if len(palindrome) == length:
                    possible_palindromes.add(palindrome)
    return {palindrome for palindrome in possible_palindromes if palindrome == palindrome[::-1]}