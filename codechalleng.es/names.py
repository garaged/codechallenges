NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return the modified names sequence"""
    return [i.title() for i in set(names)]

def sort_by_surname_desc(names):
    names = dedup_and_title_case_names(names)
    return sorted(names, key=lambda surname: surname.split()[1:])[::-1]


def shortest_first_name(names):
    names = dedup_and_title_case_names(names) 
    return min(sorted(names, key=lambda names: names.split(maxsplit=1))).split()[0]
