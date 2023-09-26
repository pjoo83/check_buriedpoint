from appium.webdriver.common.mobileby import MobileBy


class CommonElementIos:
    def __init__(self):
        # 底部登录
        self.login = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="登录/注册"]')
        # 使用邮箱
        self.use_email = (MobileBy.XPATH, '//*[@label="使用邮箱"]')
        # 点击快捷登录
        self.quick_login = (MobileBy.XPATH, '//*[@label="keler122@sm.com"]')
        # 关闭弹窗
        self.close_popup = (MobileBy.XPATH, '//*[@label="icon popup close"]')
        # 我的页面
        self.my = (MobileBy.XPATH, '//XCUIElementTypeTabBar[@name="标签页栏"]/XCUIElementTypeButton[5]')
        # 设置
        self.setting = (MobileBy.XPATH, '//*[@label="设置"]')
        # 登出
        self.log_out = (MobileBy.XPATH, '//*[@label="登出"]')
        # 退出
        self.quit = (MobileBy.XPATH, '//*[@label="退出"]')

        # 直播部分--------------------------------------------------------------------------------------------------------
        self.room_page = (MobileBy.XPATH, '//XCUIElementTypeTabBar[@name="标签页栏"]/XCUIElementTypeButton[1]')
        self.live_tittle = (MobileBy.XPATH, '//*[@label="直播"]')
        # 选择推荐位第一个
        self.first_recommend = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="推荐"])[6]')
        # 热门tab
        self.hot_tab = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="热门"])[2]')
        # 评论按钮
        self.comment_button = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="sm ktv comment white"]')
        self.send_msg = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Send"]')
        self.close_keyboard = (MobileBy.XPATH, '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other['
                                               '1]/Other[1]/ScrollView[1]/Other[1]/ScrollView[1]/Other[1]/Other[3]')
        # 热门直播
        self.hot_live = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="热门直播"]')
        # 分享
        self.share_live = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="room btn share"]')
        self.share_to = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="分享到"]')
        self.share_more = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="更多"]')
        self.quit_share = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="关闭"]')
        # 送礼按钮
        self.giving_gifts = (MobileBy.XPATH, '//XCUIElementTypeApplication['
                                             '@name="StarMaker"]/XCUIElementTypeWindow/XCUIElementTypeOther'
                                             '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                             '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                             '/XCUIElementTypeScrollView/XCUIElementTypeOther'
                                             '/XCUIElementTypeScrollView/XCUIElementTypeOther['
                                             '1]/XCUIElementTypeOther[8]/XCUIElementTypeOther[2]')

        self.give_button = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="live icon menu"]')

        self.close_gifts = (MobileBy.XPATH, '//XCUIElementTypeApplication['
                                            '@name="StarMaker"]/XCUIElementTypeWindow/XCUIElementTypeOther'
                                            '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                            '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                            '/XCUIElementTypeScrollView/XCUIElementTypeOther'
                                            '/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther['
                                            '7]/XCUIElementTypeOther[2]')
        # 余额不足
        self.balance_insufficient = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="账户余额"]')
        # 余额不足页面得返回按钮
        self.back_of_balance =(MobileBy.XPATH, '//XCUIElementTypeApplication['
                                               '@name="StarMaker"]/XCUIElementTypeWindow/XCUIElementTypeOther'
                                               '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                               '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther['
                                               '2]/XCUIElementTypeOther['
                                               '2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                               '/XCUIElementTypeOther/XCUIElementTypeWebView/XCUIElementTypeWebView'
                                               '/XCUIElementTypeWebView/XCUIElementTypeOther/XCUIElementTypeOther'
                                               '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]')

        # 关注
        self.follow_img = (MobileBy.XPATH, '//XCUIElementTypeApplication['
                                           '@name="StarMaker"]/XCUIElementTypeWindow/XCUIElementTypeOther'
                                           '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                           '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                           '/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeScrollView'
                                           '/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther['
                                           '1]/XCUIElementTypeImage[2] '
                           )
        self.follow_button = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="关注"]')
        # 退出直播
        self.quit_live = (MobileBy.XPATH, '//*[@label="icon party close title"]')

        # 搜索-----------------------------------------------------------------------------------------------------------
        self.search_button = (MobileBy.XPATH, '//*[@label="icon navi search"]')
        # 输入内容
        self.input_search = (MobileBy.XPATH, '//*[@label=""]')
        # 点击搜索
        self.search_key = (MobileBy.XPATH, '//*[@label="search"]')
        # 选择第一个结果
        self.select_song = (MobileBy.XPATH, '//*[@label="為你寫下這首情歌"]')

        # KTV页面--------------------------------------------------------------------------------------------------------
        self.ktv_tab = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="卡拉OK"])[3]')
        #  一起唱歌
        self.sing_together = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="一起唱歌"])[1]')
        # ktv列表
        self.ktv_list = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="一起唱歌"])[2]')
        # 分享
        self.share_ktv = (MobileBy.XPATH, '//*[@label="ktv room top share"]')
        # ktv关注用户
        self.click_tittle = (MobileBy.XPATH, '//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other['
                                             '1]/Other[3]/Other[1]/Other[1]/Image[1]')
        # 选择房主
        self.click_homeowner = (MobileBy.XPATH, '//*[@label="房主"]')
        # 关注

        self.follow_homeowner = (MobileBy.XPATH, '//*[@label="关注"]')
        # 送礼
        self.send_gift = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="room bottom gift"]')
        # 选择里哦呜
        self.select_gift = (MobileBy.XPATH, '//*[@label="魔法棒"]')
        # 赠送
        self.click_give = (MobileBy.XPATH, '//*[@label="赠送"]')

        # song部分-------------------------------------------------------------------------------------------------------
        self.room_setting = (MobileBy.XPATH, '//Table/Other[1]/Other[1]/Other[2]/Other[1]/Other[1]')
        # 进房
        self.my_room = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="进入我的房间"]')
        # 切换类型
        self.change_room_type = (MobileBy.XPATH, '//Window/Other[2]/Other[1]/Other[1]/Other[1]/Other[1]/Other['
                                                 '1]/Other[3]/Other[1]/Other[1]/Other[3]')
        # 卡拉ok
        self.select_klok = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="卡拉OK"]')
