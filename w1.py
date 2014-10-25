import os
import re

def get_w1_temps():

    basedir = '/sys/bus/w1/devices/w1_bus_master1'
    basedir = os.path.sep.join(basedir.split('/'))
    with open(os.path.join(basedir, 'w1_master_slaves'), 'r') as f:
        slaves = f.read()
        slaves = slaves.splitlines()

    """  Sample output:
    aa 01 4b 46 7f ff 06 10 84 : crc=84 YES
    aa 01 4b 46 7f ff 06 10 84 t=26625
    """
    temp_re = re.compile(r'\st=(?P<temp>\d+)[\s\n]')
    temps = {}
    for slave in slaves:
        with open(os.path.join(basedir, slave, 'w1_slave'), 'r') as f:
            out = f.read()
            temp, = temp_re.search(out).groups('temp')
            temp = float('.'.join([temp[:2], temp[2:]]))
            temps[slave] = temp

    return temps

print get_w1_temps()
