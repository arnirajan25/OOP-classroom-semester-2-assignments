# module_b.py
import module1

def func_b():
    return module1.func_a()  # module1.func_a might not exist yet at import time