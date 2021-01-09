import csv
#state dictionary from https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5
states = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
read_path = 'employee_data.csv'
output = []
with open(read_path) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    next(csvreader)
    for row in csvreader:
        #changes the data to the new format
        f_name, l_name = row[1].split()
        #tuple unpacking 
        year, month, day = row[2].split('-')
        dob = '/'.join([month, day, year])
        ssn = '***-**-'+row[3][-4:]
        state = states[row[4]]
        output.append([row[0], f_name, l_name, dob, ssn, state])

new_headers = ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']
with open('new_employee_data.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile,delimiter=',')
    csvwriter.writerow(new_headers)
    for row in output:
        csvwriter.writerow(row)