#!/bin/env python3

with open('../aiotgm/client.py') as r:
    lines = r.readlines()

import re

ln = 0

def get_params(methods: str, match: str) -> dict[str, str]:
    global ln
    matched_empty_dict = re.match(r'\s*params\s*=\s*\{\s*\}\s*\n', lines[ln])
    matched_dict = re.match(r'\s*params\s*=\s*\{\s*\n', lines[ln])
    if matched_empty_dict:
        print(match)
    if matched_dict:
        print(match)
    else:
        raise Exception(match, lines[ln])


def main():
    global ln
    methods = {}
    for line in lines:
        mached_method = re.match(r'\s{4}async\s*def\s*([^_]\w*)', line)
        if mached_method:
            match = mached_method.group(1)
            if match in ('long_polling', ' _process_update'):
                continue
            methods[match] = {'params': None, 'return': None}
            get_params(methods, match)
        ln += 1

main()