from toybox.textstats import average_word_length, char_count, sentence_count, word_count


def test_char_count():
    assert char_count("hello") == 5


def test_word_count():
    assert word_count("the quick brown fox") == 4


def test_sentence_count():
    assert sentence_count("Hi there. How are you? Fine!") == 3


def test_average_word_length():
    assert average_word_length("a bb ccc") == 2.0
