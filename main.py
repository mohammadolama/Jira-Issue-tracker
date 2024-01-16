import requests
import pandas as pd
import json
import os
from flatten_json import flatten


print("This is a basic app to interact with Apache issue tracker")
while True:
    print("please enter your issue key: (enter 'exit' to quit)")
    inp = input()
    if inp == "exit":
        break
    else:
        try:
            os.mkdir("results/" + inp)
        except OSError as error:
            pass

        api_url = "https://issues.apache.org/jira/rest/api/2/issue/" + inp
        print("Connecting to Jira ..." + api_url)
        response = requests.get(api_url)
        r = response.content
        data = json.loads(r)
        data1 = pd.json_normalize(data)
        data1.to_excel('results/' + inp + '/output.xlsx', index=False)
        data1.to_csv('results/' + inp + '/output.csv', index=False)
        j = response.json()
        with open("results/" + inp + "/output.json", "w") as write_file:
            json.dump(j, write_file, indent=4)

        flat = flatten(j)
        with open("results/" + inp + "/output_flat.json", "w") as write_file:
            json.dump(flat, write_file, indent=4)
        print("The data is saved in results/" + inp + "in 4 different formats: json, csv, xlsx, and flat json.")




