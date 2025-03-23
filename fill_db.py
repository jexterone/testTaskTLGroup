import random
from datetime import date, timedelta
from departments.models import Department, Employee

root = Department.objects.create(name="Main Department")
for i in range(1, 6):
    parent = root
    for j in range(5):
        child = Department.objects.create(name=f"Department {i}-{j}", parent=parent)
        parent = child

departments = Department.objects.all()
for _ in range(50000):
    department = random.choice(departments)
    Employee.objects.create(
        full_name=f"Employee {_}",
        position=random.choice(["Manager", "Developer", "Analyst"]),
        hire_date=date.today() - timedelta(days=random.randint(0, 365)),
        salary=random.uniform(1000, 10000),
        department=department,
    )