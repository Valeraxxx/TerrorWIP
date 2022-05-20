from time import sleep
import threading 
import services.JobHandler as JobHandler

lock = threading.Lock()

class TerroistDaemon:
    def __init__(self) -> None:
        print("Daemon Started...")
        Response = JobHandler.JobHandler.DaemonJobEnterancePoint()
        print(f"Generated Job Variables")
        if Response == 3:
            print("No Jobs to do.")
        ##TODO




switch = 0

DT = threading.Thread(target=TerroistDaemon, name='Terroist-DaemonPService', daemon=True)

def Job() -> None:
    JOBS = 0
    IdleSwitch = False

    if switch == 0:
        JOBS = 0
    if switch == 1:
        JOBS = 1

    if JOBS == 0:
        IdleSwitch = False
    if JOBS == 1:
        IdleSwitch = True
    
    
    if IdleSwitch == False:
       print("Terroist Jobs Pending.")
       return 0
    if IdleSwitch == True:
        print("Daemon Service is Idling and is ready.")
        DT.start()
        return 1
        ##TODO
    


