# General information, describing your project (i.e., the abstract)
This study analyses the number of English and non-English books added to the Project Gutenberg Catalog before and after the year 2010. It does this using the Project Gutenberg Catalog Metadata, from which the date of being indexed by Project Gutenberg and the document language are extracted, which are then counted and analysed. 

# Background information (list at least two studies that have looked at your topic, including correct referencing)
Gerlach, M., & Font-Clos, F. (2020). discusses the creation of a curated Project Gutenberg database. In their article they show the language distribution of this database. showing clear bias in favour of western languages, with English being the most common language by far, at 81% of all books. 

# Research question and hypotheses
## Research Question
What is the difference in the proportion of English versus non-English books added to Project Gutenberg before and after 2010?
## Hypothesis
The proportion of non-English books added to Project Gutenberg in the post-2010 period is higher than in the pre-2010 period. This can be caused by multiple things:
- An increased focus and increased accessibility in digital preservation efforts.
- As the number of English public domain books that have not been added to the Gutenberg Project Collection becomes smaller, adding non-English books will become more common comparatively.
- Increased internet access for non-English people leads to greater focus on non-English books.
- As the Gutenberg Project becomes larger in scale, the project has an easier time finding and being found in non-English communities.

# Method (including the dataset in use, sampling method etc.)
The dataset that will be used will be The Project Gutenberg Catalog Metadata in Machine-Readable Format, available freely on their website: (https://www.gutenberg.org/ebooks/offline_catalogs.html#the-project-gutenberg-catalog-metadata-in-machine-readable-format as allowed by their license: https://www.gutenberg.org/policy/license.html). This dataset includes the date that a book was orignally added to the Gutenberg Catalog, and the language of the document. These are avaiable in machine readable .rdf files. These will be parsed using a Python script that will count the Data and Language. This script will also discount and log any errors, such as missing date or language fields to prevent potential bias and for further investigation. 

# Citations
Gerlach, M., & Font-Clos, F. (2020). A Standardized Project Gutenberg Corpus for Statistical Analysis of Natural Language and Quantitative Linguistics. Entropy, 22(1), 126. https://doi.org/10.3390/e22010126 
