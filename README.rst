Hypothesis-EBNF
===============
A Hypothesis strategy for generating sentences from an EBNF grammar.

Can be imported like any other strategy, and used in the ``given()`` annotation with Hypothesis tests.

.. code-block:: python

	# third-party
	from hypothesis import given
	from nltk.parse.generate import demo_grammar

	# code from this repository
	from hypothesis_ebnf import ebnf


	@given(sentence=ebnf(demo_grammar))
	def test_demo_grammar(sentence):
		"""Use the demo grammar from NLTK to make some test cases."""
		print(sentence)
		assert isinstance(sentence, str)

Installation
------------
This code can currently be installed via GitHub with:

.. code-block:: bash

	$ python3 -m pip install git+https://github.com/cthoyt/hypothesis-ebnf.git@master

Once it's tested better, it will be put on PyPI.

Acknowledgements and References
-------------------------------
- `Hypothesis <https://hypothesis.readthedocs.io/en/latest/>`_
- `Natural Language Toolkit <https://www.nltk.org/>`_
