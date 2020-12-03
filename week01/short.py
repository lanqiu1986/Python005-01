import time
import logging
import os
from pathlib import Path

def short_func():
    print('life is short')

    #日志
    #取得当前日期，若当前没有此文件夹，创建文件夹，如果有进入
    #time.localtime()
    nowdate = time.strftime("%Y%m%d",time.localtime()) 
    my_file = "python"+nowdate
    path = Path('log/'+my_file)
    if not path.exists():
        os.makedirs(path)       
    
    #日志记录，保存位置设定
    filename = nowdate +'.log'
    logging.basicConfig(filename='log/'+my_file+'/'+filename,
                    level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s %(name)-8s %(levelname)-8s [line: %(lineno)d] %(message)s'
                    )
    logging.info('open short_func')


if __name__ == '__main__': 
    short_func()


