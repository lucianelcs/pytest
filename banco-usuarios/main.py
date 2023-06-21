from src.models.store import Store
from src.models.user import User
from src.service.service_user import ServiceUser

store = Store()

print("#Primeiro Teste")
name = "Luciane"
job = "QA Engineer"

user = User(name=name, job=job)
#print(user, name)
#print(user, job)

service = ServiceUser()
result = service.add_user(name=name, job=job)
print("Nome:", service.store.bd[0].name)
print("Job:", service.store.bd[0].job)
print("Result:", result)

print("#Second Test")
name_1 = None
job_1 = "Eng"

service = ServiceUser()
result = service.add_user(name=name, job=job)
print(service.store.bd)
print("Result:", result)
