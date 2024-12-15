# General Information
This study analyses the linguistic diversity in Project Gutenberg's digital library collection over time, specifically examining changes in the proportion of English versus non-English books before and after 2010. The research aims to understand how increased internet penetration in non-English speaking countries may have influenced the linguistic composition of digital preservation efforts.

# Background Information
Several studies have examined linguistic diversity in digital libraries and Project Gutenberg specifically:

1. Lebert, M. (2008) explored multilingualism on the web and Project Gutenberg's early efforts at linguistic diversification, providing important historical context for understanding the evolution of digital preservation efforts.

2. Gerlach, M., & Font-Clos, F. (2020) analysed a curated Project Gutenberg database, revealing a strong bias toward Western languages, with English comprising 81% of all books. Their work established baseline metrics for understanding linguistic representation in digital libraries.

# Research Question and Hypotheses

## Research Question
Is there a difference in the proportion of English versus non-English books added to Project Gutenberg before and after 2010?

## Hypothesis
The proportion of non-English books added to Project Gutenberg in the post-2010 period is higher than in the pre-2010 period. This hypothesis is based on several factors:
- An increased focus and accessibility in digital preservation efforts for non-English books in the English speaking community
- The diminishing pool of undigitised English public domain books
- Project Gutenberg's growing visibility and reach in non-English communities

# Method
The study utilises The Project Gutenberg Catalog Metadata in Machine-Readable Format, freely available from their website (https://www.gutenberg.org/ebooks/offline_catalogs.html#the-project-gutenberg-catalog-metadata-in-machine-readable-format) under their license (https://www.gutenberg.org/policy/license.html). The analysis focuses on two key metadata fields:
- Date of addition to the Gutenberg Catalog
- Document language

Data processing involves:
1. Parsing .rdf files using Python
2. Extracting and categorising language and date information
3. Error handling for missing fields to prevent bias
4. Analysis of language distribution pre/post-2010

# Citations
Gerlach, M., & Font-Clos, F. (2020). A Standardized Project Gutenberg Corpus for Statistical Analysis of Natural Language and Quantitative Linguistics. Entropy, 22(1), 126. https://doi.org/10.3390/e22010126

Lebert, M. (2008). Multilingualism on the Web. Project Gutenberg. http://www.gutenberg.org/etext/27028
