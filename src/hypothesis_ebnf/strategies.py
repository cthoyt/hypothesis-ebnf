# -*- coding: utf-8 -*-

"""A Hypothesis strategy for generating sentences from an EBNF grammar."""

from hypothesis.searchstrategy import SearchStrategy
from hypothesis.strategies import defines_strategy
from nltk import CFG
from nltk.parse.generate import generate

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

    def __init__(self, grammar: str) -> None:
        """Load and initialize a context-free grammar.

        :param str grammar: An EBNF grammar as a string
        """
        super().__init__()
        self.grammar = grammar
        self.model = CFG.fromstring(self.grammar)
        self.model.start()

    def __repr__(self) -> str:
        """Return the grammar that represents this strategy."""
        return self.grammar

    def do_draw(self, data) -> str:
        """Sample from this grammar."""
        it = generate(self.model, n=1)  # make this draw next from sequence?
        return ' '.join(next(it))
