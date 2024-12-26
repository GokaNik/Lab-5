import re
import csv


input_file = "task3.txt"
output_file = "task3.csv"

pattern_id = r"\b\d+\b"
pattern_name = r"\b[A-Z][a-z]+\b"
pattern_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
pattern_date = r"\b\d{4}-\d{2}-\d{2}\b"
pattern_website = r"https?://[^\s]+"

with open(input_file, "r", encoding="utf-8") as file:
    data = file.read()

ids = re.findall(pattern_id, data)
names = re.findall(pattern_name, data)
emails = re.findall(pattern_email, data)
dates = re.findall(pattern_date, data)
websites = re.findall(pattern_website, data)

print(f"ID: {ids[:5]}")
print(f"Фамилии: {names[:5]}")
print(f"Почты: {emails[:5]}")
print(f"Даты: {dates[:5]}")
print(f"Сайты: {websites[:5]}")


with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["ID", "Фамилия", "Электронная почта", "Дата регистрации", "Сайт"])
    for row in zip(ids, names, emails, dates, websites):
        csvwriter.writerow(row)

print(f"Файл сохранен как {output_file}")
