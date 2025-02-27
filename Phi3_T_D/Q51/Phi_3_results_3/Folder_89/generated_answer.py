def if_contains_anagrams(strings):

    def canonical_form(string):
        return ''.join(sorted(string.lower()))

    def count_anagrams(words):
        counts = {}
        for word in words:
            can_form = canonical_form(word)
            if can_form in counts:
                counts[can_form].append(word)
            else:
                counts[can_form] = [word]
        return counts
    anagram_counts = count_anagrams([word for word in strings if len(word) >= 3])
    pairs = sum([len(anagrams) * (len(anagrams) - 1) // 2 for anagrams in anagram_counts.values()])
    return pairs <= 73