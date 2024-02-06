def parse_month(month):
    dictionary_month = {
        'January': '01', 'February': '02', 'March': '03', 'April': '04',
        'May': '05', 'June': '06', 'July': '07', 'August': '08',
        'September': '09', 'October': '10', 'November': '11', 'December': '12'
    }
    return dictionary_month[month]

def parse_date(full_date):
    split_date = full_date.split()
    month = parse_month(split_date[0])
    day = split_date[1][:-1].zfill(2)  # Remove comma and zero-pad day
    year = split_date[2]
    return f"{month}/{day}/{year}"

if __name__ == '__main__':
    while True:
        full_date = input("Enter a date: ")
        
        if full_date == "-1":
            break

        parsed_date = parse_date(full_date)
        print(parsed_date)
