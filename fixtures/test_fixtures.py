# import pytest
class vehicle:

    def start_vehicle(self):
        print("Vehicle started")
        return  "vehicle started"

    def show_details(self):
        print("Vehicle details")
        return "show details"


v = vehicle()
print(v.start_vehicle())

#
# def test_vehiclestarted():
#     v = vehicle()
#     assert v.start_vehicle() == "vehicle started"
#
# def test_vehicledetails():
#     v = vehicle()
#     assert v.show_details() == "show details"