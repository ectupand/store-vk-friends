from __future__ import annotations

import collections
from typing import Tuple, Any

import vk_api

from constants import FIELDS


class VkApiAccessor:
    def __init__(self, access_token: str, user_id: int):
        self.session = vk_api.VkApi(token=access_token)
        self.user_id = user_id
        self.friends_list = collections.defaultdict(lambda: 0)

    def get_friends_list(self) -> tuple[Any, Any]:
        response = self.session.method(
            "friends.get", {
                'user_id': self.user_id,
                'fields': FIELDS,
                }
        )
        self.friends_list = response['items']
        return response['count'], self.friends_list
