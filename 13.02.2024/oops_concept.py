class Department:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        pass

class CSE(Department):
    def __init__(self, name):
        super().__init__(name)

    def get_info(self):
        return f"Computer Science and Engineering Department ({self.name})"

class EEE(Department):
    def __init__(self, name):
        super().__init__(name)

    def get_info(self):
        return f"Electrical and Electronics Engineering Department ({self.name})"


if __name__ == "__main__":
    cse_dept = CSE("Dhinakaran R")
    eee_dept = EEE("Deepak N")

    departments = [cse_dept, eee_dept]

    for dept in departments:
        print(dept.get_info())
