"1"


import math


class Vector:
    def __init__(self, *sonlar):
        if not sonlar:
            raise ValueError("Vektor kamida bitta komponentga ega bo'lishi kerak")
        self.sonlar = sonlar

    def __len__(self):
        return len(self.sonlar)

    def __str__(self):
        qismlar = []
        for x in self.sonlar:
            if isinstance(x, float):
                qismlar.append(str(round(x, 3)))
            else:
                qismlar.append(str(x))
        return f"Vector({', '.join(qismlar)})"

    def _olcham_tekshir(self, other):
        if len(self) != len(other):
            raise ValueError(f"Vektorlar o'lchami har xil: {len(self)} va {len(other)}")

    def __add__(self, other):
        self._olcham_tekshir(other)
        return Vector(*[x + y for x, y in zip(self.sonlar, other.sonlar)])

    def __sub__(self, other):
        self._olcham_tekshir(other)
        return Vector(*[x - y for x, y in zip(self.sonlar, other.sonlar)])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*[x * other for x in self.sonlar])
        if isinstance(other, Vector):
            self._olcham_tekshir(other)
            return sum(x * y for x, y in zip(self.sonlar, other.sonlar))
        raise TypeError("Vektorni faqat songa yoki vektorga ko'paytirish mumkin")

    def __rmul__(self, other):
        return self * other

    def magnitude(self):
        return math.sqrt(sum(x ** 2 for x in self.sonlar))

    def normalize(self):
        uzunlik = self.magnitude()
        if uzunlik == 0:
            raise ValueError("Nol vektorni normallashtirib bo'lmaydi")
        return Vector(*[x / uzunlik for x in self.sonlar])


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1)
print(v1 + v2)
print(v2 - v1)
print(v1 * v2)
print(3 * v1)
print(v1.magnitude())
print(v1.normalize())


"2"

class Employee:
    """Bitta xodimni ifodalaydi."""

    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:
    """employees.txt faylidagi xodimlarni boshqaradi."""

    def __init__(self, filename="employees.txt"):
        self.filename = filename

    def _load(self):
        """Fayldagi barcha xodimlarni Employee obyektlari ro'yxati sifatida qaytaradi."""
        employees = []
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    parts = line.strip().split(", ")
                    if len(parts) == 4:
                        employees.append(Employee(*parts))
        except FileNotFoundError:
            pass
        return employees

    def _save(self, employees):
        """Xodimlar ro'yxatini faylga qaytadan to'liq yozadi."""
        with open(self.filename, "w") as f:
            for emp in employees:
                f.write(str(emp) + "\n")

    def _find(self, employees, employee_id):
        """ID bo'yicha xodimni topadi, topilmasa None qaytaradi."""
        for emp in employees:
            if emp.employee_id == employee_id:
                return emp
        return None

    def _input_salary(self, prompt, allow_empty=False):
        """Maoshni so'raydi va son ekanini tekshiradi."""
        while True:
            salary = input(prompt).strip()
            if allow_empty and salary == "":
                return ""
            if salary.isdigit():
                return salary
            print("Salary must be a positive whole number!")

    def add_employee(self):
        employees = self._load()
        employee_id = input("Enter Employee ID: ").strip()
        if not employee_id:
            print("Employee ID cannot be empty!")
            return
        if self._find(employees, employee_id):
            print("Employee ID already exists!")
            return
        name = input("Enter Name: ").strip()
        position = input("Enter Position: ").strip()
        salary = self._input_salary("Enter Salary: ")

        employee = Employee(employee_id, name, position, salary)
        try:
            with open(self.filename, "a") as f:
                f.write(str(employee) + "\n")
            print("Employee added successfully!")
        except OSError:
            print("Error: could not write to file.")

    def view_all_employees(self):
        employees = self._load()
        if not employees:
            print("No employee records found.")
            return

        sort_choice = input("Sort by: 1) ID  2) Name  3) Salary  (Enter to skip): ").strip()
        if sort_choice == "1":
            employees.sort(key=lambda e: e.employee_id)
        elif sort_choice == "2":
            employees.sort(key=lambda e: e.name.lower())
        elif sort_choice == "3":
            employees.sort(key=lambda e: int(e.salary), reverse=True)

        print("Employee Records:")
        for emp in employees:
            print(emp)

    def search_employee(self):
        employee_id = input("Enter Employee ID to search: ").strip()
        emp = self._find(self._load(), employee_id)
        if emp:
            print("Employee Found:")
            print(emp)
        else:
            print("Employee not found.")

    def update_employee(self):
        employees = self._load()
        employee_id = input("Enter Employee ID to update: ").strip()
        emp = self._find(employees, employee_id)
        if not emp:
            print("Employee not found.")
            return

        print("Press Enter to keep the current value.")
        emp.name = input(f"New Name ({emp.name}): ").strip() or emp.name
        emp.position = input(f"New Position ({emp.position}): ").strip() or emp.position
        emp.salary = self._input_salary(f"New Salary ({emp.salary}): ", allow_empty=True) or emp.salary

        self._save(employees)
        print("Employee updated successfully!")

    def delete_employee(self):
        employees = self._load()
        employee_id = input("Enter Employee ID to delete: ").strip()
        remaining = [emp for emp in employees if emp.employee_id != employee_id]
        if len(remaining) == len(employees):
            print("Employee not found.")
            return
        self._save(remaining)
        print("Employee deleted successfully!")

    def run(self):
        print("Welcome to the Employee Records Manager!")
        while True:
            print("""
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit""")
            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                self.search_employee()
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please enter a number from 1 to 6.")


