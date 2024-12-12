import subprocess
from multiprocessing import Pool
import subprocess
import os

design_name = ["ispd18_test5", "ispd18_test8", "ispd18_test10", "ispd19_test7", "ispd19_test8", "ispd19_test9"]
# design_name = ["ispd18_test5", "ispd18_test8", "ispd18_test10"]


def run_command(command):
    subprocess.run(command, shell=True, capture_output=True, text=True)
def run_gr():
    commands = []
    os.makedirs(f'./guide/', exist_ok=True)
    os.makedirs(f'./gr_logs/', exist_ok=True)
    for i in range(len(design_name)):
        command1 = f"./build/route -lef /data/hdliu21/workspace/RRP/dataset/{design_name[i]}/{design_name[i]}.input.lef \
        -def /data/hdliu21/workspace/RRP/dataset/{design_name[i]}/{design_name[i]}.input.def \
        -output ./guide/{design_name[i]}.solution.guide \
        -threads 1 \
        | tee ./gr_logs/{design_name[i]}.gr.log"
        print(command1)
        commands.append(command1)

        command2 = f"./build/route -lef /data/hdliu21/workspace/RRP/dataset/{design_name[i]}_metal5/{design_name[i]}_metal5.input.lef \
        -def /data/hdliu21/workspace/RRP/dataset/{design_name[i]}_metal5/{design_name[i]}_metal5.input.def \
        -output ./guide/{design_name[i]}_metal5.solution.guide \
        -threads 1 \
        | tee ./gr_logs/{design_name[i]}_metal5.gr.log"
        print(command2)
        commands.append(command2)

    # Run commands sequentially
    # for command in commands:
    #     run_command(command)
    # Run commands in parallel
    with Pool(processes=len(commands)) as pool:
        pool.map(run_command, commands)

if __name__ == '__main__':
    run_gr()
# Run commands in parallel
# with Pool(processes=len(commands)) as pool:
#     pool.map(run_command, commands)
