from random import Random, random

#

class CodeGeneration():
    def JobVarSetup(self):
        ProvidedJobs = self
        LengthOfJobs = len(self)
        VarNameGen = ['a', 'x', 'j', 'n', 'w', 'q', 'p', 'tdS']
        for i in ProvidedJobs:
            VarNameAs = Random.choice(VarNameGen)
            VarNumber = Random.randint(0, 30)
            VariableF = f'{VarNameAs}{VarNumber} = \'{i}\''
            CreatedVars.append(VariableF)
            CreatedVars = []
        return CreatedVars

    



