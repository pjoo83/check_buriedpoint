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

        # 通用
        self.back_button = 'id,com.android.systemui:id/back'
        self.insufficient_balance = 'x,//*[@text="账户余额"]'
        self.page_party = 'x,//*[@text="派对"]'

        # 直播部分=======================================================================================================
        self.live = 'x,//*[@text="直播"]'
        # 热门直播
        self.live_select = 'x,//*[@resource-id="com.starmakerinteractive.starmaker:id/live_hall_recycler_view' \
                           '"]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[' \
                           '2]/android.widget.FrameLayout[1] '
        # 等待
        self.live_loading = 'id,com.starmakerinteractive.starmaker:id/unstable_loading_avatar'
        # 直关注
        self.live_anchor_follow = 'id,com.starmakerinteractive.starmaker:id/live_rlyt_anchor_follow'
        # 评论
        self.live_msg = 'id,com.starmakerinteractive.starmaker:id/img_msg'
        self.live_meg_text = 'id,com.starmakerinteractive.starmaker:id/input_text_hint'
        self.live_send_msg = ' id,com.starmakerinteractive.starmaker:id/send_button'
        # 分享
        self.live_share = 'id,com.starmakerinteractive.starmaker:id/img_shareroom'
        self.live_share_friend = 'x,//*[@text="我的好友"]'
        # 送礼
        self.live_gift = 'id,com.starmakerinteractive.starmaker:id/img_gift'
        self.live_gift_send = 'id,com.starmakerinteractive.starmaker:id/btn_send_gift'

        # 搜索部分======================================================================================================
        self.search_button = 'id,com.starmakerinteractive.starmaker:id/search_switcher_icon'
        self.search_text = 'id,com.starmakerinteractive.starmaker:id/searchView'
        self.search_result = 'id,com.starmakerinteractive.starmaker:id/tv_name'
        self.search_select = 'x,//*[@resource-id="com.starmakerinteractive.starmaker:id/all_list"]/android.widget' \
                             '.RelativeLayout[1] '
