from appium.webdriver.common.mobileby import MobileBy


class CommonElementAndroid:
    def __init__(self):
        # 登录
        self.login = (MobileBy.XPATH, '//*[@resource-id="com.starmakerinteractive.starmaker:id/tv_login_guide"]')
        self.more_login = (MobileBy.XPATH, '//*[@resource-id="com.starmakerinteractive.starmaker:id/btn_more_ways"]')
        self.select_email = (MobileBy.XPATH, '//*[@resource-id="com.starmakerinteractive.starmaker:id/txt_anchor"]')
        self.select_use = (MobileBy.XPATH, '//*[@resource-id="com.starmakerinteractive.starmaker:id/ll_user1"]')
        self.home_page = (MobileBy.XPATH, '//*[@text="房间"]')

        # 退出
        self.page_my = (MobileBy.XPATH, '//*[@content-desc="main_tab_me"]/android.widget.FrameLayout[1]')
        self.settings = (MobileBy.XPATH, '//*[@resource-id="com.starmakerinteractive.starmaker:id/rcy_content'
                                         '"]/android.widget.FrameLayout[2]')
        self.logout = (MobileBy.XPATH, '//*[@resource-id="com.starmakerinteractive.starmaker:id/btn_settings_logout"]')
        self.quit = (MobileBy.XPATH, '//*[@text="登出"]')

        # 直播部分=======================================================================================================
        self.live = 'x,//*[@text="直播"]'
        # 热门直播
        self.select_first_live = (MobileBy.XPATH, '//*[@resource-id="com.starmakerinteractive.starmaker:id'
                                                  '/live_hall_recycler_view"]/android.widget.RelativeLayout['
                                                  '1]/android.widget.RelativeLayout[2]/android.widget.FrameLayout[1]')
        # 热门直播
        self.hot_live = '//*[@text="热门直播"]'
