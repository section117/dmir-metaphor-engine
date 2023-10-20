from dataset import search, tokenize_text, stem_sinhala_text


def get_all():
    query = {
        'match_all': {}
    }
    return search(query)


def search_by_poem_name(search_term):
    query = {
        'match': {
            'poem_name': search_term
        }
    }
    return search(query)


def search_by_poet(search_term):
    query = {
        'match': {
            'poet': search_term
        }
    }
    return search(query)


def search_metaphors(search_term):
    query = {
        'match': {
            'metaphor_line': search_term
        }
    }
    return search(query)


def search_metaphors_with_stemming(search_term):
    stemmed_search_term = stem_sinhala_text(tokenize_text(search_term)[1])
    query = {
        'bool': {
            'should': [
                {'match': {'metaphor_line': {'query': search_term, 'boost': 2}}},
                {'match': {'metaphor_line_stemmed': {'query': stemmed_search_term, 'boost': 1}}}
            ]
        }
    }
    return search(query)


def search_by_source_domain(search_term):
    query = {
        'match': {
            'source_domain': {
                'query': search_term,
                'analyzer': 'plain_with_synonyms'
            }
        }
    }
    return search(query)


def search_by_target_domain(search_term):
    query = {
        'match': {
            'target_domain': {
                'query': search_term,
                'analyzer': 'plain_with_synonyms'
            }
        }
    }
    return search(query)


def multi_search(search_term: str, mode: int):
    if mode == 0:
        res = get_all()
    elif mode == 1:
        res = search_by_poem_name(search_term)
    elif mode == 2:
        res = search_by_poet(search_term)
    elif mode == 3:
        res = search_metaphors(search_term)
    elif mode == 4:
        res = search_metaphors_with_stemming(search_term)
    elif mode == 5:
        res = search_by_source_domain(search_term)
    elif mode == 6:
        res = search_by_target_domain(search_term)
    else:
        raise RuntimeError('Invalid search mode')

    return res
