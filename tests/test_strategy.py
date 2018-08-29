# -*- coding: utf-8 -*-

"""Tests for hypothesis-ebnf."""

from hypothesis import given
from nltk.parse.generate import demo_grammar

from hypothesis_ebnf import sentences


@given(sentence=sentences(demo_grammar))
def test_demo_grammar(sentence):
    """Use the demo grammar from NLTK to make some test cases."""
    print(sentence)
    assert isinstance(sentence, str)


if __name__ == '__main__':
    test_demo_grammar()
