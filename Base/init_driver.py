# 启动WDA命令:  tidevice -u 00008110-0006616A0AD9401E wdaproxy -B  com.chhhhhhh.WebDriverAgentRunner.xctrunner --port 8100
# 查询 UDID  tidevice list
# 查询app名 tidevice applist
# iphone 8p id  038354c675cac77949c24141797d17ec137091da
# iphone 14 id
# IO初始化配置  00008110-0006616A0AD9401E
import uiautomator2 as u2


def init_driver_ios():
    desired_caps = {
        "platformName": "IOS",
        "appium:platformVersion": "15.6.1",
        "appium:deviceName": "iphone 8 plus",
        "appium:udid": "00008110-0006616A0AD9401E",
        "appium:bundleId": "com.starmakerapp.starmaker",
        "appium:automationName": "XCUITest",
        "appium:noReset": False,
        "appium:webDriverAgentUrl": "http://127.0.0.1:8100",
        "appium:usePrebuiltWDA": "false",
        "appium:useXctestrunFile": "false",
        "appium:skipLogCapture": "true",
        # "appium:fullReset":True,
        # "app":r"D:\project\BuriedPoint_check\StarMaker_Develop_8.65.0_802308282259_ebb5501718.ipa"
    }
    return desired_caps


# 安卓初始化配置
def init_driver_android_appium():
    desired_caps = {
        "platformName": "Android",
        "appium:platformVersion": "10",
        "appium:appPackage": "com.starmakerinteractive.starmaker",
        "appium:automationName": "UiAutomator2",
        "appium:noReset": True,
        # "appium:appActivity": "com.ushowmedia.starmaker.activity.MainActivity",
        "appium:appActivity": "com.ushowmedia.starmaker.splash.SplashActivity",
        "appium:deviceName": "127.0.0.1:62001",
        "skipServerInstallation": "false",
        'settings[waitForIdleTimeout]': 100
    }
    return desired_caps


def init_driver_android_ui2():
    device = u2.connect_usb('b7924af6')
    # driver = d.app_start('com.starmakerinteractive.starmaker')
    return device
