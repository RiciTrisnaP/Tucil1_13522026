from class_definition import *
from txt_handler import *
import numpy as np

matrix,buffer,sequences = read_txt("test.txt")
matrix_cp = matrix.copy()
current_optimum = np.full([buffer.size], '??')
list_step = np.full([buffer.size,2],-1)
start_position = np.array([0,0])
direction = "horizontal"
max_weight = 0
step = 0

def solution_finder(matrix, buffer, sequences, direction, start_position, list_step, step):
    global current_optimum 
    global max_weight
    if step != buffer.size:
        if direction == "horizontal":
            direction = "vertical"
            step = step + 1
            for i in range(matrix.width):
                print("")
                print("-------------------------------------")
                matrix.print()
                buffer.print()
                sequences.print()
                print(direction)
                print(start_position)
                print(list_step)
                print(step)
                print("-------------------------------------")
                new_position = np.copy(start_position)
                new_position[1] = i
                print(new_position)
                if matrix.get_cell(new_position[0],new_position[1]) == '##':
                    print("masuk")
                    continue
                list_step[step-1] = np.array([new_position[0],new_position[1]])
                buffer.set_element(step-1,matrix.get_cell(new_position[0],new_position[1]))
                matrix.set_cell(new_position[0],new_position[1],'##')
                solution_finder(matrix, buffer, sequences, direction, new_position, list_step, step)
                matrix.set_cell(list_step[step-1][0],list_step[step-1][1],buffer.get_element(step-1))
                buffer.set_element(step-1,'??')
                list_step[step-1] = np.array([-1,-1])
                print('FJDKSLJFLDS')
                print(new_position)
                matrix.print()
        else:
            direction = "horizontal"
            step = step + 1
            for i in range(matrix.height):
                print("")
                print("-------------------------------------")
                matrix.print()
                buffer.print()
                sequences.print()
                print(direction)
                print(start_position)
                print(list_step)
                print(step)
                print("-------------------------------------")
                new_position = np.copy(start_position)
                new_position[0] = i
                print(new_position)
                if matrix.get_cell(new_position[0],new_position[1]) == '##':  
                    print("masuk")
                    continue
                list_step[step-1] = np.array([new_position[0],new_position[1]])
                buffer.set_element(step-1,matrix.get_cell(new_position[0],new_position[1]))
                matrix.set_cell(new_position[0],new_position[1],'##')
                solution_finder(matrix, buffer, sequences, direction, new_position, list_step, step)
                matrix.set_cell(list_step[step-1][0],list_step[step-1][1],buffer.get_element(step-1))
                buffer.set_element(step-1,'??')
                list_step[step-1] = np.array([-1,-1])
                print('FJDKSLJFLDS')
                print(new_position)
                matrix.print()
    else:
        print("")
        print("--------------WEIGHT---------------")
        matrix.print()
        buffer.print()
        sequences.print()
        print(direction)
        print(start_position)
        print(list_step)
        print(step)
        print("-------------------------------------")
        lol = sequences.match_all(buffer)
        print(lol)
        if lol > max_weight:
            max_weight = lol
            current_optimum = np.copy(buffer.list)
            print(current_optimum)

solution_finder(matrix,buffer,sequences,direction,start_position,list_step,step)
