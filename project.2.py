def clockangle(hour, minutes):
  for i in range(12):
    if 00 <= hour <= 24 and 00 <= minutes <= 60:
      if hour > 12:
        hour = hour - 12
      if minutes == 60:
        hour = hour + 1
        minutes = 00
      hour = hour + minutes / 60
      handiff = abs(hour - minutes / 5)
      preangle = handiff * 30
      postangle = min(preangle, 360 - preangle)
      return postangle
    else:
      print("Enter a correct time.")
      exit()
print("_______________________________________________\n")
print("Give a time in hh:mm format in 24 hour notation")
print("_______________________________________________\n")
postangle=clockangle(int(input("Hour: ")), int(input("Minutes: ")))
angle=format(postangle,".2f")
print("\nThe difference between the hour and the minute hand is",angle + "°")  