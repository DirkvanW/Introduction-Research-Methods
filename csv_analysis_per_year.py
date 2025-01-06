import csv
from collections import defaultdict

with open('pg_catalog.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    languages_by_year = defaultdict(lambda: defaultdict(int))
    all_years = set()
    all_languages = set()
    
    # Skip header
    next(csv_reader)
    
    for row in csv_reader:
        year = int(row[2].split("-")[0])
        row_languages = [lang.strip() for lang in row[4].split(";")]
        if year != 2025:
            for language in row_languages:
                languages_by_year[year][language] += 1
                all_languages.add(language)
                all_years.add(year)

    # Write to CSV
    with open('language_analysis_by_year.csv', 'w', newline='', encoding='utf-8') as output_file:
        csv_writer = csv.writer(output_file)
        
        # Create header with all years
        years = sorted(list(all_years))
        header = ['Language'] + [str(year) for year in years]
        csv_writer.writerow(header)
        
        # Write data for each language
        for language in sorted(all_languages):
            row = [language]
            for year in years:
                row.append(languages_by_year[year][language])
            csv_writer.writerow(row)