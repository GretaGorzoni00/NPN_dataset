# NPN dataset

[![CC BY- 4.0][cc-by-shield]][cc-by]

- [NPN dataset](#npn-dataset)
	- [Dataset construction](#dataset-construction)
		- [The structure of Masini (2024)](#the-structure-of-masini-2024)
		- [From Masini (2024) to `NPN dataset`](#from-masini-2024-to-npn-dataset)
	- [NPN dataset](#npn-dataset-1)
		- [Repository](#repository)
		- [Construction instances parameters:](#construction-instances-parameters)
		- [Distractor instances parameters:](#distractor-instances-parameters)
	- [References](#references)


The present dataset collects instances of the Italian Noun-Preposition-Noun (NPN) discontinuous reduplication construction (e.g., `pagine su pagine`, *pages upon pages*). The instances come from the CORIS corpus, 2021 version, 165Mw ([https://corpora.ficlit.unibo.it/TCORIS/](https://corpora.ficlit.unibo.it/TCORIS/)).

## Dataset construction

Data is built upon Masini (2024), the result of an empirical analysis that surveys all occurrences of the construction pattern NPN found in [CORIS](https://corpora.ficlit.unibo.it/TCORIS/): a large-scale reference corpus of contemporary written Italian developed at the University of Bologna.

### The structure of Masini (2024)

Masini (2024) contains 1298 construction types, each annotated with the following parameters:
- NPN: the NPN expression (type);
- token_frequency: the token frequency of the NPN expression in the CORIS 2021 corpus;
- preposition: the preposition found in the NPN expression (12 possible values);
- reduplicated_noun: the lemmatised form of the noun that appears in the NPN expression;
- number_of_noun: the number value of the noun that appears in the NPN expression, with possible values `singular`, `plural`, `singular/plural`;
- syntactic_function: the syntactic function of the NPN expression, with possible values `modifier`, `nominal`, `clause`;
- meaning: the semantic function of the NPN expression (9 possible values);

The original data taken as a starting point for this work is contained in file `dataset_Masini.csv`.

### From Masini (2024) to `NPN dataset`

For the present dataset, we only considered a subset of the original data, namely constructions instantiated by prepositions **su** and **a**.
Each construction form in this subset was manually searched in CORIS in order to retrieve the occurrence within its sentential boundaries.

This procedure revealed a number of instances that cannot be identified through a CQL query of the form NN–PREP–NN, since automatic POS tagging occasionally fails to assign the NN tag to nouns that function as such, instead labelling them as verbs (VERB).

Main differences in frequency between the present dataset and Masini (2024), where they occur, can therefore be attributed to this issue. Other mismatch come from the decision for the present dataset to exclude some occurrences, the main reasons are: duplication of sentences in the corpus, nominal phrase with no significat context.

The differences in frequencies between Masini (2024) and the present dataset are underlined in `dataset_freq.csv`.

The exclusion criteria reported by (Masinini, 2024) were initially followed:
- foreign expression (e.g., `vis a vis`)
- instances containing proper nouns (e.g., `Italia su Italia`)
- occurrences that actually belong to another construction (e.g., `PNPN`)

With respect to the original dataset, we removed:
- lemmas that are primarily adjectives or adverbs (e.g., `poco a poco`)
- dialectal expressions (e.g., `core a core`)
- nominal expressions (e.g., newspaper headlines)
- expressions appearing in bullet lists without a proper sentential context

Hence, both construction and non-constructions (henceforth, `distractors`) instances were annotated with categories listed in section [NPN dataset](#npn-dataset-1).

## NPN dataset

### Repository

The present repository is organized as follows:

<pre>
data/
├── construction.csv
├── distractor.csv
│
├── agreements/
│   └── license.txt
│
├── dataset_Masini.csv
└── dataset_freq.csv
</pre>


### Construction instances parameters:

Constraction dataset contains 3256 occurrences, each  and annotated with the following parameters:
- NPN: the NPN expression (type);
- preposition: the preposition found in the NPN expression, with possible values `a`, `su`;
- noun: the lemmatised form of the noun that appears in the NPN expression;
- number_of_noun: tthe number value of the noun that appears in the NPN expression, with possible values `singular` (2890 token), `plural` (346 token), `singular/plural` (20 token);
- syntactic_function: the syntactic function of the NPN expression, with possible values `modifier` (2089 token), `nominal` (1166 token), `clause` (1);
- meaning: the semantic function of the NPN expression, with possible values `succession/iteration/distributivity` (577 token), `greater_plurality/accumulation` (392 token), `juxtaposition/contact` (1144 token), `connection/transition` (50 token), `inescapable_presupposition` (1 token), intensification (1 token) `idiosyncratic` (1091 token)

### Distractor instances parameters:

In addition to the dataset of actual occurrences of the NPN construction, a parallel dataset of distractors was created, defined as sequences sharing the same surface form as the construction but not instantiating it.

Distractor dataset contains 1751 occurrences, each  and annotated with the following parameters:
- NPN: surface of the distractor pattern shared with NPN construction;
- preposition: the preposition found in the pattern, with possible values `a` (1565 token), `su` (186 token);
- noun: the lemmatised form of the noun that appers reduplicated in the pattern;
- number_of_noun: tthe number value of the noun that appears in the pattern, with possible values `singular` (1600 token), `plural`(1750 token), `singular/plural` (8 token), `X` (108 token);
- Type of distractor pattern, with possible values `N_extended` (35 token), `NsuNgiù` (392 token), `juxtaposition/contact` (13 token), `NumPNum` (100 token), `PNPN` (1442 token), `proper_name_inglobation` (31 token), `thematic_target` (50 token), `verbal` (80 token):
- Other_cxv: whether this represents a structurally distinct construction construction different from the NPN linked horizontally or merely a surface-isomorphic pattern, with possible values `yes` (1535 token), `no` (216 token)


## References

- Masini, Francesca (2024) NPN discontinuous reduplications in Italian: dataset. Univesity of Bologna. DOI [10.6092/unibo/amsacta/7489](https://doi.org/10.6092/unibo%2Famsacta%2F7489)




-----

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by-nc-sa].

<!-- [![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa] -->

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://licensebuttons.net/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
