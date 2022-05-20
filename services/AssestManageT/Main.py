import random






class CodeGeneration():
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

    



