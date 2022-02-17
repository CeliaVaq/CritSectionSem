#04_decker

from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Value, Array
from multiprocessing import Lock

N = 8


def task(common, tid, critical, l):

    a=0
    for i in range(100):
        print(f'{tid}−{i}: Non−critical Section')
        a += 1
        print(f'{tid}−{i}: End of non−critical Section')
        critical[tid] = 1
        
        l.acquire()
        try:
            print(f'{tid}−{i}: Critical section')
            v = common.value + 1
            print(f'{tid}−{i}: Inside critical section')
            common.value = v
            print(f'{tid}−{i}: End of critical section')
            critical[tid] = 0
        finally:
            l.release()

def main():
    lp = []
    lock = Lock()
    common = Value('i', 0)
    critical = Array('i', [0]*N)
    for tid in range(N):
        lp.append(Process(target=task, args=(common, tid, critical, lock)))
    print (f"Valor inicial del contador {common.value}")
    for p in lp:
        p.start()
    
    for p in lp:
        p.join()
    
    print (f"Valor final del contador {common.value}")
    print ("fin")

if __name__ == "__main__":
    main()
"""
    for num in range(10):
        Process(target=task, args=(lock, num)).start()
"""
#lock -> semaforo binario con k = 1
#BoundedSemaphore(k) -> semáforo arbitrario
#l.acquire() es wait
#l.release() es signal


