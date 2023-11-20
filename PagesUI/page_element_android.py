class CommonElementAndroid:
    def __init__(self):
        # 首页活动
        self.party_img = '//*[@resource-id="com.starmakerinteractive.starmaker:id/img_cover_2"]'
        # 通用==========================================================================================================
        self.back_button = 'id,com.android.systemui:id/back'
        self.insufficient_balance = 'x,//*[@text="账户余额"]'
        self.page_party = 'x,//*[@content-desc="main_tab_discovery"]'
        self.gift_send = 'id,com.starmakerinteractive.starmaker:id/btn_send_gift'
        self.page_song = 'x,//*[@content-desc="main_tab_sing"]/android.widget.FrameLayout[' \
                         '1]/android.widget.ImageView[1] '
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
        self.live_send_msg = 'id,com.starmakerinteractive.starmaker:id/btn_send'
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
        self.ktv_tab = 'x,//*[@text="派对"]'
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
        self.chat_follow_nothing = 'x,//*[@text="没有更多内容"]'
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

        # 通知页房间
        self.notice_page = 'x,//*[@resource-id="com.starmakerinteractive.starmaker:id/tab_layout"]/android.widget' \
                           '.LinearLayout[1]/android.widget.FrameLayout[3] '
        self.notice_room = 'x,//*[@resource-id="com.starmakerinteractive.starmaker:id/live_recommend_recycler_view"]'
        self.notice_room_click = 'x,//*[@resource-id="com.starmakerinteractive.starmaker:id' \
                                 '/live_recommend_recycler_view"]/android.widget.RelativeLayout[1] '

        # 点唱页部分=====================================================================================================
        self.song_select = 'x,//*[@resource-id="com.starmakerinteractive.starmaker:id/rcc_list"]/android.widget' \
                           '.RelativeLayout[1] '
        self.song_sing_btn = 'id,com.starmakerinteractive.starmaker:id/btn_sing'
        self.song_know = 'id,com.starmakerinteractive.starmaker:id/recording_headset_dialog_i_know_btn'
        self.song_part = 'x,//*[@text="唱片段"]'
        self.song_ready = 'id,com.starmakerinteractive.starmaker:id/button_record_play'
        self.song_next = 'x,//*[@resource-id="com.starmakerinteractive.starmaker:id' \
                         '/tv_next_baserecord_fragment_edit_btn"] '
        self.song_sure = 'x,//*[@resource-id="com.starmakerinteractive.starmaker:id/btn_ok"]'
        self.song_save = 'x,//*[@resource-id="com.starmakerinteractive.starmaker:id/publish_save_draft"]'
        self.song_attention = 'x,//*[@resource-id="com.starmakerinteractive.starmaker:id/common_dialog_title"]'
        self.song_to_publish = 'x,//*[@resource-id="com.starmakerinteractive.starmaker:id/lyt_publish_immediately"]'
        self.song_publish = 'x,//*[@resource-id="com.starmakerinteractive.starmaker:id/publish_post"]'
        self.song_complete_publish = 'x,//*[@text="完成"]'
        self.song_facebook_publish = 'x,//*[@text="创建帖子"]'
        self.song_facebook_cancel = 'x//*[@text="放弃"]'
        # 广场动态页=====================================================================================================
        self.page_dynamic = 'x,//*[@text="动态"]'
        self.page_disc = 'x,//*[@resource-id="com.starmakerinteractive.starmaker:id/sing_tab_layout"]/android.widget' \
                         '.LinearLayout[1]/android.widget.FrameLayout[2] '
        self.dynamic_click = 'x,//*[@resource-id="com.starmakerinteractive.starmaker:id/recycler_view"]/android.widget' \
                             '.LinearLayout[1]/android.view.ViewGroup[2]/android.widget.LinearLayout[1] '
        self.dynamic_user = 'id,com.starmakerinteractive.starmaker:id/common_user_avatar'
        self.dynamic_share = 'id,com.starmakerinteractive.starmaker:id/share_num_layout'
        self.dynamic_like = 'id,com.starmakerinteractive.starmaker:id/layout_like'
        self.dynamic_follow = 'id,com.starmakerinteractive.starmaker:id/new_v_follow'
        self.dynamic_comment = 'id,com.starmakerinteractive.starmaker:id/tv_comment_hint'
        self.dynamic_gift = 'id,com.starmakerinteractive.starmaker:id/tv_gift'
        self.dynamic_voice = 'id,com.starmakerinteractive.starmaker:id/iv_send_danmu'
        # 详情页
        self.dynamic_detail = 'id,com.starmakerinteractive.starmaker:id/ll_trend_function'
        self.dynamic_detail_follow = 'id,com.starmakerinteractive.starmaker:id/tv_follow'
        self.dynamic_detail_like = 'id,com.starmakerinteractive.starmaker:id/lottie_like_view'
        self.dynamic_detail_comment = 'id,com.starmakerinteractive.starmaker:id/layout_comment'
        self.dynamic_detail_gift = 'id,com.starmakerinteractive.starmaker:id/layout_gift'
        self.dynamic_detail_share = 'id,com.starmakerinteractive.starmaker:id/layout_share'
        self.dynamic_detail_voice = 'id,com.starmakerinteractive.starmaker:id/iv_send_danmu'

        # sing排行榜======================================================================================================
        self.rank_navigation = 'x,//*[@text="排行榜"]'
        self.rank_select = 'x,//*[@resource-id="com.starmakerinteractive.starmaker:id/recycler_view"]/android.widget' \
                           '.RelativeLayout[1]'
        self.rank_detail_song = 'x,//*[@text="唱"]'
