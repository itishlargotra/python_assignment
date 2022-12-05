import requests
import json

User ='itishlargotra'
base_url = "https://api.github.com/"
url = f"https://api.github.com/users/{User}/repos"
token= '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'
data = {"type" : "all" , "sort" : "full_name" , "direction" : "asc"}
headers = {
    "Authorization":f"token {token}",
    "Accept":"application/vnd.github.mercy-preview+json"
}
reponame= 'Python_requests_assignment'

# #GET REQUESTS
# output = requests.get(url,data=json.dumps(data))
# for project in output.json():
#     print(f"Project Name: {project['name']}\nProject URL    {project['html_url']}\n")  


#post request CREATING A  Repo
# print('\n \n testing the POST request') 
# header = {"Authorization":f"token {token}"}
# data = {f"name": f"{reponame}"}
# output = requests.post(base_url + "user/repos" + "" , data=json.dumps(data), headers=header)
# print(output)

# if output.status_code == 201:
#   print(f"Repo named {reponame} Successfully created")
# else:
#   print("ERROR, Repo Not created")


# #delete request DELETING A REPO 
# url = f"https://api.github.com/repos/{User}/{reponame}"
# output=requests.delete(url,headers=headers)
# print(output)

# if output.status_code == 204:
#   print(f"Repo named {reponame} Successfully deleted")
# else:
#   print("ERROR, Repo can't be deleted")

# #updating the file
# print('\n\n testing the PATCH request') 
header = {"Authorization":f"token {token}"}
# data = {"has_wiki": 'false'}
# output = requests.patch(base_url + f"repos/{User}/{reponame}" , data=json.dumps(data), headers=header)
# print(output)

# if output.status_code == 200:
#   print(f"Patch request successfully implemented")
# else:
#   print("ERROR,patch request unsuccessful")


# print('\n\n testing the PUT request')
# collaborator_name = 'sachinkayy'
# output = requests.put(base_url + f"repos/{User}/{reponame}/collaborators/{collaborator_name}", headers=header)
# print(output)

# if output.status_code == 201:
#   print(f"Collaborator request successfully sent to {collaborator_name} for REPO:{reponame} ")
# else:
#   print("ERROR, Collaborator Not added")