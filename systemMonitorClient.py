import psutil
import time
import _thread as thread

def my_background_task():
    while(True):
        # Get cpu statistics
        cpu = str(psutil.cpu_percent()) + '%'

        # Calculate memory information
        memory = psutil.virtual_memory()
        # Convert Bytes to MB (Bytes -> KB -> MB)
        available = round(memory.available/1024.0/1024.0,1)
        total = round(memory.total/1024.0/1024.0,1)
        mem_info = str(available) + 'MB free / ' + str(total) + 'MB total ( ' + str(memory.percent) + '% )'

        # Calculate disk information
        disk = psutil.disk_usage('/')
        # Convert Bytes to GB (Bytes -> KB -> MB -> GB)
        free = round(disk.free/1024.0/1024.0/1024.0,1)
        total = round(disk.total/1024.0/1024.0/1024.0,1)
        disk_info = str(free) + 'GB free / ' + str(total) + 'GB total ( ' + str(disk.percent) + '% )'
        print("CPU Info–> ", cpu)
        print("Memory Info–>", mem_info)
        print("Disk Info–>", disk_info)
        time.sleep(1)

thread.start_new_thread(my_background_task, ())