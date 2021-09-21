from selenium.webdriver.common.by import By

"""
通用text
"""
TEXT = '//*[@text="{}"]'


"""
滑动方向的取值范围
"""
DIRECTION_UP = 'up'
DIRECTION_DOWN = 'down'
DIRECTION_LEFT = 'left'
DIRECTION_RIGHT = 'right'

"""偏好选择页"""
# 标题, 文案: 你都喜欢听些什么音乐？
choice_title_text = (By.ID, 'com.xiaoma.music:id/tvTitle')

# 跳过按钮
choice_skip_btn = (By.ID, 'com.xiaoma.music:id/tvSkip')

"""首页"""
# 搜索
index_search_btn = (By.ID, 'com.xiaoma.music:id/tv_search')

# 在线音乐
index_online_music_btn = (By.XPATH, '//*[@text="在线音乐"]')

# 本地音乐
index_local_music_btn = (By.XPATH, '//*[@text="本地音乐"]')

# 我的音乐
index_my_music_btn = (By.XPATH, '//*[@text="我的音乐"]')

# 缩略播放器播放icon
index_thimb_icon = (By.ID, 'com.xiaoma.music:id/fragment_thumb_iv_status')

# 缩略播放器封面
index_thumb_cover_img = (By.ID, 'com.xiaoma.music:id/fragment_thumb_iv_cover')

# 缩略播放器歌名
index_thumb_info_text = (By.ID, 'com.xiaoma.music:id/fragment_thumb_tv_music_info')

# 推荐
index_recommendation_btn = (By.XPATH, '//*[@text="推荐"]')

# 排行榜
index_rank_btn = (By.XPATH, '//*[@text="排行榜"]')

# 分类
index_category_btn = (By.XPATH, '//*[@text="分类"]')

# 列表音乐封面(带倒影)
index_list_music_cover_img1 = (By.XPATH,
                               '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[]/android.widget.FrameLayout/android.widget.ImageView[1]')

# 列表音乐封面(不带倒影)
index_list_music_cover_img2 = (By.XPATH,
                               '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[]/android.widget.FrameLayout/android.widget.ImageView[2]')

# 滑动条
index_scroll_bar = (By.ID, 'com.xiaoma.music:id/scroll_bar')

# 断网

"""搜索页面"""
index_network_retry_btn = (By.XPATH, '//*[@text="重新加载"]')

# 语音搜索
search_voice_search_btn = (By.ID, 'com.xiaoma.music:id/tv_start_voice_search')

# 搜索框
search_input_search_edit = (By.ID, 'com.xiaoma.music:id/et_normal_content')

# 立即搜索
search_now_search_btn = (By.ID, 'com.xiaoma.music:id/search_view_search_now_btn')

# 语音搜索状态 左边动画
search_voice_recording_img = (By.ID, 'com.xiaoma.music:id/iv_recording_left')

# '搜索历史'标题
search_history_search_title = (
    By.XPATH, '//*[@resource-id="com.xiaoma.music:id/rl_search_history"]/android.widget.TextView')

# '搜索历史'删除按钮
search_history_search_clear_btn = (By.XPATH, '//*[@resource-id="com.xiaoma.music:id/tv_clear"]')

# '搜索历史'搜索选项, 从1开始计数
search_history_search_btn = (
    By.XPATH, '//*[@resource-id="com.xiaoma.music:id/ll_search_history"]/android.widget.TextView[]')

# '大家都在搜'标题
search_hot_search_title = (By.XPATH, '//*[@text="大家都在搜"]')

# '大家都在搜'推荐选项, 从1开始计数
search_hot_search_btn = (By.XPATH, '//*[@resource-id="com.xiaoma.music:id/ll_recommend"]/android.widget.TextView[]')

"""分类页面"""
# 列表分类, 从1开始计数
category_list_item_text = (
    By.XPATH, '//*[@resource-id="com.xiaoma.music:id/fragment_category_rv"]/android.widget.TextView[]')

"""分类详情页面"""
# 列表音乐封面, 从1开始计数
category_detail_list_music_cover_img = (
    By.XPATH, '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[]/android.widget.ImageView')

"""我的音乐页面"""
# 我的收藏
my_music_collection_btn = (By.XPATH, '//*[@text="我的收藏"]')

