from ast import Str
from asyncio import exceptions
from importlib.resources import path
from multiprocessing.context import ForkContext
import random
from re import sub
import subprocess
import os
from time import sleep
from traceback import print_tb
from typing import Any, Literal



class CodeGenerationPRE():
    _GENERATED_PATHSPRE = []
    G_PATH = ""
    CURRENT_WORKSPACE = ""
    """
    CodeGeneration Pre
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

        CodeGenerationPRE.G_PATH = Path

        with open(__TerrorBuildFileCGB, 'r') as cgb:
            Lin = cgb.readlines()
            
            r = str(Lin).find("def")
            w = str(Lin).find("END")



            if r == -1:
                print("Error: Missing Workspace definition. Did you add \"def\" at top-level of the .tbf file?")
                return
            elif w == -1: 
                print("Warning: Missing END decleration, This may cause problems for larger builds.")
                pass
            else:
                pass

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
                        CodeGenerationPRE.GEN(LFN[1], LFN[2], Path, ReturnToMe, LineB)
                    case "ADD":
                        pass
                    case "DEL":
                        Pth = f"./{CodeGenerationPRE.CURRENT_WORKSPACE}/{LFN[2]}"
                        CodeGenerationPRE.DEL(LFN[1], Pth, ReturnToMe, Path)
                    case "END":
                        CodeGenerationPRE.END()
                    case "def":
                        CodeGenerationPRE.DEFINE(LFN[1], ReturnToMe)
                    case "wait":
                        CodeGenerationPRE.WAIT(ReturnToMe, LFN[1])
                    case _:
                        return

    
    def GEN(__FType, __FName, GCBP, RtoGCGB, FullStr):
        ftt = 9
        fttS = ""
        foo = f"./{CodeGenerationPRE.CURRENT_WORKSPACE}/{__FName}"
        ReturnToMai = RtoGCGB

        Check = str(FullStr).find("in")
        Strtouse = str(FullStr)
        Strlen = len(Strtouse)

        if Check == -1:
            pass
        else: 
            Strtouse = Strtouse[Check: Strlen].replace("in", '').strip()
            pass    
        
        if CodeGenerationPRE._GENERATED_PATHSPRE == 0:
            pass
        else:
            lk = CodeGenerationPRE.StringFormattingEXE(__FName, CodeGenerationPRE._GENERATED_PATHSPRE, Strtouse)
            if lk == None:
                print("INFO: Empty Path List, Populating.")
                pass
            elif lk == 1:
                print("FATAL: Looks like you're running CGB Again, Exit CodeGen and try again.")
            else:
                print("INFO: Populated Path list.")
                foo = lk
                
        match __FType:
            case "FOLDER":
                ftt = 0
            case "FILE":
                ftt = 1
            case _:
                ftt = 9
        
        if ftt == 0:
            try:
                os.mkdir(foo)
                print(f"Created {foo} from {GCBP}")
                CodeGenerationPRE._GENERATED_PATHSPRE.append(foo)
                if ReturnToMai == True:
                    CodeGenerationPRE.GenerateCodeGenBase(GCBP, GCBP)
                elif ReturnToMai == False:
                    pass
            except FileExistsError:
                print(f"Folder {foo} Exists already.")

        elif ftt == 1:
            outp = foo
            CodeGenerationPRE._GENERATED_PATHSPRE.append(foo)
            fo = open(outp, "w")
            fo.close()
            pass
        
            

    def DEL(_FType, _FPath, RtoGCGB, GCBP):
        match _FType:

                    case "FOLDER":
                        try:
                            os.rmdir(_FPath)
                            print(f"Deleted {_FPath}")
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
        CodeGenerationPRE._GENERATED_PATHSPRE.clear()
        return
    
    def DEFINE(WorkSpace, RtoGCGB):
        rootfname = WorkSpace
        CodeGenerationPRE.CURRENT_WORKSPACE = str(rootfname).replace('-', '_')
        short = CodeGenerationPRE.G_PATH
        try:
            os.mkdir(f"./{CodeGenerationPRE.CURRENT_WORKSPACE}".replace('-', "_"))
        except FileExistsError:
            pass

        if RtoGCGB == True:
            CodeGenerationPRE.GenerateCodeGenBase(short, short)
        else:
            return
    
    def WAIT(RtoGCGB, _RTime):
        print(f"Sleeping for {_RTime} seconds")
        sleep(int(_RTime))
        short = CodeGenerationPRE.G_PATH
        if RtoGCGB == True:
            CodeGenerationPRE.GenerateCodeGenBase(short, short)
        else:
            return


    def StringFormattingEXE(NameBefIn, pthlst, NameAftIn):
        _ALWAYSROOT = f"./{CodeGenerationPRE.CURRENT_WORKSPACE}/"
        for i, x in enumerate(pthlst):
            FixString = str(x).strip().find(NameAftIn)

            if FixString == -1:
                continue
            else:
                StrN = x 
                NewStr = f"{StrN}/{NameBefIn}"
                return NewStr
    
    

        
                
                
             




        
                
        


                    
                
                
                

        



    



