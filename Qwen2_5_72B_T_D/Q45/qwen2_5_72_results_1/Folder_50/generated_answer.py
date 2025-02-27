from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:9].lower()
    letter_counts = Counter(filter(str.isalpha, substring))
    single = []
    double = []
    for letter, count in letter_counts.items():
        if count // 2 > 0:
            double.extend([letter] * (count // 2))
        if count % 2 == 1:
            single.append(letter)
    double = ''.join(double)

    def generate_palindromes(double, single):
        if not double:
            return set((word + (sngl if sngl else '') + word[::-1] for sngl in single))
        results = set()
        for i in range(len(double)):
            new_double = double[:i] + double[i + 1:]
            new_single = single + [double[i]]
            results.update(generate_palindromes(new_double, new_single))
        return results
    palindromes = generate_palindromes(double, single)
    return {p for p in palindromes if len(p) >= 5}