
import rpitemp
w1 = rpitemp.W1Bus()

for device_name in w1.devices:
    print device_name
