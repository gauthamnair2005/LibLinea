# LibLinea - The Core Module for Linea Programming Language

# Imports

import os
import sys
import ast
import statistics
import math
import matplotlib.pyplot as plt
import time
import datetime
import threading
import subprocess
import platform
import psutil
import pandas as pd

# Constants / Linea/LSP reserved keywords

_lspVer = "2.2.0"
_lineaVer = "2.2.0"
_developer = "Gautham Nair"
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"
ARITH = ["+", "-", "*", "/", "%", "^"]
floatNotCase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "'", '"', ",", "/", "\\", "<", ">", ";", ":", "[", "]", "{", "}", "-", "_", "+", "=", "(", ")", "!", "@", "#", "$", "%", "^", "&", "*", "~", "`", "|"]
operators = ["+", "-", "*", "/", "%", "^", "(", ")"]

# Variable Storing (Struct)

_lspVariables = {"_lspVer" : _lspVer, "_developer" : _developer}
_lspVariablesDType = {"_lspVer" : "String", "_developer" : "String"}
_lineaVariables = {"_lineaVer" : _lineaVer, "_developer" : _developer}
_lineaVariablesDType = {"_lineaVer" : "String", "_developer" : "String"}
_lineaActorVariables = {}
_lineaActorVariablesDType = {}
_lspActorVariables = {}
_lspActorVariablesDType = {}

# Classes

# Linea Class

