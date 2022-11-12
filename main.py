# Python Class 란?
class User:

    count = 0

    def __init__(self, user_id, username, password):
        '''initialize attributes란'''
        self.id = user_id
        self.username = username
        self.password = password
        self.follower = 0
        self.following = 0
        User.count += 1 # 해당 클래스를 인스턴스로 호출할 때마다 증가함.

    def follow(self, user):
        '''python class method란'''
        user.follower += 1
        self.following += 1


user_1 = User("001", "mianmianhae", "1234")
user_2 = User("002", "leeleeleelee", "5678")
user_3 = User("003", "jangminchu...", "9876")
user_1.follow(user_2)
print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)


print(User.count)
