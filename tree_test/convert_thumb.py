# import ffmpeg
import subprocess

def convert_mov_to_seq():
    input = r"C:\Users\jin91\PipelineTD\git\images\test.mp4"
    output = r"C:\Users\jin91\Documents\ShotGrid\show\oksusu\tmp\thumb\test.%4e.jpg"

    cmd = f'ffmpeg -i "{input}" "{output}"'
    print(cmd)
    subprocess.check_output(cmd, shell=True)

convert_mov_to_seq()

