def transform_date(data):
    if '-' in str(data) and len(str(data)) == 10:
        return str(data).split('-')[2] + "/" + str(data).split('-')[1] + "/" + str(data).split('-')[0]
    else:
        return ""