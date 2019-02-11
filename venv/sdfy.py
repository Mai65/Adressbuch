import csv
from fdfgen import forge_fdf
import os
import sys

sys.path.insert(0, os.getcwd())
filename_prefix = "NVC"
csv_file = "NVC.csv"
pdf_file = "NVC.pdf"
tmp_file = "tmp.fdf"
output_folder = './output/'

def process_csv(file):
    headers = []
    data =  []
    csv_data = csv.reader(open(file))
    for i, row in enumerate(csv_data):
      if i == 0:
        headers = row
        continue;
      field = []
      for i in range(len(headers)):
        field.append((headers[i], row[i]))
      data.append(field)
    return data

