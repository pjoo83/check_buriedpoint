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

        # 通用==========================================================================================================
        self.back_button = 'id,com.android.systemui:id/back'
        self.insufficient_balance = 'x,//*[@text="账户余额"]'
        self.page_party = 'x,//*[@content-desc="main_tab_discovery"]'
        self.gift_send = 'id,com.starmakerinteractive.starmaker:id/btn_send_gift'

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

        # 搜索部分======================================================================================================
        self.search_button = 'id,com.starmakerinteractive.starmaker:id/search_switcher_icon'
        self.search_text = 'id,com.starmakerinteractive.starmaker:id/searchView'
        self.search_result = 'id,com.starmakerinteractive.starmaker:id/tv_name'
        self.search_select = 'x,//*[@resource-id="com.starmakerinteractive.starmaker:id/all_list"]/android.widget' \
                             '.RelativeLayout[1] '

        # KTV部分 ======================================================================================================
        self.ktv_page = 'x,//*[@text="歌房"]'
        self.ktv_tab = 'x,//*[@resource-id="com.starmakerinteractive.starmaker:id/tab_layout"]/android.widget' \
                       '.LinearLayout[1]/android.widget.FrameLayout[2] '
        self.ktv_room_select = 'id,com.starmakerinteractive.starmaker:id/room_bg'
        self.ktv_room_owner = 'id,com.starmakerinteractive.starmaker:id/room_owner_level'
        self.ktv_room_homeowner = 'id,com.starmakerinteractive.starmaker:id/rl_owner_container'
        self.ktv_follow = 'id,com.starmakerinteractive.starmaker:id/btn_follow'
        self.ktv_cancel_follow = 'id,com.starmakerinteractive.starmaker:id/common_dialog_btn_positive'
        self.ktv_share = 'id,com.starmakerinteractive.starmaker:id/player_act_share'
        self.ktv_gift = 'id,com.starmakerinteractive.starmaker:id/v_menu_send_gift'

        # friends部分===================================================================================================
        # 聊天页
        self.chat_page = 'x,//*[@content-desc="main_tab_message"]'
        self.chat_msg = 'x,//*[@resource-id="com.starmakerinteractive.starmaker:id/tab_layout"]/android' \
                        '.widget.LinearLayout[1]/android.widget.FrameLayout[2] '
        self.chat_msg_recommend = 'x,//*[@resource-id="com.starmakerinteractive.starmaker:id/recycler_view' \
                                  '"]/android.widget.RelativeLayout[7] '
        self.chat_msg_recommend_follow = 'x,//*[@resource-id="com.starmakerinteractive.starmaker:id/recycler_view' \
                                         '"]/android.widget.RelativeLayout[7]/android.widget.FrameLayout[2] '
        # 关注页
        self.chat_follow_page = 'x,//*[@resource-id="com.starmakerinteractive.starmaker:id/tab_layout"]/android' \
                                '.widget.LinearLayout[1]/android.widget.FrameLayout[1] '
        self.chat_follow_recommend = 'id,com.starmakerinteractive.starmaker:id/tv_title'
        self.chat_follow_recommend_select = 'x,//*[@resource-id="com.starmakerinteractive.starmaker:id/recycler_view' \
                                            '"]/android.widget.RelativeLayout[7] '
        self.chat_follow_recommend_follow = 'id,com.starmakerinteractive.starmaker:id/follow_icon'

        # 好友搜索
        self.find_friend = 'id,com.starmakerinteractive.starmaker:id/iv_create_conversation'
        self.add_friend = 'x,//*[@text="添加好友"]'
        self.find_friend_vicinity = 'id,com.starmakerinteractive.starmaker:id/btw_dialog_request'
        self.find_friend_select = 'x,//*[@resource-id="com.starmakerinteractive.starmaker:id/rv_find_friend"]/android' \
                                  '.widget.RelativeLayout[1] '
        self.find_friend_follow = 'x,//*[@resource-id="com.starmakerinteractive.starmaker:id/rv_find_friend"]/android' \
                                  '.widget.RelativeLayout[1]/android.widget.FrameLayout[2] '
