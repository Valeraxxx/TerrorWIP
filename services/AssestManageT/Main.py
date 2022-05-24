from importlib.resources import path
import random
from re import sub
import subprocess
import os



class CodeGenerationPRE():
    """
    Sets Up and writes the Job Variable for CodeGeneration. Variable Name is plucked at random 
    and is assigned a Job INT.
    """
    def JobVarSetup(self):
        ProvidedJobs = self
        LengthOfJobs = len(self)
        VarNameGen = ['a', 'x', 'j', 'n', 'w', 'q', 'p', 'tdS']
        for i in ProvidedJobs:
            VarNameAs = random.choice(VarNameGen)
            VarNumber = random.randint(0, 30)
            VariableF = f'{VarNameAs}{VarNumber} = \'{i}\''
            CreatedVars = []
            CreatedVars.append(VariableF)
        return CreatedVars

    def GenerateCodeGenBase(__TerrorBuildFileCGB, TerrorCGBpth):
        Path = TerrorCGBpth
        with open(__TerrorBuildFileCGB, 'r') as cgb:
            Lin = cgb.readlines()
            for i, x in enumerate(Lin):
                ReturnToMe = False
                LineBeingProc = i
                if i > 0: 
                    ReturnToMe = True
                else:
                    pass
                
                LineB = str(Lin[i]).rstrip()
                LFN = list(LineB.split(' '))
                Lin[i] = ' '
                match LFN[0]:
                    case "GEN":
                        CodeGenerationPRE.GEN(LFN[1], LFN[2], Path, ReturnToMe)
                    case "OUT":
                        pass
                    case "ADD":
                        pass
                    case "DEL":
                        pass
                    case _:
                        return
    
    def GEN(__FType, __FName, GCBP, RtoGCGB):
        ftt = 9
        fttS = ""
        ReturnToMai = RtoGCGB
        match __FType:
            case "FOLDER":
                ftt = 0
                fttS = "Folder"
            case "FILE":
                ftt = 1
                fttS = "File"
            case _:
                ftt = 9
                ftts = '?'
        
        if ftt == 0:
            pth = f"./{__FName}"
            os.mkdir(pth)
            pass
        elif ftt == 1:
            outp = f'./{__FName}'
            fo = open(outp, "w")
            fo.close()
            pass
        else:
            return 0
            
        print(f"Created {fttS} {outp} from {GCBP}")
        if ReturnToMai == True:
            CodeGenerationPRE.GenerateCodeGenBase(GCBP, GCBP)
        elif ReturnToMai == False:
            pass
        else:
            pass

        
                
        


                    
                
                
                

        



    



