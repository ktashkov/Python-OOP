from project.table import Table


class InsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        if not 1 <= table_number <= 50:
            raise ValueError("Inside table's number must be between 1 and 50 inclusive!")
        super().__init__(table_number, capacity)

    def free_table_info(self):
        if self.is_reserved:
            return ""
        return f"Table: {self.table_number}\nType: Inside\nCapacity: {self.capacity}"
