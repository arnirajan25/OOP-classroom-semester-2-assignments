from multiprocessing import Process

def message1():
    print("Process 1: Hello!")

def message2():
    print("Process 2: This is multiprocessing module.")

def message3():
    print("Process 3: Multiple processes are running.")

if __name__ == "__main__":
    p1 = Process(target=message1)
    p2 = Process(target=message2)
    p3 = Process(target=message3)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
    print("All processes completed.")
