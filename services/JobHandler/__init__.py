import readline
from services.AssestManageT.Main import CodeGeneration


Q_JOBS = []

FileForAsset = "./services/AssestManageT/Main.py"

class JobHandler:
    def DaemonJobEnterancePoint():
        if len(Q_JOBS) == 0:
            return 3
        else:
           CollectedVars =  CodeGeneration.JobVarSetup(Q_JOBS)

           with open(FileForAsset, 'r+') as ffa:
               Line = ffa.readlines

               for i, Line in enumerate(Line):
                   if Line.startswith('#'):
                    for i in CollectedVars:
                        Line[i] = Line[i].strip() + i
                    i.seek(0)
                    for i in Line:
                        ffa.write(i)
                

            



    def MainThreadEnterancePoint():

