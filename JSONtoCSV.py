# This code reads data from a JSON file named "input.json", converts it into a CSV format, and saves
# it in a file named "output.csv". The code uses the `json` module to load the data from the JSON file
# and then iterates over each object in the data to create a CSV string. The CSV string is then
# written to the "output.csv" file. If any error occurs during the process, it will be caught and
# printed as an error message.
import json
if__name__== '__main__':
try:
        with open('input.json','r') as f :
            data = json.loads(f.read())
        output = ','.join([*data[0]])
        for obj in data:
            output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'
        with open('output.csv', 'w')as f:
            f.write(output)
except Exception as ex:
        print(f'Error: {str(ex)}')
        