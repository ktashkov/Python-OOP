from project.booths.booth import Booth

class OpenBooth(Booth):
    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        price_per_person = 2.50
        reservation_price = price_per_person * number_of_people
        self.price_for_reservation = reservation_price
        self.is_reserved = True
