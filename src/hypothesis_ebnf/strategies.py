# -*- coding: utf-8 -*-

"""A Hypothesis strategy for generating sentences from an EBNF grammar."""

import sys
from typing import Iterator, Optional, Sequence

from hypothesis.searchstrategy import SearchStrategy
from hypothesis.strategies import defines_strategy
from nltk import CFG
from nltk.parse.generate import _generate_all

__all__ = [
    'sentences',
]


@defines_strategy
def sentences(grammar: str) -> SearchStrategy:
    """Generate a strategy to generate sentences from an EBNF grammar.

    :param str grammar: An EBNF grammar as a string
    """
    return EBNFStrategy(grammar)


class EBNFStrategy(SearchStrategy):
    """A search strategy for generating sentences from an EBNF grammar."""

    def __init__(self, grammar: str, depth: Optional[int] = None) -> None:
        """Load and initialize a context-free grammar.

        :param str grammar: An EBNF grammar as a string
        """
        super().__init__()
        self.grammar = grammar
        self.cfg = CFG.fromstring(self.grammar)
        self.start = self.cfg.start()

        self._generator = self._get_generator(depth=depth)

    def _get_generator(self, depth: Optional[int] = None) -> Iterator[Sequence[str]]:
        if depth is None:
            depth = sys.maxsize
        return iter(_generate_all(self.cfg, [self.start], depth))

    def __repr__(self) -> str:
        """Return the grammar that represents this strategy."""
        return self.grammar

    def __next__(self) -> Sequence[str]:
        """Get the next entry in this grammars."""
        sentence_parts = next(self._generator)
        sentence = ' '.join(sentence_parts)
        return sentence

    def do_draw(self, data) -> str:
        """Sample from this grammar."""
        return next(self)
