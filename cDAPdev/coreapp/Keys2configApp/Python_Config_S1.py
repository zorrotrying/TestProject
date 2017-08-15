import inspect
import importlib
import sys


def generateForm(FunPath, ScriptFileName):
    sys.path.append(FunPath)
    myModule = importlib.import_module(ScriptFileName)
    FunList = [x.__name__ for x in myModule.__dict__.values() if inspect.isfunction(x)]

    ResultListDir = []
    for i in range(len(FunList)):
        argList = inspect.getargspec(eval('%s.%s' % ('myModule', FunList[i])))
        temp_d = {'Arg_Name': argList[0],
                  'Fun_Name': FunList[i],
                  'Arg_Value': argList[3],}
        ResultListDir.append(temp_d)
    return ResultListDir


