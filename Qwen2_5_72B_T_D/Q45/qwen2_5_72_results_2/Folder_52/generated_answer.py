from collections import Counter

def palindromes_between_indices(s):
    s_sub = s[0:8]
    letter_counts = Counter(filter(str.isalpha, s_sub.lower()))
    odd_counts = [count for count in letter_counts.values() if count % 2 != 0]
    if len(odd_counts) > 1:
        return set()
    available_letters = ''.join([letter * (count // 2) for letter, count in letter_counts.items()])

    def generate_palindromes(prefix, available_letters):
        if not available_letters:
            yield (prefix + prefix[::-1])
        for i in range(len(available_letters)):
            yield from generate_palindromes(prefix + available_letters[i], available_letters[:i] + available_letters[i + 1:])
    palindromes = {palindrome for palindrome in generate_palindromes('', available_letters) if len(palindrome) >= 6}
    return palindromes