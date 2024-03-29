#!/bin/env python3

if __name__ == '__main__':
    import logging
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    logger.addHandler(handler)

    while True:
        logger_level = input('Do you want to use logger.level INFO? (Y) or DEBUG (n) ')

        if logger_level.lower() in ('y', str()):
            logger.setLevel(20)
            break
        elif logger_level.lower() == 'n':
            logger.setLevel(10)
            break

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
            logger.debug(line)
            group = match_is_none.group(1, 2, 3)
            if not (group[0].replace('self.', '') == group[1] == group[2].replace('self.', '')):
                logger.debug('is wrong')
                errors.append((group[0], group[1], group[2]))
            else:
                logger.debug('is correct')
                corrects.append((group[0], group[1], group[2]))
        match_is_params = is_params.match(line)
        if match_is_params:
            logger.debug(line)
            group = match_is_params.group(1, 2)
            if not (group[0]) == group[1]:
                logger.debug('is wrong')
                errors.append((group[0], group[1]))
            else:
                logger.debug('is correct')
                corrects.append((group[0], group[1]))

    logger.info('len() of errors are: %s' % len(errors))
    logger.info('len() of correct is: %s' % len(corrects))
