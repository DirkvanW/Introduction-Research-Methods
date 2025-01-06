import csv

with open('pg_catalog.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    all_languages = {}
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            row_languages = row[4].split(";")
            row_languages = [j.strip() for j in row_languages]
        
            for language in row_languages:
                all_languages.setdefault(language, [0, 0])
                if int(row[2].split("-")[0]) < 2010:
                    all_languages[language][0] += 1
                    line_count += 1
                if int(row[2].split("-")[0]) >= 2010:
                    all_languages[language][1] += 1
                    line_count += 1
    print(all_languages)
    
    with open('language_analysis.csv', 'w', newline='', encoding='utf-8') as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerow(['Language', 'Pre-2010 Count', 'Post-2010 Count'])
        for language, counts in all_languages.items():
            csv_writer.writerow([language, counts[0], counts[1]])