class Linea:
    @staticmethod
    def display(param):
        try:
            if callable(param):
                result = param()
                print(result)
            else:
                print(param)
        except Exception as e:
            print(f"{RED}Error in display: {str(e)}{END}")
    
    @staticmethod
    def displayError(param):
        Linea.display(RED + param + END)

    @staticmethod
    def displayWarning(param):
        Linea.display(YELLOW + param + END)

    def plot(param):
        try:
            if param == "":
                err = Error("L-E4", f"Syntax Error: Invalid operation")
                err.displayError()
                return
            else:
                plt.plot(param)
                plt.show()
        except Exception as e:
            print(f"{RED}Error in plot: {str(e)}{END}")

    @staticmethod
    def varOps(param):
        operator, varName= param.split(" ")
        varName = varName.split(",")
        varName = [i.strip() for i in varName]
        if operator == "+":
            result = 0
            for i in range(0, len(varName)):
                result += float(_lineaVariables[varName[i]])
            print(result)
        elif operator == "-":
            result = float(_lineaVariables[varName[0]])
            for i in range(1, len(varName)):
                result -= float(_lineaVariables[varName[i]])
            print(result)
        elif operator == "*":
            result = 1
            for i in range(0, len(varName)):
                result *= float(_lineaVariables[varName[i]])
            print(result)
        elif operator == "/":
            result = float(_lineaVariables[varName[0]])
            for i in range(1, len(varName)):
                try:
                    result /= float(_lineaVariables[varName[i]])
                except:
                    err = Error("L-E8", f"Syntax Error: Division by zero")
                    err.displayError()
            print(result)
        elif operator == "%":
            result = float(_lineaVariables[varName[0]])
            for i in range(1, len(varName)):
                result %= float(_lineaVariables[varName[i]])
            print(result)
        elif operator == "^":
            result = float(_lineaVariables[varName[0]])
            for i in range(1, len(varName)):
                result **= float(_lineaVariables[varName[i]])
            print(result)
        else:
            err = Error("L-E7", f"Syntax Error: Invalid operator '{operator}'")
            err.displayError()

    @staticmethod
    def varAct(varName, value, global_context = None):
        if varName not in _lineaVariables:
            err = Error("L-E1", f"Syntax Error: Variable '{varName}' not found")
            err.displayError()
            Linea.displayWarning(f"Variable Name: {varName}. To update its value, use `varUpd`")
        try:
            if value in _lineaVariables.keys():
                _lineaActorVariables[varName] = _lineaVariables[value]
                _lineaActorVariablesDType[varName] = _lineaVariablesDType[value]
            elif value.isdigit():
                _lineaActorVariables[varName] = int(value)
                _lineaActorVariablesDType[varName] = "Integer"
            elif value.replace(".", "", 1).isdigit():
                _lineaActorVariables[varName] = float(value)
                _lineaActorVariablesDType[varName] = "Floating Point"
            elif value.startswith('"') and value.endswith('"'):
                _lineaActorVariables[varName] = value[1:-1]
                _lineaActorVariablesDType[varName] = "String"
            elif value.startswith("'") and value.endswith("'"):
                _lspActorVariables[varName] = value[1:-1]
                _lineaActorVariablesDType[varName] = "String"
            elif value.startswith("[") and value.endswith("]"):
                import ast
                _lineaActorVariables[varName] = ast.literal_eval(value)
                _lineaActorVariablesDType[varName] = "Array"
            elif value == "True":
                _lineaActorVariables[varName] = True
                _lineaActorVariablesDType[varName] = "Boolean"
            elif value == "False":
                _lineaActorVariables[varName] = False
                _lineaActorVariablesDType[varName] = "Boolean"
            elif value in ["None", "NULL", "NIL", "undefined"]:
                _lineaActorVariables[varName] = None
                _lineaActorVariablesDType[varName] = "None"
            elif value in ["Yes", "yes", "YES", "Y", "y"]:
                _lineaActorVariables[varName] = True
                _lineaActorVariablesDType[varName] = "QuestionAnswer"
            elif value in ["No", "no", "NO", "N", "n"]:
                _lineaActorVariables[varName] = False
                _lineaActorVariablesDType[varName] = "QuestionAnswer"
            else:
                try:
                    parts = value.split(".")
                    module_name = ".".join(parts[:-2])  # e.g., "math.liblinea"
                    class_name = parts[-2]  # e.g., "Basic"
                    function_call = parts[-1]  # e.g., "sqrt(5)"
                    func_name, args = function_call.split("(", 1)
                    args = args.rstrip(")")# Get the module, class, and function
                    module = global_context.get(module_name)
                    if not module:
                        Linea.displayError(f"Module '{module_name}' not found")
                    cls = getattr(module, class_name)
                    func = getattr(cls(), func_name)
                    
                    # Evaluate the arguments and call the function
                    result = func(*eval(f"[{args}]"))
                    _lineaVariables[varName] = result
                except:
                    err = Error("L-E2", f"Syntax Error: Invalid value in variable declaration")
                    err.displayError(err)
                    return
        except (ValueError, SyntaxError):
            err = Error("L-E2", f"Syntax Error: Invalid value in variable declaration")
            err.displayError(err)
            return

    @staticmethod
    def displayVars():
        for varName, value in _lineaVariables.items():
            if not varName.startswith("_"):
                print(f"{varName}: {value} ({_lineaVariablesDType[varName]})", end = " ")
            else:
                pass
        print("\n")
        return
    
    @staticmethod
    def displayVarsDType():
        for varName, value in _lineaVariablesDType.items():
            if not varName.startswith("_"):
                print(f"{varName}: {value}", end = " ")
            else:
                pass
        print("\n")
        return
    
    @staticmethod
    def displayActVars():
        for varName, value in _lineaActorVariables.items():
            if not varName.startswith("_"):
                print(f"{varName}: {value} ({_lineaActorVariablesDType[varName]})", end = " ")
            else:
                pass
        print("\n")
        return
    
    @staticmethod
    def displayActVarsDType():
        for varName, value in _lineaActorVariablesDType.items():
            if not varName.startswith("_"):
                print(f"{varName}: {value}", end = " ")
            else:
                pass
        print("\n")
        return
        
    @staticmethod
    def varActKill(varName):
        if varName == "":
            _lineaActorVariables.clear()
            _lineaActorVariablesDType.clear()
        elif varName in _lineaActorVariables:
            del _lineaActorVariables[varName]
            del _lineaActorVariablesDType[varName]
        else:
            err = Error("L-E6", f"Syntax Error: Actor {varName} not found")
            err.displayError()
            Linea.displayWarning(f"Variable Name: {varName}. To mask its value, use `act`")
        return

    @staticmethod
    def varDeclare(varName, value, global_context = None):
        if varName in _lspVariables:
            err = Error("L-E5", f"Syntax Error: Variable already declared")
            err.displayError()
            Linea.displayWarning(f"Variable Name: {varName}. To update its value, use `varUpd`")
        try:
            if value in _lineaVariables.keys():
                _lineaVariables[varName] = _lineaVariables[value]
                _lineaVariablesDType[varName] = _lineaVariablesDType[value]
            elif value.isdigit():
                _lineaVariables[varName] = int(value)
                _lineaVariablesDType[varName] = "Integer"
            elif value.replace(".", "", 1).isdigit():
                _lineaVariables[varName] = float(value)
                _lineaVariablesDType[varName] = "Floating Point"
            elif value.startswith('"') and value.endswith('"'):
                _lineaVariables[varName] = value[1:-1]
                _lineaVariablesDType[varName] = "String"
            elif value.startswith("'") and value.endswith("'"):
                _lspVariables[varName] = value[1:-1]
                _lineaVariablesDType[varName] = "String"
            elif value.startswith("[") and value.endswith("]"):
                _lineaVariables[varName] = ast.literal_eval(value)
                _lineaVariablesDType[varName] = "Array"
            elif value == "True":
                _lineaVariables[varName] = True
                _lineaVariablesDType[varName] = "Boolean"
            elif value == "False":
                _lineaVariables[varName] = False
                _lineaVariablesDType[varName] = "Boolean"
            elif value in ["None", "NULL", "NIL", "undefined"]:
                _lineaVariables[varName] = None
                _lineaVariablesDType[varName] = "None"
            elif value in ["Yes", "yes", "YES", "Y", "y"]:
                _lineaVariables[varName] = "Yes"
                _lineaVariablesDType[varName] = "QuestionAnswer"
            elif value in ["No", "no", "NO", "N", "n"]:
                _lineaVariables[varName] = "No"
                _lineaVariablesDType[varName] = "QuestionAnswer"
            else:
                try:
                    parts = value.split(".")
                    module_name = ".".join(parts[:-2])  # e.g., "math.liblinea"
                    class_name = parts[-2]  # e.g., "Basic"
                    function_call = parts[-1]  # e.g., "sqrt(5)"
                    func_name, args = function_call.split("(", 1)
                    args = args.rstrip(")")# Get the module, class, and function
                    module = global_context.get(module_name)
                    if not module:
                        Linea.displayError(f"Module '{module_name}' not found")
                    cls = getattr(module, class_name)
                    func = getattr(cls(), func_name)
                    
                    # Evaluate the arguments and call the function
                    result = func(*eval(f"[{args}]"))
                    _lineaVariables[varName] = result
                except:
                    err = Error("L-E9", f"Unknown command: {value}")
                    err.displayError(err)
        except (ValueError, SyntaxError):
            err = Error("L-E2", f"Syntax Error: Invalid value in variable declaration")
            err.displayError()
            return
        
    @staticmethod
    def createDataFrame(data):
        try:
            # If data is a string representation, try to evaluate it
            if isinstance(data, str):
                data = ast.literal_eval(data)
            df = pd.DataFrame(data)
            return df
        except Exception as e:
            Linea.displayError(f"Error creating DataFrame: {str(e)}")
            return None

    @staticmethod
    def breakPhraseToWords(param, global_context = None):
        sepComp = []
        words = param.split("+")
        words = [word.strip() for word in words]
        for word in words:
            if word in _lineaActorVariables:
                sepComp.append(_lineaActorVariables[word])
            elif word in _lineaVariables:
                sepComp.append(_lineaVariables[word])
            elif (word.startswith('"') and word.endswith('"')) or (word.startswith("'") and word.endswith("'")):
                sepComp.append(word[1:-1])
            elif word.isdigit():
                sepComp.append(word)
            elif word == "@act":
                sepComp.append(Linea.displayActVars())
            elif word == "@var":
                sepComp.append(Linea.displayVars())
            elif word == "@varDType":
                sepComp.append(Linea.displayVarsDType())
            elif word == "@actDType":
                sepComp.append(Linea.displayActVarsDType())
            elif word == "getMemory":
                sepComp.append(Linea.getMemory())
            elif word == "getMem":
                sepComp.append(Linea.getMemory())
            elif word == "getMemory available":
                sepComp.append(Linea.getMemory("Available"))
            elif word == "getMem available":
                sepComp.append(Linea.getMemory("Available"))
            elif word == "getMemory used":
                sepComp.append(Linea.getMemory("Used"))
            elif word == "getMem used":
                sepComp.append(Linea.getMemory("Used"))
            elif word == "getMemory all":
                sepComp.append(Linea.getMemory("All"))
            elif word == "getMem all":
                sepComp.append(Linea.getMemory("All"))
            elif word == "getMemory usage":
                sepComp.append(Linea.getMemory("MemoryUsage"))
            elif word == "getMem usage":
                sepComp.append(Linea.getMemory("MemoryUsage"))
            elif word == "getMemory free":
                sepComp.append(Linea.getMemory("Free"))
            elif word == "getMem free":
                sepComp.append(Linea.getMemory("Free"))
            else:
                try:
                    parts = word.split(".")
                    module_name = ".".join(parts[:-2])  # e.g., "math.liblinea"
                    class_name = parts[-2]  # e.g., "Basic"
                    function_call = parts[-1]  # e.g., "sqrt(5)"
                    func_name, args = function_call.split("(", 1)
                    args = args.rstrip(")")# Get the module, class, and function
                    module = global_context.get(module_name)
                    if not module:
                        Linea.displayError(f"Module '{module_name}' not found")
                    cls = getattr(module, class_name)
                    func = getattr(cls(), func_name)
                    
                    # Evaluate the arguments and call the function
                    result = func(*eval(f"[{args}]"))
                    sepComp.append(result)
                except:
                    err = Error("L-E9", f"Unknown command: {word}")
                    err.displayError(err)
        return "".join(map(str, sepComp))
    
    @staticmethod
    def varUpdate(varName, value, global_context = None):
        if varName not in _lineaVariables:
            err = Error("L-E1", f"Syntax Error: Variable '{varName}' not found")
            err.displayError()
            Linea.displayWarning(f"Variable Name: {varName}. To declare a new variable, use `var`")
            return
        try:
            if value in _lineaVariables.keys():
                _lineaVariables[varName] = _lineaVariables[value]
                _lineaVariablesDType[varName] = _lineaVariablesDType[value]
            elif value.isdigit():
                _lineaVariables[varName] = int(value)
                _lineaVariablesDType[varName] = "Integer"
            elif value.replace(".", "", 1).isdigit():
                _lineaVariables[varName] = float(value)
                _lineaVariablesDType[varName] = "Floating Point"
            elif value.startswith('"') and value.endswith('"'):
                _lineaVariables[varName] = value[1:-1]
                _lineaVariablesDType[varName] = "String"
            elif value.startswith("'") and value.endswith("'"):
                _lineaVariables[varName] = value[1:-1]
                _lineaVariablesDType[varName] = "String"
            elif value.startswith("[") and value.endswith("]"):
                import ast
                _lineaVariables[varName] = ast.literal_eval(value)
                _lineaVariablesDType[varName] = "Array"
            elif value == "True":
                _lineaVariables[varName] = True
                _lineaVariablesDType[varName] = "Boolean"
            elif value == "False":
                _lineaVariables[varName] = False
                _lineaVariablesDType[varName] = "Boolean"
            elif value in ["None", "NULL", "NIL", "undefined"]:
                _lineaVariables[varName] = None
                _lineaVariablesDType[varName] = "None"
            elif value in ["Yes", "yes", "YES", "Y", "y"]:
                _lineaVariables[varName] = True
                _lineaVariablesDType[varName] = "QuestionAnswer"
            elif value in ["No", "no", "NO", "N", "n"]:
                _lineaVariables[varName] = False
                _lineaVariablesDType[varName] = "QuestionAnswer"
            else:
                try:
                    parts = value.split(".")
                    module_name = ".".join(parts[:-2])  # e.g., "math.liblinea"
                    class_name = parts[-2]  # e.g., "Basic"
                    function_call = parts[-1]  # e.g., "sqrt(5)"
                    func_name, args = function_call.split("(", 1)
                    args = args.rstrip(")")# Get the module, class, and function
                    module = global_context.get(module_name)
                    if not module:
                        Linea.displayError(f"Module '{module_name}' not found")
                    cls = getattr(module, class_name)
                    func = getattr(cls(), func_name)
                    
                    # Evaluate the arguments and call the function
                    result = func(*eval(f"[{args}]"))
                    _lineaVariables[varName] = result
                except:
                    err = Error("L-E2", f"Syntax Error: Invalid value in variable declaration")
                    err.displayError(err)
                    return
        except (ValueError, SyntaxError):
            err = Error("L-E2", f"Syntax Error: Invalid value in variable declaration")
            err.displayError()
            return
        
    @staticmethod
    def varKill(varName):
        if varName == "":
            _lineaVariables.clear()
            _lineaVariablesDType.clear()
        elif varName in _lineaVariables:
            del _lineaVariables[varName]
            del _lineaVariablesDType[varName]
        else:
            err = Error("L-E1", f"Syntax Error: Variable '{varName}' not found")
            err.displayError()
            Linea.displayWarning(f"Variable Name: {varName}. To declare a new variable, use `var`")
        return
    
    @staticmethod
    def killAll():
        _lineaVariables.clear()
        _lineaVariablesDType.clear()
        _lineaActorVariables.clear()
        _lineaActorVariablesDType.clear()
        return
    
    @staticmethod
    def address(param):
        varName = param.strip()
        if varName in _lineaVariables:
            address = hex(id(_lineaVariables[varName]))
            print(address)
        else:
            err = Error("L-E1", f"Syntax Error: Variable '{varName}' not found")
            err.displayError()
            Linea.displayWarning(f"Variable Name: {varName}. To declare a new variable, use `var`")
            return
    
    @staticmethod
    def typeCast(param):
        varName, toType = param.split("=", 1)
        varName = varName.strip()
        toType = toType.strip()
        if varName not in _lineaVariables:
            err = Error("L-E1", f"Syntax Error: Variable '{varName}' not found")
            err.displayError()
            Linea.displayWarning(f"Variable Name: {varName}. To declare a new variable, use `var`")
            return
        try:
            if toType == "int":
                _lineaVariables[varName] = int(_lineaVariables[varName])
                _lineaVariablesDType[varName] = "Integer"
            elif toType == "float":
                _lineaVariables[varName] = float(_lineaVariables[varName])
                _lineaVariablesDType[varName] = "Floating Point"
            elif toType == "str":
                _lineaVariables[varName] = str(_lineaVariables[varName])
                _lineaVariablesDType[varName] = "String"
            elif toType == "bool":
                _lineaVariables[varName] = bool(_lineaVariables[varName])
                _lineaVariablesDType[varName] = "Boolean"
            else:
                err = Error("L-E3", f"Syntax Error: Invalid type '{toType}'")
        except (ValueError, SyntaxError):
            err = Error("L-E2", f"Syntax Error: Invalid value in variable declaration")
            err.displayError()
            return

    @staticmethod
    def varArray(param):
        varDec, varArrayValue = param.split("=", 1)
        varName = varDec.strip()
        varArrayValue = varArrayValue.strip()
        varArrayValueArray = [i.strip() for i in varArrayValue.split(",")]
        _lineaVariables[varName] = varArrayValueArray
        for i in range(0, len(varArrayValueArray)):
            if varArrayValueArray[i].isdigit():
                _lineaVariables[varName][i] = int(varArrayValueArray[i])
            elif varArrayValueArray[i] in _lineaActorVariables:
                _lineaVariables[varName][i] = _lineaActorVariables[varArrayValueArray[i]]
            elif varArrayValueArray[i] in _lineaVariables:
                _lineaVariables[varName][i] = _lineaVariables[varArrayValueArray[i]]
            else:
                if varArrayValueArray[i].startswith('"') and varArrayValueArray[i].endswith('"') or varArrayValueArray[i].startswith("'") and varArrayValueArray[i].endswith("'"):
                    _lineaVariables[varName][i] = varArrayValueArray[i][1:-1]
                elif varArrayValueArray[i] == "True" or varArrayValueArray[i] == "False" or varArrayValueArray[i] == "true" or varArrayValueArray[i] == "false":
                    _lineaVariables[varName][i] = varArrayValueArray[i].upper()
                elif varArrayValueArray[i] == "NULL" or varArrayValueArray[i] == "NILL" or varArrayValueArray[i] == "null" or varArrayValueArray[i] == "nill" or varArrayValueArray[i] == "None" or varArrayValueArray[i] == "none":
                    _lineaVariables[varName][i] = None
                elif "." in varArrayValueArray[i] and varArrayValueArray[i] not in floatNotCase:
                    pointCount = 0
                    for j in range(0, len(varArrayValueArray[i])):
                        if varArrayValueArray[i][j] == ".":
                            pointCount += 1
                        else:
                            pass
                    if pointCount == 1:
                        try:
                            _lineaVariables[varName][i] = float(varArrayValueArray[i])
                        except:
                            err = Error("L-E2", f"Syntax Error: Invalid value in variable declaration")
                            err.displayError()
                    else:
                        err = Error("L-E2", f"Syntax Error: Invalid value in variable declaration")
                        err.displayError()
                else:
                    err = Error("L-E2", f"Syntax Error: Invalid value in variable declaration")
                    err.displayError()

    
    @staticmethod
    def forLoop(param):
        iteratorVar, forCommand, times, action = param.split(" ", 3)
        iteratorVar = iteratorVar.strip()
        forCommand = forCommand.strip()
        times = times.strip()
        action = action.strip()
        if forCommand == "from":
            start, end = times.split("~")
            start = int(start)
            end = int(end)
            for i in range(start, end + 1):
                if action.startswith("display->"):
                    Linea.display(Linea.breakPhraseToWords(action[9:]))
                elif action.startswith("var->"):
                    Linea.varDeclare(action[5:])
                elif action.startswith("varUpd->"):
                    Linea.varUpd(action[8:])
                elif action.startswith("var[]->"):
                    Linea.varArray(action[7:])
                elif action.startswith("typecast->"):
                    Linea.typeCast(action[10:])
                elif action.startswith("bin->"):
                    bin(action[5:])
                elif action.startswith("hex->"):
                    hex(action[5:])
                elif action.startswith("oct->"):
                    oct(action[5:])
                elif action.startswith("varops->"):
                    Linea.varOps(action[8:])
                else:
                    err = Error("L-E4", f"Invalid operation in for loop")
                    err.displayError()
        elif forCommand == "till":
            times = int(times)
            for i in range(0, times + 1):
                if action.startswith("display->"):
                    Linea.display(Linea.breakPhraseToWords(action[9:]))
                elif action.startswith("var->"):
                    Linea.varDeclare(action[5:])
                elif action.startswith("varUpd->"):
                    Linea.varUpd(action[8:])
                elif action.startswith("var[]->"):
                    Linea.varArray(action[7:])
                elif action.startswith("typecast->"):
                    Linea.typeCast(action[10:])
                elif action.startswith("bin->"):
                    bin(action[5:])
                elif action.startswith("hex->"):
                    hex(action[5:])
                elif action.startswith("oct->"):
                    oct(action[5:])
                elif action.startswith("varops->"):
                    Linea.varOps(action[8:])
                else:
                    err = Error("L-E4", f"Invalid operation in for loop")
                    err.displayError()
        elif forCommand == "noDuckTill":
            times = int(times)
            for i in range(1, times + 1):
                if action.startswith("display->"):
                    Linea.display(Linea.breakPhraseToWords(action[9:]))
                elif action.startswith("var->"):
                    Linea.varDeclare(action[5:])
                elif action.startswith("varUpd->"):
                    Linea.varUpd(action[8:])
                elif action.startswith("var[]->"):
                    Linea.varArray(action[7:])
                elif action.startswith("typecast->"):
                    Linea.typeCast(action[10:])
                elif action.startswith("bin->"):
                    bin(action[5:])
                elif action.startswith("hex->"):
                    hex(action[5:])
                elif action.startswith("oct->"):
                    oct(action[5:])
                elif action.startswith("varops->"):
                    Linea.varOps(action[8:])
                else:
                    err = Error("L-E4", f"Invalid operation in for loop")
                    err.displayError()
        else:
            err = Error("L-E4", f"Invalid for loop command")
            err.displayError()

    @staticmethod
    def getMemory(param = "All"):
        mem = psutil.virtual_memory()
        total_memory = mem.total / (1024 ** 3)
        available_memory = mem.available / (1024 ** 3)
        used_memory = mem.used / (1024 ** 3)
        memory_percent = mem.percent
        if param == "All":
            return f"Total Memory: {total_memory:.2f} GB\nAvailable Memory: {available_memory:.2f} GB\nUsed Memory: {used_memory:.2f} GB\nMemory Usage: {memory_percent}%\n"
        elif param == "Total":
            return f"{total_memory:.2f} GB\n"
        elif param == "Available":
            return f"{available_memory:.2f} GB\n"
        elif param == "Used":
            return f"{used_memory:.2f} GB\n"
        elif param == "Free":
            return f"{mem.free / (1024 ** 3):.2f} GB\n"
        elif param == "MemoryUsage":
            return f"{memory_percent}%\n"
        else:
            return f"Invalid parameter {param}. Use 'All', 'Total', 'Available', 'Used', or 'MemoryUsage'."

    @staticmethod
    def exit():
        Linea.killAll()
        sys.exit(0)

