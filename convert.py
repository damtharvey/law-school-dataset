import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", type=str, default="law_dataset.arff")
args = parser.parse_args()

with open(args.file) as file:
    lines = file.readlines()
    
with open("law_dataset.csv", "w") as file:
    file.writelines([",".join(line.split()[1] for line in lines[1:13]) + "\n"] + lines[14:])