import logging
import time

# 创建logger对象
logger = logging.getLogger('check_BuriedPoint')

# 设置日志等级
# 创建时间单位

time = time.strftime('%Y年%m月%d日 %H点-%M分-%S秒', time.localtime(time.time()))

print(time, "开始测试！！！！！！！！！")
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=f'../logs/{time}安卓端埋点错误问题日志.log',
                    filemode='w', encoding='utf-8')
