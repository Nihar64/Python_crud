
# user.py
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role


# Predefined users
USERS = {
    "1": User("USER1", "ADMIN"),
    "2": User("USER2", "USER")
}
