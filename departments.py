from employer import list_employers

list_departments = [
    {
        'IT': list(filter(lambda item: item if 'Programmer' in item['job'] else None, list_employers)),
        'HR': list(filter(lambda item: item if 'Researcher' in item['job'] else None, list_employers)),
    },
]
