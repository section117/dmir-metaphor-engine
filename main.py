from search import multi_search
from ui import get_search_results_table

def take_inputs():
    mode = int(input('Enter search mode: '))
    search_term = input('Enter search query: ')

    return mode, search_term


def transform_results(results):
    total_matches = results['total']['value']
    documents = [i['_source'] for i in results['hits']]

    table_rows = []
    for doc in documents:
        row = [
            doc['poem_name'],
            doc['poet'],
            doc['published_year'],
            doc['metaphor_line'],
            doc['metaphor_terms'],
            doc['source_domain'],
            doc['target_domain'],
            doc['interpretation'],
        ]
        table_rows.append(tuple(row))

    return total_matches, table_rows


def main():
    mode, search_term = take_inputs()
    results = multi_search(search_term, mode)

    total_matches, table_rows = transform_results(results)
    results_table = get_search_results_table(table_rows)
    results_table.mainloop()


main()
