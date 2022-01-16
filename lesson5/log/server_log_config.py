import sys
import os
import logging
import logging.handlers
from common.settings import LOGGING_LEVEL
sys.path.append('../')

FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'server.log')

STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(LOGGING_LEVEL)
STREAM_HANDLER.setLevel(logging.ERROR)
LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf8', interval=1, when='D')
LOG_FILE.setFormatter(LOGGING_LEVEL)

LOG = logging.getLogger('server')
LOG.addHandler(STREAM_HANDLER)
LOG.addHandler(LOG_FILE)
LOG.setLevel(LOGGING_LEVEL)

if __name__ == '__main__':
    LOG.debug('Отладочная информация')