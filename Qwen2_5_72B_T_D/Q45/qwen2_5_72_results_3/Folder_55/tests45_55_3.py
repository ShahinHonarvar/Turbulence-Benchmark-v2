from Q45.qwen2_5_72_results_3.Folder_55.generated_answer import palindromes_between_indices


def test_string_of_similar_chars():
    s = ''.join('a' for _ in range(2 + 1))
    if 2 - 0 + 1 < 3:
        assert not palindromes_between_indices(s)
    else:
        assert palindromes_between_indices(s) == {'a' * i for i in range(3, 2 - 0 + 2)}


def test_string_of_distinct_chars():
    s = 'abcdefghijkl'
    assert not palindromes_between_indices(s)


def test_string_of_spaces():
    s = ' ' * (2 * 2)
    assert not palindromes_between_indices(s)


def test_string_of_same_punctuations():
    s = '@' * (2 * 2)
    assert not palindromes_between_indices(s)


def test_string_of_same_numbers():
    s = '0' * (2 * 2)
    assert not palindromes_between_indices(s)
        

def test_length_of_palindrome():
    s = ''.join('a' for _ in range(2 + 1))
    returned_result = palindromes_between_indices(s)
    for i in returned_result:
        assert 3 <= len(i) <= 2 - 0 + 1


def test_string_of_spaces_and_letters():
    s = ' a ' * (2 + 1)
    ss = s[0:2 + 1]
    ss = ss.replace(' ', '')
    length = len(ss)
    if length < 3:
        assert not palindromes_between_indices(s)
    else:
        min_ = min(length, 3)
        max_ = max(length, 3)
        assert palindromes_between_indices(s) == {'a' * i for i in range(min_, max_ + 1)}


def test_string_of_punctuations_and_letters():
    s = '%a&' * (2 + 1)
    ss = s[0:2 + 1]
    ss = ss.replace('%', '')
    ss = ss.replace('&', '')
    length = len(ss)
    if length < 3:
        assert not palindromes_between_indices(s)
    else:
        min_ = min(length, 3)
        max_ = max(length, 3)
        assert palindromes_between_indices(s) == {'a' * i for i in range(min_, max_ + 1)}
        