# 播放历史
my_music_history_btn = (By.XPATH, '//*[@text="播放历史"]')

# 会员中心
my_music_vip_btn = (By.XPATH, '//*[@text="会员中心"]')

# 清空收藏
my_music_clear_collection_btn = (By.XPATH, '//*[@text="清空我的收藏"]')

# 清除历史记录
my_music_history_clear_history = (By.XPATH, '//*[@resource-id="com.xiaoma.music:id/tv_clear_all_history"]')

# 确认清除按钮
my_music_confirm_clear_btn = (By.XPATH, '//*[@resource-id="com.xiaoma.music:id/btn_confirm_sure"]')

# 取消清除按钮
my_music_cancel_clear_btn = (By.XPATH, '//*[@resource-id="com.xiaoma.music:id/btn_confirm_cancel"]')

# 默认空数据配图
my_music_null_img = (By.XPATH, '//*[@resource-id="com.xiaoma.music:id/iv_tips"]')

# 默认空数据文字(暂无数据)
my_music_null_text = (By.XPATH, '//*[@resource-id="com.xiaoma.music:id/tv_tips"]')

# 我的收藏 列表音乐的歌曲名
my_music_collection_list_music_song_name = (
    By.XPATH,
    '//*[@resource-id="com.xiaoma.music:id/rv_music_collect"]/android.widget.LinearLayout[]/android.widget.TextView')

# 我的收藏 列表音乐的封面
my_music_collection_list_music_cover = (
    By.XPATH,
    '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[]/android.widget.FrameLayout/android.widget.ImageView[2]')

my_music_collection_list_music_singer_name = (
    By.XPATH,
    '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[]/android.widget.FrameLayout/android.widget.TextView')

# 播放历史 列表音乐的歌曲名
my_music_history_list_music_song_name = (
    By.XPATH,
    '//*[@resource-id="com.xiaoma.music:id/rv_music_history"]/android.widget.LinearLayout[]/android.widget.TextView')

# 播放历史 列表音乐的封面
my_music_history_list_music_cover = (
    By.XPATH,
    '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[]/android.widget.FrameLayout/android.widget.ImageView[2]')

# 播放历史 列表音乐的专辑名
my_music_history_list_music_singer_name = (
    By.XPATH,
    '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[]/android.widget.FrameLayout/android.widget.TextView')

"""播放器页面"""
# 返回键缩略播放器歌名
player_back_btn = (By.XPATH, '//*[@resource-id="com.xiaoma.music:id/activity_player_back"]')

# 播放的歌曲名
player_song_name_text = (By.ID, 'com.xiaoma.music:id/tv_music_name')

# 收藏按钮
player_collection_btn = (By.XPATH, '//*[@resource-id="com.xiaoma.music:id/iv_favourite"]')

# 上一曲
player_last_song_btn = (By.XPATH, '//*[@resource-id="com.xiaoma.music:id/iv_previous"]')

# 播放键
player_play_btn = (By.XPATH, '//*[@resource-id="com.xiaoma.music:id/iv_play"]')

# 下一曲
player_next_song_btn = (By.XPATH, '//*[@resource-id="com.xiaoma.music:id/iv_next"]')

# 歌词按钮
player_lyric_btn = (By.XPATH, '//*[@resource-id="com.xiaoma.music:id/iv_lyric"]')

"""桌面页面"""

# 应用列表按钮
launcher_index_app_list_btn = (By.XPATH, '//*[@resource-id="com.xiaoma.launcher:id/iv_go_app_list"]')

# 桌面收藏按钮
launcher_index_collection_btn = (By.XPATH, '//*[@resource-id="com.xiaoma.launcher:id/iv_favourite"]')

# 桌面播放按钮
launcher_index_play_btn = (By.XPATH, '//*[@resource-id="com.xiaoma.launcher:id/iv_play"]')

# 桌面应用列表页面 音乐
launcher_app_list_music = (By.XPATH, '//*[@text="音乐"]')

# 桌面应用列表页面 车应用
launcher_app_list_app = (By.XPATH, '//*[@text="车应用"]')

"""车应用页面"""
# 打开音乐的按钮
app_open_music_btn = (By.XPATH, '//*[@text="音乐"]/../*[@resource-id="com.xiaoma.app:id/progressBtn"]')

