#!/bin/env python3

if __name__ == '__main__':
    import re

    with open('../aiotgm/client.py') as r:
        lines = r.readlines()

    is_not_none = re.compile(r"if\s*(.*?)\s*is\s*not\s*None\s*:\s*params\[\s*'(.*?)'\s*\]\s*=\s*(.*)\n*")
    is_params = re.compile(r"\s*'(.*?)'\s*:\s*([^,]*)\s*,*\s*\n")

    errors = []
    corrects = []
    for line in lines:
        match_is_none = is_not_none.search(line)
        if match_is_none:
            group = match_is_none.group(1, 2, 3)
            if not (group[0].replace('self.', '') == group[1] == group[2].replace('self.', '')):
                errors.append((group[0], group[1], group[2]))
            else:
                corrects.append((group[0], group[1], group[2]))
        match_is_params = is_params.match(line)
        if match_is_params:
            group = match_is_params.group(1, 2)
            if not (group[0]) == group[1]:
                errors.append((group[0], group[1]))

    print('errors are:', errors)
    print('len() of correct is:', corrects, len(corrects))

