from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Base:
    def __init__(self, driver):
        self.driver = driver

    # 元素查找
    def base_find(self, loc, timeout=60, poll=0.5):
        if len(loc) > 2:
            try:
                return WebDriverWait(self.driver, timeout=timeout,
                                     poll_frequency=poll).until(
                    lambda x: self.driver.find_elements(loc[0], loc[1])[loc[2]])
            except IndexError:
                print("定位元素未找到" + str(loc))
        else:
            return WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=poll).until(ec.presence_of_element_located(loc),
                                                            message="定位元素未找到" + str(loc))

    # 点击方法
    def base_click(self, loc):
        el = self.base_find(loc)
        el.click()

    # 输入
    def base_input(self, loc, value):
        el = self.base_find(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)

    # 根据坐标滑动
    def base_swipe_coordinate(self, start_x, start_y, end_x, end_y, duration=0):
        # 获取屏幕尺寸
        windows_size = self.driver.get_window_size()
        x = windows_size["width"]
        y = windows_size["height"]
        self.driver.flick(start_x=x * start_x,
                          start_y=y * start_y,
                          end_x=x * end_x,
                          end_y=y * end_y)

    # 单次滑动
    def base_swipe_single(self, i):
        if i == 1:
            self.driver.execute_script('mobile: swipe', {'direction': 'up'})
        elif i == 2:
            self.driver.execute_script('mobile: swipe', {'direction': 'down'})
        elif i == 3:
            self.driver.execute_script('mobile: swipe', {'direction': 'left'})
        else:
            self.driver.execute_script('mobile: swipe', {'direction': 'right'})

    # 隐藏键盘
    def hide_keyboard(self):
        self.driver.hide_keyboard()

    # 显示等待
    def wait_time(self, loc):
        WebDriverWait(self.driver, 10, 0.5).until(ec.presence_of_element_located(loc))

    # 点击
    def click_advance(self, x1, y1, x2, y2, duration=3000):
        self.driver.tap([(x1, y1), (x2, y2)], duration)

    # 根据相对坐标点击
    def tapA(self):
        # 比例系数
        x = 542 / 1080
        y = 1362 / 2340
        # 获取新测试机屏幕宽、高
        w = self.driver.get_window_size()['width']
        h = self.driver.get_window_size()['height']
        # 屏幕宽高乘以A点的比例系数，即可得A点在新测试机上坐标
        self.driver.tap(x * w, y * h)

    # 滑动到指定元素
    def swipe_screen_until_to_element(self, locator):
        while True:
            try:
                self.driver.find_element(*locator)
                break
            except NoSuchElementException:
                self.swipe_random_down_distance()

    # 返回
    def base_back(self):
        self.driver.back()
