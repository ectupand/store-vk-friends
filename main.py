from constants import TOKEN, USER_ID
from store.database import Database
from store.new_frens_check import NewFrensChecker
from vk_api_accessor.accessor import VkApiAccessor


if __name__ == "__main__":
    accessor = VkApiAccessor(access_token=TOKEN, user_id=USER_ID)
    actual_friends_count, friends_list = accessor.get_friends_list()
    checker = NewFrensChecker(actual_friends_count)
    checker.check_for_new_friends()
    #if checker.has_new == 1:
    database = Database(friends_list)
    database.clear_table()
    database.store()
