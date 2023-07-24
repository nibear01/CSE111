class Rickshaw:
  def __init__(self, cap = 2):
    self.capacity = cap
    self.list1 = []
    self.ride_km = 0
    self.fare = 0

  def addpassenger(self, *x):
    count = 0
    if len(self.list1)>=1:
      count = 1
    else:
      for i in x:
        if isinstance(i, str):
          self.list1.append(i)
        elif isinstance(i, int):
          self.ride_km += i

    if count == 1:
      print("Cannnot add ride. alredy booked.")
    else:
      print(f"{len(self.list1)} peoples are ready for riding {self.ride_km} km")

  def droppassenger(self):
    self.list1 = []
    print("all booked seats are dropped.")
    self.fare = self.ride_km*20

  def details(self):
    return f"capacity: {self.capacity}\nperson: {self.list1}\ntotal fare: {self.fare}"

r1 = Rickshaw()
r1.addpassenger("shanto",3)
print("==============================")
print(r1.details())
print("==============================")
r1.addpassenger("turzo","alif","shaon","riad",5)
print("==============================")
r2 = Rickshaw(3)
r2.addpassenger("turzo","alif","riad","ddddd",6)
print("==============================")
print(r2.details())
print("==============================")
r1.droppassenger()
r2.droppassenger()
print("==============================")
print(r1.details())
print("==============================")
print(r2.details())