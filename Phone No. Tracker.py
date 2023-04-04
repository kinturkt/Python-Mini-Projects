import phonenumbers
from phonenumbers import geocoder
p1= phonenumbers.parse("+91 9537428943")
p2= phonenumbers.parse("+91 9408686215")
p3= phonenumbers.parse("+1 9052660304")
p4= phonenumbers.parse("+1 6475406958")
p5= phonenumbers.parse("+1 7147574759")
p6= phonenumbers.parse("+1 6825979978")


print("Kintur's number Location: " + geocoder.description_for_number(p1,"en"))
print("Heli's number Location: " + geocoder.description_for_number(p2,"en"))
print("Sandip's number Location: " + geocoder.description_for_number(p3,"en"))
print("Urdhva's number Location: " + geocoder.description_for_number(p4,"en"))
print("Gunjan's number Location: " + geocoder.description_for_number(p5,"en"))
print("Krina's number Location: " + geocoder.description_for_number(p6,"en"))