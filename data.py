import numpy as np
import ast


def read_graph(filename):
    if filename == 'inputnetwork.txt':
        Cap = False
    elif filename == 'inputcapbud.txt':
        Cap = True
    else:
        exit('The input files are not correctly labelled.')
    with open(filename) as f:
        lines = f.readlines()
    f.close()

    if not Cap:
        return ast.literal_eval(lines[0])
    else:
        return ast.literal_eval(lines[0]), ast.literal_eval(lines[1])


def save_logs(filename, logs, solution=None):
    """
    Saves the solutions to the log and solutions files.
    :param filename: Filename to save the solutions to
    :param logs: The logs from the solver functions
    :param solution: The solutions from the solver functions.
    :return: None
    """
    if filename == 'lognetwork.txt':

        msg = f'The first step is to calculate the choices for the penultimate nodes. These calculations resulted in' \
              f' the following stage:\n\n{logs[-1]}\n\n'

        for i in reversed(range(len(logs))):
            if i != 0:
                msg += f'Going to the next level, the calculations for each node yields:\n{logs[i]}\n\n'

        msg += f'Finally, the cheapest path is simply traced through the solved network, making the solution:\n\n' \
               f'{solution}'

        np.savetxt(filename, [msg], fmt='%s')
        np.savetxt('solutionnetwork.txt', [str(solution)], fmt='%s')
        print('logs saved\n')

    elif filename == 'logcapbud.txt':

        max_profit, choices, total_cost, capbudlogs = solution

        msg = f'The first step is to calculate the optimal value for the first subsidiary for maximum capital of' \
              f' {capbudlogs[0]} ' \
              f', resulting in:\n\n{capbudlogs[2][0]},\nwith the associated plans:\n{capbudlogs[1][0]}\n'

        for i in range(len(capbudlogs[2])):
            if i != 0:
                msg += f'\nThe next level gives the optimal returns for the associated plans:\n{capbudlogs[2][i]},\n' \
                       f'{capbudlogs[1][i]}.\n'

        msg+=f'\nFinally, the optimal solution can be traced backwards, making the maximum return {max_profit}, for a '\
             f'total cost of {total_cost}, by using the plans {choices}.'

        solution_str = f'The maximum return was calculated as {max_profit}, for a total cost of {total_cost}, by ' \
                       f'using the plans {choices}.'

        np.savetxt(filename, [msg], fmt='%s')
        np.savetxt('solutioncapbud.txt', [solution_str], fmt='%s')
        print('\nlogs saved\n')

    else:
        exit('The output files are not correctly labelled.')
