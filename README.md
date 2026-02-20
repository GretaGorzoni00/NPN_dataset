# The NPN dataset

This repository is associated with the following dataset published on Zenodo:

**Title:** *NPN Construction and Distractor dataset*  
**Authors:** Greta Gorzoni, Ludovica Pannitto, Francesca Masini  
**Year:** 2025  
**DOI:** https://doi.org/10.5281/zenodo.18716255

[![DOI](https://zenodo.org/badge/1118878500.svg)](https://doi.org/10.5281/zenodo.18716255)

[![CC BY- 4.0][cc-by-shield]][cc-by]

- [The NPN dataset](#the-npn-dataset)
	- [Dataset construction](#dataset-construction)
		- [The structure of Masini (2024)](#the-structure-of-masini-2024)
		- [From Masini (2024) to `NPN dataset`](#from-masini-2024-to-npn-dataset)
	- [NPN dataset](#npn-dataset)
		- [Repository](#repository)
		- [Construction instances parameters](#construction-instances-parameters)
		- [Distractor instances parameters](#distractor-instances-parameters)
	- [Coder agreement](#coder-agreement)
	- [How to cite](#how-to-cite)
	- [References](#references)
	- [Changelog](#changelog)


The present dataset collects instances of the Italian Noun-Preposition-Noun (NPN) discontinuous reduplication construction (e.g., `pagine su pagine`, *pages upon pages*). The instances come from the CORIS corpus, 2021 version, 165Mw ([https://corpora.ficlit.unibo.it/TCORIS/](https://corpora.ficlit.unibo.it/TCORIS/)).

## Dataset construction

Data is built upon Masini (2024), the result of an empirical analysis that surveys all occurrences of the construction pattern NPN found in [CORIS](https://corpora.ficlit.unibo.it/TCORIS/): a large-scale reference corpus of contemporary written Italian developed at the University of Bologna.

### The structure of Masini (2024)

Masini (2024) contains 1298 construction types, each annotated with the following parameters:
- **NPN**: the NPN expression (type);
- **token_frequency**: the token frequency of the NPN expression in the CORIS 2021 corpus;
- **preposition**: the preposition found in the NPN expression (12 possible values);
- **reduplicated_noun**: the lemmatised form of the noun that appears in the NPN expression;
- **number_of_noun**: the number value of the noun that appears in the NPN expression, with possible values `singular`, `plural`, `singular/plural`;
- **syntactic_function**: the syntactic function of the NPN expression, with possible values `modifier`, `nominal`, `clause`;
- **meaning**: the semantic function of the NPN expression (9 possible values);

The original data taken as a starting point for this work is contained in file `dataset_Masini.csv`.

### From Masini (2024) to `NPN dataset`

For the present dataset, we only considered a subset of the original data, namely constructions instantiated by prepositions **su** and **a**.
Each construction form in this subset was manually searched in CORIS in order to retrieve the occurrence within its sentential boundaries.

This procedure revealed a number of instances that cannot be identified through a CQL query of the form NN–PREP–NN, since automatic PoS tagging in CORIS occasionally fails to assign the NN tag to nouns that function as such, instead labelling them as verbs (VERB).

Main differences in frequency between the present dataset and Masini (2024), where they occur, can therefore be attributed to this issue. Other mismatch come from the decision for the present dataset to exclude some occurrences, the main reasons are: duplication of sentences in the corpus, nominal phrase with no significant context.

The differences in frequencies between Masini (2024) and the present dataset are underlined in `dataset_freq.csv`.

The exclusion criteria reported by (Masini, 2024) were initially followed:

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

Data in the present repository is organized as follows:

```
.
├── data/
│	├── construction.csv
│	└── distractor.csv
│
├── agreements/
│   ├── exp1.csv
│	└── exp2.csv
│
├── dataset_Masini.csv
└── dataset_freq.csv
```

### Construction instances parameters

Construction dataset (`data/construction.csv`) contains 3256 occurrences, each annotated with the following parameters:

- **NPN**: the NPN expression (type);
- **preposition**: the preposition found in the NPN expression, with possible values `a`, `su`;
- **noun**: the lemmatised form of the noun that appears in the NPN expression;
- **number_of_noun**: the number value of the noun that appears in the NPN expression, with possible values `singular` (2890 items), `plural` (346 items), `singular/plural` (20 items);
- **syntactic_function**: the syntactic function of the NPN expression, with possible values `modifier` (2089 items), `nominal` (1166 items), `clause` (1 item);
- **meaning**: the semantic function of the NPN expression, with possible values `succession/iteration/distributivity` (577 items), `greater_plurality/accumulation` (392 items), `juxtaposition/contact` (1144 items), `connection/transition` (50 items), `inescapable_presupposition` (1 item), intensification (1 items) `idiosyncratic` (1091 items)

### Distractor instances parameters

In addition to the dataset of actual occurrences of the NPN construction, a parallel dataset of distractors (`data/distractor.csv`) was created, defined as sequences sharing the same surface form as the construction but not instantiating it.

Distractor dataset contains 1751 occurrences, each  and annotated with the following parameters:

- **NPN**: surface of the distractor pattern shared with NPN construction;
- **preposition**: the preposition found in the pattern, with possible values `a` (1565 items), `su` (186 items);
- **noun**: the lemmatised form of the noun that appers reduplicated in the pattern;
- **number_of_noun**: the number value of the noun that appears in the pattern, with possible values `singular` (1600 items), `plural`(1750 items), `singular/plural` (8 items), `X` (108 items);
- **type of distractor**: pattern, with possible values `N_extended` (35 items), `NsuNgiù` (392 items), `juxtaposition/contact` (13 items), `NumPNum` (100 items), `PNPN` (1442 items), `proper_name_inglobation` (31 items), `thematic_target` (50 items), `verbal` (80 items);
- **proper_cxn**: whether this represents a structurally distinct construction construction different from the NPN linked horizontally or merely a surface-isomorphic pattern, with possible values `yes` (1535 items), `no` (216 items)

## Coder agreement


**Annotation process**  
Inter-annotator agreement was evaluated on a controlled subset of 100 instances. All annotators followed a shared annotation schema, including formal constraints and semantically motivated label definitions derived from the literature.

The agreement subset was balanced across semantic categories:  
– 50 instances from the subset of NPN constructions instantiated by the preposition  *a* (25 `juxt`, 25 `succ`)  
– 50 instances from the subset of NPN constructions instantiated by the preposition  *su* (25 `succ`, 25 `acc`)

**Inter-annotator agreement**  
Annotation quality was assessed using Cohen’s κ and Krippendorff’s α. Pairwise Cohen’s κ shows consistently high observed agreement (Ao = 0.87–0.94), with stable expected agreement (Ae ≈ 0.36–0.37), resulting in strong to near-perfect reliability across annotator pairs (κ = 0.79–0.91).

Since Cohen’s κ assumes equal distances between labels, agreement was also evaluated using Krippendorff’s α, which supports distance-sensitive comparison. Nominal α is high (α = 0.858) and further increases when a reduced penalty is assigned to confusions between semantically adjacent labels (custom distance = 0.5; α = 0.892). This indicates that residual disagreement mainly concerns borderline semantic cases rather than inconsistencies in the shared annotation scheme.


## How to cite

If you use this data in your work please cite
> Gorzoni, G., Masini, F., & Pannitto, L. (2025). NPN_dataset (Version 1.0.0) [Data set]. https://github.com/GretaGorzoni00/NPN_dataset

```
@misc{Gorzoni_NPN_dataset_2025,
  author       = {Gorzoni, Greta and Pannitto, Ludovica and Masini, Francesca},
  title        = {{NPN Dataset}},
  year         = {2026},
  month        = gen,
  doi          = {10.5281/zenodo.18268134},
  url          = {https://github.com/GretaGorzoni00/NPN_dataset},
  howpublished = {Zenodo},
}
```

## References

- Masini, Francesca (2024) NPN discontinuous reduplications in Italian: dataset. Univesity of Bologna. DOI [10.6092/unibo/amsacta/7489](https://doi.org/10.6092/unibo%2Famsacta%2F7489)
- [CORIS 2021, a 165Mw reference corpus of contemporary written Italian](https://corpora.ficlit.unibo.it/TCORIS/)

## Changelog

* 2026-02-20:
  * minor change to distractor item, v1.0.1 released
* 2026-01-15:
  * first release

-----

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

<!-- [![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa] -->

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://licensebuttons.net/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
