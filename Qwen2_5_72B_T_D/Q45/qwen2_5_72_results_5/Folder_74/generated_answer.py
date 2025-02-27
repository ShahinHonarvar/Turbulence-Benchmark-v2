from collections import Counter

def palindromes_between_indices(s):
    substring = s[1:7].lower()
    letter_counts = Counter(substring)
    even_counts = [char for char, count in letter_counts.items() if count % 2 == 0]
    odd_counts = [char for char, count in letter_counts.items() if count % 2 != 0]
    if len(odd_counts) > 1 or sum(letter_counts.values()) < 6:
        return set()
    palindromes = set()

    def generate_palindrome(slate, remaining):
        if len(slate) * 2 + (1 if len(odd_counts) == 1 else 0) == 6:
            if len(odd_counts) == 1:
                palindrome = slate + odd_counts[0] + slate[::-1]
            else:
                palindrome = slate + slate[::-1]
            palindromes.add(palindrome)
        else:
            for char in remaining:
                if remaining[char] > 1:
                    remaining[char] -= 2
                    generate_palindrome(slate + char, remaining)
                    remaining[char] += 2
    generate_palindrome('', letter_counts)
    return palindromes