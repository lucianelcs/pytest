from src.models.store import Store
from src.models.user import User

class ServiceUser:
    def __init__(self):
        self.store = Store()

    def check_user(self, name):
        for user in self.store.bd:
            if name == user.name:
                return user
        return None

    def add_user(self, name, job):
        if name is not None and job is not None:
            if isinstance(name, str) and isinstance(job, str):
                if self.check_user(name):
                    return "User already exists"
                else:
                    user = User(name, job)
                    self.store.bd.append(user)
                    return "User added successfully"
            else:
                return "Name or job need to be string"
        else:
            return "Invalid User"

    def update_user(self, name, new_job):
        user_bd = self.check_user(name)
        if user_bd is not None:
            user_bd.job = new_job
            return "Job was updated"
        else:
            return "User name is not found"

    def select_user(self, name):
        user_bd = self.check_user(name)
        if user_bd is not None:
            return "Job: " + user_bd.job
        else:
            return "User name is not found"

    def delete_user(self, name):
        user = self.check_user(name)
        if user is not None:
            self.store.bd.remove(user)
            return "User was removed"
        else:
            return "User name is not found"
