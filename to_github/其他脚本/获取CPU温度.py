from time import sleep
from pyspectator.processor import Cpu
cpu = Cpu(monitoring_latency=1)
with cpu:
    while True:
        print(f'Temp: {cpu.temperature} °C')
        sleep(2)