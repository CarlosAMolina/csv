import csv

def read_csv():
    with open('file.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="|", quotechar='"', escapechar="\\")
        column_names = None
        number_of_colums = None
        for index, row in enumerate(csv_reader):
            if index == 0:
                column_names = row
                number_of_colums = len(column_names)
                print(f'Column names ({number_of_colums}): {", ".join(column_names)}')
            else:
                #for name, value in zip(column_names, row):
                #    print(name, value)
                print(f"Row (length: {len(row)}):", row)
                assert number_of_colums == len(row)


if __name__ == "__main__":
    read_csv()
