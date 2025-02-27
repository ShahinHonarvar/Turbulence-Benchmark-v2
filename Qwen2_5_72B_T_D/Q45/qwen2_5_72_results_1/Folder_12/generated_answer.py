from collections import Counter

def palindromes_between_indices(s):
    substring = s[3:9].lower()
    freq = Counter(substring)
    odd_chars = [char for char, count in freq.items() if count % 2 != 0]
    even_chars = [char for char, count in freq.items() if count % 2 == 0]
    if len(odd_chars) > 1 or not even_chars:
        return set()
    if len(odd_chars) == 1 and len(substring) < 4:
        return set()
    half_palindrome = ''.join([char * (count // 2) for char, count in freq.items()])
    palindromes = set()

    def generate_palindromes(half, remaining):
        if len(half) * 2 >= 4:
            if odd_chars:
                palindrome = half + odd_chars[0] + half[::-1]
            else:
                palindrome = half + half[::-1]
            palindromes.add(palindrome)
        for char in remaining:
            new_half = half + char
            new_remaining = remaining.replace(char, '', 1)
            generate_palindromes(new_half, new_remaining)
    generate_palindromes('', half_palindrome)
    return palindromes