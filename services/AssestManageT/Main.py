from importlib.resources import path
import random
from re import sub
import subprocess
import os
from traceback import print_tb
from typing import Any



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
                LengthS = len(Lin)
                ReturnToMe = False
                LineBeingProc = i
                
                if i > LengthS: 
                    ReturnToMe = True
                else:
                    pass
                
                LineB = str(Lin[i]).rstrip()
                LFN = list(LineB.split(' '))
                Lin[i] = ' '
                match LFN[0]:
                    case "GEN":
                        CodeGenerationPRE.GEN(LFN[1], LFN[2], Path, ReturnToMe)
                    case "ADD":
                        pass
                    case "DEL":
                        Pth = f"./{LFN[2]}"
                        CodeGenerationPRE.DEL(LFN[1], Pth, ReturnToMe, Path)
                    case "END":
                        CodeGenerationPRE.END()
                    case _:
                        return
    
    def GEN(__FType, __FName, GCBP, RtoGCGB):
        ftt = 9
        fttS = ""
        foo = f"./{__FName}"
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
                fttS = '?'
        
        if ftt == 0:
            pth = f"./{__FName}"
            try:
                os.mkdir(pth) 
            except FileExistsError:
                print("Folder Exists already.")

            
        elif ftt == 1:
            outp = f'./{__FName}'

            fo = open(outp, "w")
            fo.close()
            pass
        else:
            return 0
            
        print(f"Created {fttS} {foo} from {GCBP}")
        if ReturnToMai == True:
            CodeGenerationPRE.GenerateCodeGenBase(GCBP, GCBP)
        elif ReturnToMai == False:
            pass
        else:
            pass

    def DEL(_FType, _FPath, RtoGCGB, GCBP):
        match _FType:
                    case "FOLDER":
                        try:
                            os.rmdir(_FPath)
                            pass
                        except NotADirectoryError as b:
                            print(f"{_FPath} Doesnt Exists.")
                            pass
                        except FileNotFoundError as b:
                            print(f"{_FPath} Doesnt Exists.")
                            pass

                    case "FILE":
                        try:
                            os.remove(_FPath)
                            print(f"Deleted {_FPath}.")
                            pass
                        except FileNotFoundError as s:
                            print(f"{_FPath} Doesnt Exists.")
                            pass
                    case _:
                        ftt = 9
                        fttS = '?'
        

        
        if RtoGCGB == True:
            CodeGenerationPRE.GenerateCodeGenBase(GCBP, GCBP)
        else:
            return
    
    def END():
        print("Reached EOL.")
        return




        
                
        


                    
                
                
                

        



    



