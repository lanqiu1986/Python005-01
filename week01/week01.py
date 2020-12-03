import short
import logging
short.short_func()


logging.basicConfig(filename='week1.log',
                    level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s %(name)-8s %(levelname)-8s [line: %(lineno)d] %(message)s'
                    )
logging.info('info mes')
