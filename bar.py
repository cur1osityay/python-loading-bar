import time
import sys
toolbar_width = 90

start_time = time.time()

def toolbar():
    print('EXEC TIME IS 90S)')
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) 
    for i in range(toolbar_width):
        time.sleep(1) 
        sys.stdout.write("■")
        sys.stdout.flush()
    sys.stdout.write("]\n") 

toolbar()

print("--- %s seconds ---" % (time.time() - start_time))
