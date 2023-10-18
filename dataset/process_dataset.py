from sinling import SinhalaStemmer

from dataset.elasticsearch_client import bulk_insert_documents, create_metaphor_index


def read_dataset(file_path):
    with open(file_path, mode='r', encoding='utf_8') as f:
        lines = f.readlines()[1:]
        lines = [_.rstrip() for _ in lines]

        metaphors = []
        for line in lines:
            m = line.split(',')
            if m[4] == 'yes':
                metaphors.append(m)

        return metaphors


def stem_sinhala_text(text_line: str):
    stemmer = SinhalaStemmer()
    text_line = text_line.lstrip().rstrip()
    words = text_line.split()
    stemmed_words = [stemmer.stem(i)[0] for i in words]
    return ' '.join(stemmed_words)


def convert_metaphor_to_elasticsearch_document(m):
    metaphor_line = m[3]
    source_domain = m[7]
    target_domain = m[8]

    document = {
        'poem_name': m[0],
        'poet': m[1],
        'published_year': m[2],
        'metaphor_line': metaphor_line,
        'metaphor_line_stemmed': stem_sinhala_text(metaphor_line),
        'metaphor_terms': m[6],
        'source_domain': source_domain,
        'source_domain_stemmed': stem_sinhala_text(source_domain),
        'target_domain': target_domain,
        'target_domain_stemmed': stem_sinhala_text(target_domain),
        'interpretation': m[9]
    }

    return document


def main():
    metaphors = read_dataset('dataset.csv')
    metaphor_documents = [convert_metaphor_to_elasticsearch_document(i) for i in metaphors]
    print(len(metaphor_documents), 'metaphor documents found.')

    create_metaphor_index()
    print(bulk_insert_documents(metaphor_documents))


main()
