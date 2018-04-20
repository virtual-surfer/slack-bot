# coding=utf-8
import random
from service.twitter import twitter_service
from service import timeutil_service


# ######################### 処理実行時間一覧 #########################

# 前提 : batchは10分毎に起動される。2時~6時はツイート閲覧数少ないと見込んで処理しない。
# 本に関するつぶやき : 2時間ごと
# アンフォロー : 2日に1回 18時
# フォロー : 2日に1回 20時
# 安い本の紹介 : 2時間ごと
# 新着本の紹介 : 2時間ごと
# メンション返信(最適な本のレコメンド) : 適宜(TODO:1日の上限は設ける)

# ##################################################################

# ################## 各種変数(基本的にはここだけ触る) ##################

user_screen_name = 'lcai18chan'
max_follow_count_every_other_day = 100
max_unfollow_count_every_other_day = 30
follow_target_word_list = ['読書', 'ビジネス書', '本好き', 'Amazon', 'タイムセール', 'ブログ', 'Kindle', 'Amazonプライム',
                           '漫画', 'プログラミング', '本読む', 'book', '読書好き', 'Webデザイン', 'プログラミング初心者',
                           'Webエンジニア', '図書館', '世田谷', '下北沢', 'ITベンチャー', 'startup', '起業', '投資',
                           'デザイン', 'はてなブログ', 'Python', 'Ruby', 'Go', 'Java', 'Javascript', 'Node.js'
                           'React', 'Angular', 'AR', 'VR', '吉祥寺', '左利きのエレン', 'note', '女子高生社長'
                           '女子高生エンジニア', '女子高生デザイナー', '女子高生プログラマー']

# ##################################################################


def execute():
    current_hour = timeutil_service.current_datetime().hour
    # 2時~8時はおやすみ（処理しない）
    if 2 < current_hour < 8:
        return

    # 10分に1回 TODO:処理増えてきたら->自分にメンションが来ているかを確認してツイートタスクに詰める
    # 「メンションきているものにレスポンス文章作ってツイートする」タスクを1分間に1つぶやきの頻度で返す
    print('TODO')

    current_minute = timeutil_service.current_datetime().minute
    # 定期実行タスクに関しては0分~10分以外はおやすみ（処理しない）
    if 10 < current_minute <= 59:
        return

    # 偶数時間(フォロー処理時間以外)につぶやき(DB保存している女子高生のつぶやきでつぶやき時間の近いもの真似して投稿)
    if current_hour % 2 == 0 and current_hour != 18 and current_hour != 20:
        print('TODO')
    # 奇数時間につぶやき
    # done 適当にツイート検索して引用リツイート
    # TODO: 話題の本に関してのつぶやきの引用リツイート
    if current_hour % 2 != 0 and current_hour != 19:
        twitter_service.search_popular_tweet_and_retweet(user_screen_name, random.choice(follow_target_word_list))
    # 指定時間にセール情報と新着情報
    if current_hour == 11 or current_hour  == 15 or current_hour == 19:
        print('TODO')

    today = timeutil_service.current_datetime().day
    # 偶数日(2日に1回)はおやすみ（処理しない）
    if today % 2 == 0:
        return
    # done 自動アンフォロー機能
    if current_hour == 18:
        twitter_service.unfollow(user_screen_name, max_unfollow_count_every_other_day)
    # done  自動フォロー機能
    if current_hour == 20:
        twitter_service.search_follow(user_screen_name, random.choice(follow_target_word_list), max_follow_count_every_other_day)


execute()