import sys
import os
import logging
from common.settings import LOGGING_LEVEL

sys.path.append('../')

FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'client.log')

STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(FORMATTER)
STREAM_HANDLER.setLevel(logging.ERROR)

LOG_FILE = logging.FileHandler(PATH, encoding='utf8')
LOG_FILE.setFormatter(FORMATTER)

LOG = logging.getLogger('client')
LOG.addHandler(STREAM_HANDLER)
LOG.addHandler(LOG_FILE)
LOG.setLevel(LOGGING_LEVEL)

if __name__ == '__main__':
    LOG.debug('Отладочная информация')
