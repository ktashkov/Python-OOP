from project.table import Table


class OutsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        if not 51 <= table_number <= 100:
            raise ValueError("Outside table's number must be between 51 and 100 inclusive!")
        super().__init__(table_number, capacity)

    def free_table_info(self):
        if self.is_reserved:
            return ""
        return f"Table: {self.table_number}\nType: Outside\nCapacity: {self.capacity}"
