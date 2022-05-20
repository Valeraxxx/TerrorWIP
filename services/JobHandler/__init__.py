import imp
from re import I
import readline
from services.AssestManageT.Main import *

Q_JOBS = [1,1,1]

FileForAsset = "./services/AssestManageT/Main.py"

##TODO

CollectedVars =  CodeGeneration.JobVarSetup(Q_JOBS)


class JobHandler:
    def DaemonJobEnterancePoint():
        if len(Q_JOBS) == 0:
            return 3
        else:
            with open(FileForAsset, 'r') as ffa:
                Line = ffa.readlines()
                Line[4] = CollectedVars[0] + '\n'
               
            with open(FileForAsset, 'w') as ffw:
                ffw.writelines(Line)
                ffw.close()


                    

                    
                    

            
                
                

    def MainThreadEnterancePoint():
        return CollectedVars
        

