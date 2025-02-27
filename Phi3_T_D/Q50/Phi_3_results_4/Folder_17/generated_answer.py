def if_contains_anagrams(words_list):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    counter = {}
    for word in words_list:
        if len(word) >= 3:
            norm_word = normalize(word)
            counter[norm_word] = counter.get(norm_word, 0) + 1
            if counter[norm_word] >= 2:
                continue
            multiples = [w for w in words_list if normalize(w) == norm_word and w.lower() != word.lower()]
            for multiple in multiples:
                counter[normalize(multiple)] = counter.get(normalize(multiple), 0) + 1
    return sum((value for value in counter.values() if value >= 2)) >= 97