import requests
import json
token = "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"

reponame = "python_assignment"

#creating repositories
base_url = "https://api.github.com/"
header = {"Authorization":f"token {token}"}
data = {f"name": f"{reponame}"}

response = requests.post(base_url + "user/repos" + "" , data=json.dumps(data), headers=header)
print(response)