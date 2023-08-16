import pandas as pd
from mypackage.simpile_file import read_file, write_file, read_excel, write_excel


content = "Hello, this is a test content."
write_file(r"D:\ITI system admin trake\python\day4\test.txt", content)
write_file(r"D:\ITI system admin trake\python\day4\test.txt", content)
read_content = read_file(r"D:\ITI system admin trake\python\day4\test.txt")
print("Read content:", read_content)


data = {'Name': ['aya', 'mohamed', 'omar'], 'Age': [25, 30, 22]}
df = pd.DataFrame(data)
write_excel(r"D:\ITI system admin trake\python\day4\test.xlsx", df)
read_df = read_excel(r"D:\ITI system admin trake\python\day4\test.xlsx")
print("Read Excel data:\n", read_df)