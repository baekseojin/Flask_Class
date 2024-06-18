from model.reservation import Reservation

class ReservationService:
    def __init__(self):
        self.reservation_db = Reservation()

    def get_reservation(self):
        return self.reservation_db.get_reservation()

    def new_reservation(self, reservation):
        self.reservation_db.add_reservation(reservation)

    def delete(self, index):
        self.reservation_db.delete(index)