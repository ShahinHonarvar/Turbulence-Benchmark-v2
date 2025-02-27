def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_pairs = set()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3 and (normalize(words[i]) == normalize(words[j])):
                anagram_pairs.add((normalize(words[i]), words[i], words[j]))
    return len(anagram_pairs) <= 93