from collections import Counter

def palindromes_between_indices(s):
    substring = s[2:10]
    counter = Counter(substring.lower())
    odd_chars = [char for char, count in counter.items() if count % 2 != 0]
    if len(odd_chars) > 1:
        return set()
    half_palindrome = ''.join((char * (count // 2) for char, count in counter.items()))
    palindromes = set()
    for length in range(6, len(half_palindrome) * 2 + 1 + (1 if odd_chars else 0)):
        if length % 2 == 0:
            for i in range(len(half_palindrome) + 1):
                if 2 * i <= length and 2 * (len(half_palindrome) - i) <= length:
                    palindrome = half_palindrome[:i] + half_palindrome[i:length // 2][::-1]
                    palindromes.add(palindrome + palindrome[::-1])
        else:
            for i in range(len(half_palindrome)):
                if 2 * i + 1 <= length and 2 * (len(half_palindrome) - i) <= length:
                    for odd_char in odd_chars:
                        palindrome = half_palindrome[:i] + odd_char + half_palindrome[i:length // 2][::-1]
                        palindromes.add(palindrome + palindrome[:-1][::-1])
    return palindromes