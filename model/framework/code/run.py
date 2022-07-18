import sys
import csv
import selfies

input_file = sys.argv[1]
output_file = sys.argv[2]

smiles_list = []
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for r in reader:
        smiles_list += [r[0]]

selfies_list = []
for smi in smiles_list:
    selfies_list += [selfies.encoder(smi)]

with open(output_file, "w") as f:
    writer = csv.writer(f, delimiter= " ")
    writer.writerow(["selfies"])
    for selfie in selfies_list:
        writer.writerow([selfie])
