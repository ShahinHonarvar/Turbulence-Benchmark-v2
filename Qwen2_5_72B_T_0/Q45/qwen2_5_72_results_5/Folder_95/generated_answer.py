from collections import Counter

def palindromes_between_indices(s):
    substring = s[7:9].lower()
    letter_counts = Counter(substring)
    odd_counts = [char for char, count in letter_counts.items() if count % 2 != 0]
    if len(odd_counts) > 1:
        return set()
    else:
        half_palindrome = ''.join([char * (count // 2) for char, count in letter_counts.items()])
        if odd_counts:
            middle_char = odd_counts[0]
        else:
            middle_char = ''
        palindromes = set()
        for i in range(len(half_palindrome) + 1):
            for j in range(len(half_palindrome) + 1):
                if i != j:
                    candidate = half_palindrome[:i] + middle_char + half_palindrome[i:]
                    candidate = candidate + candidate[::-1][len(middle_char):]
                    if len(candidate) >= 3:
                        palindromes.add(candidate)
        return palindromes