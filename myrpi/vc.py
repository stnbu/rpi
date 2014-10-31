
import subprocess

# see also /sys/class/thermal/thermal_zone*/

def get_cpu_temp():
    cmd = "/opt/vc/bin/vcgencmd measure_temp"
    out = subprocess.check_output(cmd.split(), shell=False).strip()
    label, value = out.split('=')
    value, units = value.split("'")
    units = units.lower()

    if units not in ('c', 'f'):
        raise ValueError("Unknown temperature units: {0}".format(units))
    return float(value)
