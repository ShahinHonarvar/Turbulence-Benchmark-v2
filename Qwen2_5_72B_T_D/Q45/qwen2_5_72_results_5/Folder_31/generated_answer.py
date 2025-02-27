from collections import Counter

def palindromes_between_indices(s):

    def generate_palindromes(counter, length):

        def backtrack(path, length):
            if length == 0:
                result.add(''.join(path))
                return
            for char in counter:
                if counter[char] >= 2:
                    counter[char] -= 2
                    backtrack(path + [char, char], length - 2)
                    counter[char] += 2
            for char in counter:
                if counter[char] % 2 != 0:
                    temp = path[:]
                    temp[length // 2] = char
                    backtrack(temp, length - 1)
        result = set()
        mid = length // 2
        for char in counter:
            if counter[char] % 2 != 0:
                counter[char] -= 1
                backtrack([None] * length, length)
                counter[char] += 1
            else:
                backtrack([None] * length, length)
        return result
    substring = s[1:9].lower()
    counter = Counter(substring)
    return generate_palindromes(counter, 6)