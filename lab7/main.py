# Базовый класс Сотрудник
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_info(self):
        return f"Сотрудник: {self.name}, ID: {self.emp_id}"


# Класс Менеджер, наследующий Сотрудник
class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def get_info(self):
        return f"Менеджер: {self.name}, ID: {self.emp_id}, Отдел: {self.department}"

    def manage_project(self, project_name):
        return f"Менеджер {self.name} управляет проектом: {project_name} в отделе {self.department}"


# Класс Техник, наследующий Сотрудник
class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        super().__init__(name, emp_id)
        self.specialization = specialization

    def get_info(self):
        return f"Техник: {self.name}, ID: {self.emp_id}, Специализация: {self.specialization}"

    def perform_maintenance(self, equipment):
        return f"Техник {self.name} выполняет обслуживание {equipment} (специализация: {self.specialization})"


# Класс ТехМенеджер, наследующий Менеджера и Техника
class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Employee.__init__(self, name, emp_id)
        self.department = department
        self.specialization = specialization
        self.team = []

    def get_info(self):
        return f"ТехМенеджер: {self.name}, ID: {self.emp_id}, Отдел: {self.department}, Специализация: {self.specialization}"

    def add_employee(self, employee):
        self.team.append(employee)
        print(f"{employee.name} добавлен в команду.")

    def get_team_info(self):
        if not self.team:
            return "В команде нет сотрудников."
        return "\n".join([member.get_info() for member in self.team])


# Функция интерфейса командной строки
def main():
    print("Добро пожаловать в систему управления сотрудниками!")
    tech_manager = TechManager("Диана", 104, "R&D", "Системы ИИ")
    print(f"ТехМенеджер создан: {tech_manager.get_info()}")

    while True:
        print("\nМеню:")
        print("1. Добавить Сотрудника")
        print("2. Добавить Менеджера")
        print("3. Добавить Техника")
        print("4. Показать информацию о команде")
        print("5. Выйти")

        choice = input("Введите ваш выбор: ")

        if choice == "1":
            name = input("Введите имя сотрудника: ")
            emp_id = input("Введите ID сотрудника: ")
            employee = Employee(name, emp_id)
            tech_manager.add_employee(employee)

        elif choice == "2":
            name = input("Введите имя менеджера: ")
            emp_id = input("Введите ID менеджера: ")
            department = input("Введите отдел: ")
            manager = Manager(name, emp_id, department)
            tech_manager.add_employee(manager)

        elif choice == "3":
            name = input("Введите имя техника: ")
            emp_id = input("Введите ID техника: ")
            specialization = input("Введите специализацию: ")
            technician = Technician(name, emp_id, specialization)
            tech_manager.add_employee(technician)

        elif choice == "4":
            print("\nИнформация о команде:")
            print(tech_manager.get_team_info())

        elif choice == "5":
            print("Выход из программы. До свидания!")
            break

        else:
            print("Некорректный выбор. Попробуйте ещё раз.")

# Запуск программы
if __name__ == "__main__":
    main()
