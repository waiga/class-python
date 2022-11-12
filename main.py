# Python Class 란?
class User:

    # class 내부의 local variable 값
    count = 0

    #special method - initialize
    def __init__(self, user_id, username, password):
        '''initialize attributes는 무엇인가'''
        self.id = user_id
        self.username = username
        self.password = password
        self.follower = 0
        self.following = 0
        # 이 클래스를 호출할 때마다 자동으로 카운트 되도록 클래스 변수를 설정함
        User.count += 1 # 해당 클래스를 인스턴스로 호출할 때마다 증가함

    def follow(self, user):
        '''python class method 란'''
        # 그 유저 객체의 팔로워를 하나 증가하고
        user.follower += 1
        # 나 를 기준으로 했을 때는 팔로잉을 한 거니 나 라는 객체의 팔로잉은 증가
        self.following += 1

# 다음과 같은 클래스를 호출했음 총 3명
user_1 = User("001", "mianmianhae", "1234")
user_2 = User("002", "leeleeleelee", "5678")
user_3 = User("003", "jangminchu...", "9876")

# 해당 클래스의 Method를 호출함
user_1.follow(user_2)

# 그럼 어떤 일이 벌어지게 될지를 테스트
print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)

# 인원수 카운트하기 위해 만들었음. 총 3명이니 해당 인원수 카운트 한 것
print(User.count)
