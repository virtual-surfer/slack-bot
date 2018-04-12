# coding=utf-8
from repository import common_repository
from entity.twitter_user_entity import TwitterUser


# 登録処理
def add_user(name, screen_name, image_link):
    # トランザクション開始
    session = common_repository.create_session()
    # user追加
    test_user = TwitterUser(user_name=name, user_screen_name=screen_name, profile_image_link=image_link)
    session.add(test_user)
    # 変更をコミット
    session.commit()


def add_users(users):
    # トランザクション開始
    session = common_repository.create_session()
    # bulkで一括user追加
    session.bulk_save_objects(
        [TwitterUser(user_name=user[0], user_screen_name=user[1], profile_image_link=user[2])
         for user in users], return_defaults=True)
    # 変更をコミット
    session.commit()


# 削除処理
def delete_user_by_id(twitter_id):
    # トランザクション開始
    session = common_repository.create_session()
    # 削除処理
    row = session.query(TwitterUser).filter_by(twitter_user_id=twitter_id).one()
    session.delete(row)
    # 変更をコミット
    session.commit()