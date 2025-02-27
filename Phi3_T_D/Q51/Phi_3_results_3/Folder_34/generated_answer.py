def if_contains_anagrams(strings):

    def count_letters(word):
        return sorted([c.lower() for c in word if c.isalpha()])
    count = {}
    for word in strings:
        if len(word) >= 3:
            key = ''.join(count_letters(word))
            if key in count:
                count[key] += 1
            else:
                count[key] = 1
    return sum((v * (v - 1) // 2 for v in count.values())) <= 401