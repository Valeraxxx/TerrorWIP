from concurrent.futures import thread
from gc import collect
from services import TerroistDeamon as td
import subprocess
import threading
from time import sleep
from services.AssestManageT.Main import CodeGenerationPRE
from services.JobHandler import JobHandler

##Root program where the Main thread will be launched.

TERROR_VER = "Dev0.0.0.12.1"
TERROR_CGB = 'cgb.tbf'
TERROR_CGB_PTH = './cgb.tbf'
print("Checking if Daemon Service is ready..")

response = td.Job() # Storing Response from Deamon Job Function

if response == 0:
    print("Daemon Service is busy Attempting when requested.")
if response == 1:
    print("Daemon Service is free and ready.")
    

print("Passing Shell...")
sleep(2)
subprocess.run("clear")

print("""
 ______                       ____                  _      __         __  
/_  __/__ ___________  ____  / __/______ ___ _  ___| | /| / /__  ____/ /__
 / / / -_) __/ __/ _ \/ __/ / _// __/ _ `/  ' \/ -_) |/ |/ / _ \/ __/  '_/
/_/  \__/_/ /_/  \___/_/   /_/ /_/  \_,_/_/_/_/\__/|__/|__/\___/_/ /_/\_\ 
                            𝗣𝗮𝘀𝘀𝗶𝗻𝗴 𝗦𝗵𝗲𝗹𝗹...                                                          
                                                                          """)

sleep(3)

subprocess.run('clear')

# Many other things below 

class TerroistInstructor:
        def InstructionSendOut(self):
            KNOWN_CMDS = ['daemon', 'clear', "help", "exit", "switch", "codegen"]

            match self:
                case "daemon":
                    print("Launching Daemon Service")
                    if td.switch == 0:
                        print("Daemon Not ready.")
                        TerroistInstructor.Shell()
                    else:
                        td.DT.start()
                        td.DT.join()
                        TerroistInstructor.Shell()
                case "clear":
                    subprocess.run("clear")
                    TerroistInstructor.Shell()
                case "exit":
                    print("Exit")
                    exit(0)
                case "help": # Later
                    print(""" 
                    Clear
                    Help
                    Daemon
                    Exit""")
                case "switch":
                    TerroistInstructor.DaemonOperatingStatusSwitch()
                case "codegen":
                    CodeGen.Shell()
                case _:
                    return 0 

            
        def Shell():
            while True:
                SHELL_IN = input("Terror:> ").lower().strip()

                KNOWN_CMDS = ['daemon', 'clear', "help", "exit", "switch", "codegen"]

                for i in KNOWN_CMDS:
                    CurrentC = i
                    if SHELL_IN != CurrentC:
                        continue
                    else:
                        TerroistInstructor.InstructionSendOut(SHELL_IN)
                        continue

        def DaemonOperatingStatusSwitch():
            print(f"Switch Value MUST BE AN INT. 0 Daemon is busy and will not accept new task, 1 Daemon Is ready.\nCurrentt switch value: {td.switch}")
            SwitchValue = input("Switch Value: ")


            if SwitchValue == "0":
                PreviousSV = td.switch
                td.switch = SwitchValue
                print(f"Switch Value changed from {PreviousSV} to {td.switch}")
                TerroistInstructor.Shell()
            elif SwitchValue == "1":
                PreviousSV = td.switch
                td.switch = SwitchValue
                print(f"Switch Value changed from {PreviousSV} to {td.switch}")
                TerroistInstructor.Shell()
            else:
                print("Invalid Option")
                TerroistInstructor.Shell()
                
# Codegen will NOT be handled by the daemon thread, Instead it'll be handled by the parent thread.
class CodeGen:

    def CodeGenVerify(__CODEGENC):
        match __CODEGENC:
            case "generate-cgb":
                CodeGenerationPRE.GenerateCodeGenBase(TERROR_CGB, TERROR_CGB_PTH)
            case "main":
                TerroistInstructor.Shell()
            case _:
                return 0
                


    def Shell():
        Code_Gen_C = ['generate-cgb', "main"]
        while True:
            __CodeGI = input("CODEGEN: ").lower().strip()
            for x in Code_Gen_C:
                Current = x
                if __CodeGI != Current:
                    continue
                else:
                    CodeGen.CodeGenVerify(__CodeGI)

    
                    





                        
            
    
TerroistInstructor.Shell()
        
        

        
