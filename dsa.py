def convert_date_format(date_string):
    months = {
        'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
    }

    day, month, year = date_string.split()

    day = day[:-2]

    month = months[month]

    outputted_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"

    return outputted_date

date_string = "20th Oct 2052"
print(convert_date_format(date_string))