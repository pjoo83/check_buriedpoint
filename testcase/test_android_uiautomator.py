from Base.get_driver import GetDriver_u2
from Base.init_driver import init_driver_android_ui2
from PagesUI.page_element_android import CommonElementAndroid
import pytest


@pytest.mark.usefixtures('driver_setup')
class test_android:
    def __init__(self):
        self.driver = GetDriver_u2().create_driver(init_driver_android_ui2())
        self.el = CommonElementAndroid()

    def test01_star_app(self):
        self.driver.open_app('com.starmakerinteractive.starmaker')
        if self.driver.exist_element(self.el.party_img):
            self.driver.click_on_element(self.el.back_button)

    def test02_live(self):
        """
        直播
        """
        self.driver.click_on_element(self.el.page_party)
        self.driver.click_on_element(self.el.live)
        self.driver.click_on_element(self.el.live_select)
        self.driver.phone_sleep(4)
        if self.driver.get_element(self.el.live_loading):
            self.driver.click_on_element(self.el.back_button)
            self.driver.click_on_element(self.el.live_select)
        self.driver.wait_dis_click(self.el.live_anchor_follow)
        self.driver.scroll_to_ori(orientation='hr')
        self.driver.phone_sleep(1)
        self.driver.scroll_to_ori(orientation='hl')
        self.driver.click_on_element(self.el.live_msg)
        self.driver.click_on_element(self.el.live_send_msg)
        self.driver.click_on_element(self.el.back_button)
        self.driver.click_on_element(self.el.live_share)
        self.driver.click_on_element(self.el.back_button)
        self.driver.click_on_element(self.el.live_gift)
        self.driver.click_on_element(self.el.gift_send)
        if self.driver.wait_e_dis_appear(self.el.insufficient_balance):
            self.driver.times_click_on_element(self.el.back_button, times=2)
        self.driver.click_on_element(self.el.back_button)

    def test03_search(self):
        """
        搜索
        """
        self.driver.click_on_element(self.el.page_party)
        self.driver.click_on_element(self.el.search_button)
        self.driver.sent_txt_by_selector(self.el.search_text, '為你寫下這首情歌')
        self.driver.wait_dis_click(self.el.search_result)
        self.driver.wait_dis_click(self.el.search_select)
        self.driver.times_click_on_element(self.el.back_button, 2)

    def test04_ktv(self):
        """
        KTV
        """
        self.driver.click_on_element(self.el.ktv_tab)
        self.driver.click_on_element(self.el.page_party)
        self.driver.click_on_element(self.el.ktv_page)
        self.driver.click_on_element(self.el.ktv_tab)
        self.driver.click_on_element(self.el.ktv_room_select)
        self.driver.wait_dis_click(self.el.ktv_room_owner)
        self.driver.wait_dis_click(self.el.ktv_room_homeowner)
        self.driver.click_on_element(self.el.ktv_follow)
        self.driver.click_on_element(self.el.ktv_follow)
        self.driver.click_on_element(self.el.ktv_cancel_follow)
        self.driver.click_on_element(self.el.back_button, times=2)
        self.driver.click_on_element(self.el.ktv_share)
        self.driver.click_on_element(self.el.back_button)
        self.driver.click_on_element(self.el.live_gift)
        self.driver.click_on_element(self.el.gift_send)
        if self.driver.wait_e_dis_appear(self.el.insufficient_balance):
            self.driver.times_click_on_element(self.el.back_button, times=2)
        self.driver.click_on_element(self.el.back_button)

    def test05_msg_chat_page(self):
        """
        聊天-推荐关注
        """
        self.driver.click_on_element(self.el.chat_page)
        self.driver.wait_e_dis_appear(self.el.chat_msg)
        if self.driver.wait_e_dis_appear(self.el.chat_msg_recommend) is False:
            self.driver.scroll_to_ori('down')
        self.driver.click_on_element(self.el.chat_msg_recommend)
        self.driver.click_on_element(self.el.back_button)
        self.driver.click_on_element(self.el.chat_msg_recommend_follow)

    def test06_msg_follow_page(self):
        """
        聊天-关注页
        """
        self.driver.click_on_element(self.el.chat_follow_page)
        for i in range(100):
            if self.driver.exist_element(self.el.chat_follow_recommend) or \
                    self.driver.exist_element(self.el.chat_follow_nothing):
                break
            else:
                self.driver.scroll_to_ori('up')
        self.driver.click_on_element(self.el.chat_follow_recommend_select)
        self.driver.click_on_element(self.el.back_button)
        self.driver.click_on_element(self.el.chat_follow_recommend_follow)
        self.driver.click_on_element(self.el.chat_follow_recommend_follow)

    def test07_find_friend(self):
        """
        好友搜索
        """
        self.driver.click_on_element(self.el.find_friend)
        self.driver.click_on_element(self.el.add_friend)
        if self.driver.exist_element(self.el.find_friend_vicinity):
            self.driver.click_on_element(self.el.find_friend_vicinity)
        self.driver.click_on_element(self.el.find_friend_select)
        self.driver.click_on_element(self.el.back_button)
        self.driver.click_on_element(self.el.find_friend_follow)
        self.driver.times_click_on_element(self.el.back_button, 2)

    def test08_notice_room(self):
        """
        消息通知页房间
        """
        self.driver.click_on_element(self.el.notice_page)
        if self.driver.exist_element(self.el.notice_room) is False:
            self.driver.scroll_to_ori('down')
        self.driver.wait_e_dis_appear(self.el.notice_room)
        self.driver.click_on_element(self.el.notice_room_click)
        self.driver.click_on_element(self.el.back_button)

    def test09_song(self):
        """
        演唱页面
        """
        self.driver.click_exist_element(self.el.page_song)
        self.driver.click_exist_element(self.el.song_select)
        self.driver.click_exist_element(self.el.back_button)
        self.driver.click_exist_element(self.el.song_sing_btn)

        self.driver.click_exist_element(self.el.song_know)
        self.driver.click_exist_element(self.el.song_part)
        self.driver.phone_sleep(5)
        self.driver.click_exist_element(self.el.song_ready)
        self.driver.swipe_ext_dis('up', times=2)
        self.driver.wait_dis_click(self.el.song_sure)
        self.driver.wait_dis_click(self.el.song_next)
        if self.driver.exist_element(self.el.song_attention):
            self.driver.times_click_on_element(self.el.back_button, 3)
            self.test09_song()
        else:
            self.driver.click_on_element(self.el.song_save)
            self.driver.wait_dis_click(self.el.song_to_publish)
            self.driver.wait_dis_click(self.el.song_publish)
            self.driver.click_on_element(self.el.song_complete_publish)
            self.driver.click_on_element(self.el.back_button)

    def test10_rank(self):
        """
        排行榜
        """
        self.driver.click_on_element(self.el.page_song)
        for i in range(2):
            self.driver.swipe_e(x1=755, y1=742, x2=2, y2=742)
        self.driver.wait_dis_click(self.el.rank_navigation)
        self.driver.wait_dis_click(self.el.rank_detail_song)
        self.driver.wait_dis_click(self.el.song_know)
        self.driver.times_click_on_element(self.el.back_button, 2)
        self.driver.click_on_element(self.el.rank_detail_song)
        self.driver.times_click_on_element(self.el.back_button, 2)

    def test11_ugc(self):
        """
        广场页面
        """
        self.driver.click_on_element(self.el.page_dynamic)
        self.driver.click_on_element(self.el.page_disc)
        self.driver.click_exist_element(self.el.dynamic_click)
        self.driver.click_on_element(self.el.dynamic_user)
        self.driver.click_on_element(self.el.back_button)

        self.driver.click_on_element(self.el.dynamic_follow)
        self.driver.click_on_element(self.el.dynamic_like)
        self.driver.click_on_element(self.el.dynamic_comment)
        self.driver.click_on_element(self.el.back_button, times=2)
        self.driver.click_on_element(self.el.dynamic_gift)
        self.driver.click_on_element(self.el.back_button, times=2)
        self.driver.click_on_element(self.el.dynamic_share)
        self.driver.click_on_element(self.el.back_button)
        self.driver.long_click_on_element(self.el.dynamic_voice)
        self.driver.click_on_element(self.el.back_button)

    def test12_ugc_detail(self):
        """
        广场的详情页
        """
        self.driver.click_on_element(self.el.page_dynamic)
        self.driver.click_on_element_offset(self.el.dynamic_detail)
        self.driver.click_exist_element(self.el.dynamic_detail_like)
        self.driver.click_on_element(self.el.dynamic_detail_follow)
        self.driver.click_on_element(self.el.dynamic_detail_comment)
        self.driver.click_on_element(self.el.back_button)
        self.driver.click_exist_element(self.el.dynamic_detail_gift)
        self.driver.click_on_element(self.el.back_button)
        self.driver.click_on_element(self.el.dynamic_detail_share)
        self.driver.click_on_element(self.el.back_button)
        self.driver.long_click_on_element(self.el.dynamic_detail_voice)
        self.driver.click_on_element(self.el.back_button, times=2)

    def test_button(self):
        # self.driver.times_click_on_element(self.el.ktv_tab, 1)
        self.driver.click_on_element(self.el.song_complete_publish)
        # self.driver.swipe_e(x1=755, y1=742, x2=2, y2=742)
        # self.driver.long_click_on_element(self.el.dynamic_voice)
    #
    # def test_get_request(self):
    #     interfaces = device.interfaces()  # 获取设备上的所有接口信息
    #     print("Interfaces:")
    #     for interface in interfaces:
    #         print(interface)


test_android().test_button()
