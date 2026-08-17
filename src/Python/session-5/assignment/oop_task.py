class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def view_info(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"


class Patient(Person):
    def __init__(self, name: str, age: int, medical_record: str):
        super().__init__(name, age)
        self.medical_record = medical_record

    def view_record(self) -> str:
        return self.medical_record


class Staff(Person):
    def __init__(self, name: str, age: int, position: str):
        super().__init__(name, age)
        self.position = position

    def view_info(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}"


class Department:
    def __init__(self, name: str):
        self.name = name
        self.patients = []
        self.staff_members = []

    def add_patient(self, patient: Patient) -> None:
        self.patients.append(patient)

    def add_staff(self, staff_member: Staff) -> None:
        self.staff_members.append(staff_member)


class Hospital:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.departments = []

    def add_department(self, department: Department) -> None:
        self.departments.append(department)


hospital = Hospital("Al Salam Hospital", "Cairo")

department = Department("Emergency")

patient = Patient("Ahmed", 21, "Blood Test")
staff = Staff("Mohamed", 35, "Doctor")

# Relationships
department.add_patient(patient)
department.add_staff(staff)
hospital.add_department(department)

print(patient.view_info())
print(patient.view_record())

print(staff.view_info())

print(hospital.name)
print(department.name)