from flask import render_template, request, redirect, url_for, Blueprint
from service.reservation_service import ReservationService
from service.restaurant_service import RestaurantService
from util.dto import ReservationFromDto

reservation_blueprint = Blueprint('reservation', __name__)
restaurant_service = RestaurantService()
reservation_service = ReservationService()


@reservation_blueprint.route("/")
def index():
    restaurants = restaurant_service.get_restaurant()
    return render_template('index.html', restaurants=restaurants)

@reservation_blueprint.route("/", methods=['GET', 'POST'])
def add_reservation():
    if request.method == 'POST':
        restaurant_id = request.form['restaurant_id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        num_guest = request.form['num_guests']
        date_time = request.form['date']
        reservation_service.new_reservation(ReservationFromDto(restaurant_id, name, email, phone, num_guest, date_time))
        return redirect(url_for('reservation.index'))
    
@reservation_blueprint.route("/manage")
def manage():
    reservations = reservation_service.get_reservation()
    return render_template('manage_reservations.html', reservations=reservations)

@reservation_blueprint.route("/cancel_reservation/<index>")
def delete(index):
    reservation_service.delete(index)
    return redirect(url_for("reservation.manage"))  