from __future__ import annotations


class NewFrensChecker:
    def __init__(self, actual_friends_count: str | int):
        self.has_new = 0
        self.actual_friends_count = actual_friends_count

    def store_friends_count(self):
        file1 = open("howmany.txt", "w")
        file1.write(str(self.actual_friends_count))
        file1.close()

    def check_for_new_friends(self):
        with open('howmany.txt', 'r') as file:
            previous_friends_count = int(file.read())
        if self.actual_friends_count > previous_friends_count:
            self.store_friends_count()
            self.has_new = 1
        elif self.actual_friends_count == previous_friends_count:
            self.has_new = 0
        return self.has_new
