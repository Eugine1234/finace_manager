import csv
MONTH = 'june'

def finance_manager(file):
    sum = 0
    transaction = []
    with open(file,mode ='r')as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        for row in csv_reader:
            name = row[4]
            amount = float(row[1])
            date = row[1]
            transaction = (date, name, amount)
            sum += amount
            transaction.append(transaction)
            print(f"The sum of your transaction this month is{sum}")
            print('')
            return transaction
        print(finance_manager(f'muzo_{MONTH}.csv'))

    