# LSP Class

class LSP(Linea):
    @staticmethod
    def displayLSP(param):
        return param
    
    @staticmethod
    def removeTagsFromLSPCode(LSPCode):
        if "<?lsp" not in LSPCode or "?>" not in LSPCode:
            return "Syntax Error: Missing LSP tags"
        LSPCode = LSPCode.replace("<?lsp", "")
        LSPCode = LSPCode.replace("?>", "")
        LSPCode = LSPCode.strip()
        return LSPCode
    
    @staticmethod
    def evaluate(param):
        terms = param.split(" ")
        terms = [term.strip() for term in terms]
        for i in range(len(terms)):
            if terms[i] in _lspVariables:
                terms[i] = _lspVariables[terms[i]]
            elif terms[i].isdigit():
                terms[i] = int(terms[i])
            elif terms[i] in operators:
                continue
            else:
                return f"Syntax Error: Variable '{terms[i]}' not found"
        return eval(" ".join([str(term) for term in terms]))

    def runJavaScript(param):
        if param.startswith("get.element.id "):
            return f'<script>document.getElementById("{param[15:]}")</script>'
        elif param.startswith("get.element.id.value "):
            return f'<script>document.getElementById("{param[21:]}").value</script>'
        elif param.startswith("get.element.id.innerHTML "):
            return f'<script>document.getElementById("{param[26:]}").innerHTML</script>'
        elif param.startswith("get.element.id.innerText "):
            return f'<script>document.getElementById("{param[25:]}").innerText</script>'
        elif param.startswith("get.element.class "):
            return f'<script>document.getElementsByClassName("{param[18:]}")</script>'
        elif param.startswith("get.element.tag "):
            return f'<script>document.getElementsByTagName("{param[16:]}")</script>'
        elif param.startswith("get.element.name "):
            return f'<script>document.getElementsByName("{param[17:]}")</script>'
        elif param.startswith("get.element.query "):
            return f'<script>document.querySelector("{param[18:]}")</script>'
        elif param.startswith("get.element.queryAll "):
            return f'<script>document.querySelectorAll("{param[21:]}")</script>'
        elif param.startswith("log "):
            return f'<script>console.log("{param[4:]}")</script>'
        else:
            return f"Syntax Error: Unknown LSP JavaScript '{param}'"

    @staticmethod
    def breakPhraseToWords(param):
        sepComp = []
        words = param.split("+")
        words = [word.strip() for word in words]
        for word in words:
            if word in _lspVariables:
                sepComp.append(_lspVariables[word])
            elif (word.startswith('"') and word.endswith('"')) or (word.startswith("'") and word.endswith("'")):
                sepComp.append(word[1:-1])
            elif word.isdigit():
                sepComp.append(word)
            else:
                return f"<h1 style='color: red;'>Syntax Error: Variable '{word}' not found</h1>"
        return "".join(map(str, sepComp))

    @staticmethod
    def varDeclare(varName, value):
        if varName in _lspVariables:
            return f"<h1 style='color: red;'>Syntax Error: Variable already declared</h1>\n<h2 style='color: yellow;'>Variable Name: {varName}. To update its value, use `varUpd`</h2>"
        try:
            if value in _lspVariables.keys():
                _lspVariables[varName] = _lspVariables[value]
                _lspVariablesDType[varName] = _lspVariablesDType[value]
            elif value.isdigit():
                _lspVariables[varName] = int(value)
                _lspVariablesDType[varName] = "Integer"
            elif value.replace(".", "", 1).isdigit():
                _lspVariables[varName] = float(value)
                _lspVariablesDType[varName] = "Floating Point"
            elif value.startswith('"') and value.endswith('"'):
                _lspVariables[varName] = value[1:-1]
                _lspVariablesDType[varName] = "String"
            elif value.startswith("'") and value.endswith("'"):
                _lspVariables[varName] = value[1:-1]
                _lspVariablesDType[varName] = "String"
            elif value.startswith("[") and value.endswith("]"):
                import ast
                _lspVariables[varName] = ast.literal_eval(value)
                _lspVariablesDType[varName] = "Array"
            elif value == "True":
                _lspVariables[varName] = True
                _lspVariablesDType[varName] = "Boolean"
            elif value == "False":
                _lspVariables[varName] = False
                _lspVariablesDType[varName] = "Boolean"
            elif value in ["None", "NULL", "NIL", "undefined"]:
                _lspVariables[varName] = None
                _lspVariablesDType[varName] = "None"
            elif value in ["Yes", "yes", "YES", "Y", "y"]:
                _lspVariables[varName] = True
                _lspVariablesDType[varName] = "QuestionAnswer"
            elif value in ["No", "no", "NO", "N", "n"]:
                _lspVariables[varName] = False
                _lspVariablesDType[varName] = "QuestionAnswer"
            else:
                return "<h1 style='color: red;'>Syntax Error: Invalid value in variable declaration</h1>"
        except (ValueError, SyntaxError):
            return "<h1 style='color: red;'>Syntax Error: Invalid value in variable declaration</h1>"
        
    def display(param):
        return param
    

# Error Class

class Error(Linea):
    def __init__(self, errorCode, errorMessage):
        self.errorCode = errorCode
        self.errorMessage = errorMessage

    @staticmethod
    def errCodes():
        return {
            "L-E1": "Variable not found",
            "L-E2": "Invalid value in variable declaration",
            "L-E3": "Invalid type",
            "L-E4": "Invalid operation",
            "L-E5": "Variable already declared",
            "L-E6": "Actor not found",
            "L-E7": "Invalid operator",
            "L-E8": "Division by zero",
            "L-E9": "Unknown command",
            "L-E10": "Module not found",
        }

    @staticmethod
    def displayError(self):
        print(f"{RED}Error Code: {self.errorCode}, Error Message: {self.errorMessage}{END}")