manager = EmployeeManager()
manager.run()


"3"

import csv
import json

STATUSES = ["Pending", "In Progress", "Completed"]
FIELDS = ["task_id", "title", "description", "due_date", "status"]


class Task:
   

    def __init__(self, task_id, title, description, due_date="", status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
       
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
        }

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"


class Storage:


    def __init__(self, filename):
        self.filename = filename

    def save(self, tasks):
        raise NotImplementedError

    def load(self):
        raise NotImplementedError


class JSONStorage(Storage):
   

    def save(self, tasks):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4, ensure_ascii=False)

    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return [Task(**data) for data in json.load(f)]
        except FileNotFoundError:
            return []


class CSVStorage(Storage):


    def save(self, tasks):
        with open(self.filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

    def load(self):
        try:
            with open(self.filename, "r", newline="", encoding="utf-8") as f:
                return [Task(**row) for row in csv.DictReader(f)]
        except FileNotFoundError:
            return []


STORAGE_TYPES = {
    "1": ("JSON", lambda: JSONStorage("tasks.json")),
    "2": ("CSV", lambda: CSVStorage("tasks.csv")),
}


class TaskManager:
    """Vazifalarni boshqaradi. Fayl formatiga bog'liq emas."""

    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load()

    def _find(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def _input_status(self, prompt, allow_empty=False):
        while True:
            status = input(prompt).strip()
            if allow_empty and status == "":
                return ""
            for s in STATUSES:
                if status.lower() == s.lower():
                    return s
            print(f"Status must be one of: {', '.join(STATUSES)}")

    def add_task(self):
        task_id = input("Enter Task ID: ").strip()
        if not task_id:
            print("Task ID cannot be empty!")
            return
        if self._find(task_id):
            print("Task ID already exists!")
            return
        title = input("Enter Title: ").strip()
        description = input("Enter Description: ").strip()
        due_date = input("Enter Due Date (YYYY-MM-DD, optional): ").strip()
        status = self._input_status("Enter Status (Pending/In Progress/Completed): ")
        self.tasks.append(Task(task_id, title, description, due_date, status))
        print("Task added successfully!")

    def view_tasks(self, tasks=None):
        tasks = self.tasks if tasks is None else tasks
        if not tasks:
            print("No tasks found.")
            return
        print("Tasks:")
        for task in tasks:
            print(task)

    def update_task(self):
        task = self._find(input("Enter Task ID to update: ").strip())
        if not task:
            print("Task not found.")
            return
        print("Press Enter to keep the current value.")
        task.title = input(f"New Title ({task.title}): ").strip() or task.title
        task.description = input(f"New Description ({task.description}): ").strip() or task.description
        task.due_date = input(f"New Due Date ({task.due_date}): ").strip() or task.due_date
        task.status = self._input_status(f"New Status ({task.status}): ", allow_empty=True) or task.status
        print("Task updated successfully!")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ").strip()
        remaining = [task for task in self.tasks if task.task_id != task_id]
        if len(remaining) == len(self.tasks):
            print("Task not found.")
            return
        self.tasks = remaining
        print("Task deleted successfully!")

    def filter_tasks(self):
        status = self._input_status("Enter Status to filter (Pending/In Progress/Completed): ")
        self.view_tasks([task for task in self.tasks if task.status == status])

    def save_tasks(self):
        try:
            self.storage.save(self.tasks)
            print(f"Tasks saved to {self.storage.filename}!")
        except OSError:
            print("Error: could not save tasks.")

    def load_tasks(self):
        try:
            self.tasks = self.storage.load()
            print(f"Tasks loaded from {self.storage.filename}!")
        except (OSError, ValueError, TypeError):
            print("Error: could not load tasks (file may be damaged).")

    def run(self):
        print("Welcome to the To-Do Application!")
        actions = {
            "1": self.add_task,
            "2": self.view_tasks,
            "3": self.update_task,
            "4": self.delete_task,
            "5": self.filter_tasks,
            "6": self.save_tasks,
            "7": self.load_tasks,
        }
        while True:
            print("""
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Load tasks
8. Exit""")
            choice = input("\nEnter your choice: ").strip()
            if choice == "8":
                print("Goodbye!")
                break
            if choice in actions:
                actions[choice]()
            else:
                print("Invalid choice! Please enter a number from 1 to 8.")


def choose_storage():
    """Foydalanuvchiga saqlash formatini tanlatadi."""
    while True:
        print("Choose storage format:")
        for key, (name, _) in STORAGE_TYPES.items():
            print(f"{key}. {name}")
        choice = input("Enter your choice: ").strip()
        if choice in STORAGE_TYPES:
            return STORAGE_TYPES[choice][1]()
        print("Invalid choice!")


manager = TaskManager(choose_storage())
manager.run()