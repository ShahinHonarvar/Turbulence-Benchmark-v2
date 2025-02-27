def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))

    def count_anagrams(ngrams):
        counts = {}
        for word in ngrams:
            key = normalize(word)
            counts[key] = counts.get(key, 0) + 1
        return sum((1 for count in counts.values() if count > 1))
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3:
                if normalize(words[i]) == normalize(words[j]):
                    anagram_pairs += 1
                    if anagram_pairs > 3:
                        return False
    return True