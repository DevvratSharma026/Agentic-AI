device_status = "active"
temperature = 34

if device_status == 'active':
    if temperature < 35:
        print("temprature too low!")
    elif temperature > 35:
        print("temprature too high!")
    else:
        print("perfect temperature")
else:
    print("Device is offline")