import subprocess
from time import ctime


def appium_start(host, port):
    """启动appium server"""
    bootstrap_port = str(port + 1)
    # /b表示后台运行命令行串口
    cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port)

    print('%s at %s' % (cmd, ctime()))
    subprocess.Popen(cmd, shell=True, stdout=open('../appium_log/' + str(port) + '.log', 'a'),
                     stderr=subprocess.STDOUT)


# 测试函数，在实际运行过程中可以注释
if __name__ == '__main__':
    host = '127.0.0.1'
    port = 4723
    appium_start(host, port)
