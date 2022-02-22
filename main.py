import re

def arithmetic_arranger(arthmetic_list, show_answer=False):
    if not len(arthmetic_list) > 6:
        for i in arthmetic_list:
            try:
                numbers = [int(n.strip()) for n in re.split('\+|-',i)]
                for num in numbers:
                    if len(str(num)) > 4:
                        raise Exception("Error: Numbers cannot be more than four digits.")
            except:
                raise Exception("Error: Numbers must only contain digits.")
            operation = ""
            if "+" in i:
                operation = "+"
            elif "-" in i:
                operation = "-"
            else:
                raise Exception("Error: Operator must be '+' or '-'.")
            answer = eval(i)
            def createSpaces(pos, num1, num2):
                num1 = str(num1)
                num2 = str(num2)
                if pos == "top":
                    if len(num1) == len(num2):
                        return " " * (len(num2) - len(num1) + 1)
                    elif len(num2) > len(num1):
                        return " " * (len(num2) - len(num1) + 1)

                elif pos == "bottom":
                    if len(num1) > len(num2):
                        return " " * (len(num1) - len(num2))
                    else:
                        return ""
                return " "
            print(f'{createSpaces("top", numbers[0], numbers[1])} {numbers[0]}')
            print(f"{operation} {createSpaces('bottom', numbers[0], numbers[1])}{numbers[1]}")
            print("-" * (max([len(str(numbers[0])), len(str(numbers[1]))]) + 2))
            if show_answer:
                print(f"{' ' * ((max([len(str(numbers[0])), len(str(numbers[1]))]) + 2) - len(str(answer)))}{answer}")
    else:
        raise Exception("Error: Too many problems.")
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)