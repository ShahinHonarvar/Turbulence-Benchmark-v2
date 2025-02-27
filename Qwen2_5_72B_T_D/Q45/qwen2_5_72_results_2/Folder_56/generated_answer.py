from collections import Counter

def palindromes_between_indices(s):
    substring = s[5:10].lower()
    letter_counts = Counter(substring)
    odd_counts = [char for char, count in letter_counts.items() if count % 2 != 0]
    if len(odd_counts) > 1:
        return set()
    half_palindrome = ''.join([char * (count // 2) for char, count in letter_counts.items()])
    palindromes = set()

    def generate_palindromes(half, remaining):
        if not remaining:
            palindrome = half + half[::-1]
            palindromes.add(palindrome)
        else:
            for i in range(len(remaining)):
                new_half = half + remaining[i]
                new_remaining = remaining[:i] + remaining[i + 1:]
                generate_palindromes(new_half, new_remaining)
    if odd_counts:
        for i in range(len(half_palindrome)):
            new_half = half_palindrome[:i] + odd_counts[0] + half_palindrome[i:]
            generate_palindromes(new_half, half_palindrome[:i] + half_palindrome[i:])
    else:
        generate_palindromes('', half_palindrome)
    return palindromes