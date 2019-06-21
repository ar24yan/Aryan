import threading


def gfg():
    print("GeeksforGeeks\n")


timer = threading.Timer(12.0, gfg)
timer.start()
print("Exit\n")

