import platform
import os

print("Operating System:", platform.system())
print("Node Name:", platform.node())
print("OS Release:", platform.release())
print("OS Version:", platform.version())
print("Machine:", platform.machine())
print("Processor:", platform.processor())
print("Architecture:", platform.architecture())
print("Python Version:", platform.python_version())
print("Python Compiler:", platform.python_compiler())

print(os.getcwd())

os.c


import sys

# Список загруженных модулей
print("Загруженные модули:")
for module in sys.modules:
    print(module)