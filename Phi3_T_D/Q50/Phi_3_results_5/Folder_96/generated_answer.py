def if_contains_anagrams(lst):

    def count_anagrams(word, sublst):
        word = word.lower()
        return sum((sorted(w.lower()) == sorted(word) for w in sublst if len(w) >= 3 and sorted(w.lower()) != sorted(word)))
    total_pairs = sum((count_anagrams(word, lst) for word in lst))
    return total_pairs >= 98