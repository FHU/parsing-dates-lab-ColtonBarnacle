def parse_month(month):
    dictionary_month = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}
    return dictionary_month[month]

def parse_date(full_date):
    dictionary_day = {'1': '01', '2': '02', '3': '03', '4': '04', '5': '05', '6': '06', '7': '07', '8': '08', '9': '09', '10': '10', '11': '11', '12': '12', '13': '13', '14': '14', '15': '15', '16': '16', '17': '17', '18': '18', '19': '19', '20': '20', '21': '21', '22': '22', '23': '23', '24': '24', '25': '25', '26': '26', '27': '27', '28': '28', '29': '29', '30': '30', '31': '31'}
    find_day = full_date.split()[1][:-1].strip()
    return dictionary_day[find_day]

if __name__ == '__main__':
    while True:
        full_date = input("Enter a date: ")
        
        if full_date == "-1":
            break

        month = parse_month(full_date.split()[0])
        day = parse_date(full_date)
        year = full_date.split()[2]
        
        print(f"{month}/{day}/{year}")
