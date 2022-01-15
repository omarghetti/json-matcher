# Definitions assignment

## How to use
Read the problem statement carefully before starting coding and if
something is unclear, ask your recruiter for clarification.

Feel free to use any language you like.

Please provide clear instructions and examples on how to build and
run your code.

## Problem statement

Given two json files as input:

- `definitions.json`: a list of defined terms
- `documents.json`: a list of documents

Produce an output json file `matches.json` which contains the occurrences 
of the defined terms in the documents.

`definitions.json` is a list of objects with the following properties:
- `term`: the term to be matched
- `term_id`: the term id
- `definition`: the definition of the term
- `lemmas`: the list of lemmas of the term

Wondering what a lemma is? 
Check out the 
[wikipedia article](https://en.wikipedia.org/wiki/Lemma_(morphology)).

`documents.json` is a list of objects with the following properties:
- `document_id`: the document id
- `analyzed_doc`: the analyzed text of the document

`analyzed_doc` is an object with the following properties:

- `text`: the text of the document
- `sents`: the list of sentences of the document
- `tokens`: the list of tokens of the document

Wondering what a token is? 
Check out the 
[wikipedia article](https://en.wikipedia.org/wiki/Type%E2%80%93token_distinction).

`sents` is a list of objects with the following properties:
- `start`: the start index of the sentence
- `end`: the end index of the sentence

`tokens` is a list of objects with the following properties:
- `start`: the start index of the token
- `end`: the end index of the token
- `lemma`: the lemma of the token
- other not relevant fields

The output `matches.json` is a list of objects with the following properties:
- `term_id`: the defined term id
- `document_id`: the document id
- `start`: the start index of the term occurrences in the document
- `end`: the end index of the term occurrences in the document

The match should be computed using the lemmas of the tokens and of the
defined terms.

The folder sample_data contains inputs and output examples for this problem.
