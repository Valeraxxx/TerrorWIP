import random




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

    def GenerateCodeGenBase(__TerrorBuildFileCGB):
        with open(__TerrorBuildFileCGB, 'r') as cgb:
            Lin = cgb.readlines()
            for i, x in enumerate(Lin):
                hold = str(x)
                ##TODO
                
                
                

        



    



