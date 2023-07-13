import requests
import json
import configuration as config

HEAD = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {config.TOKEN}", 
    "X-GitHub-Api-Version": "2022-11-28" 
}
def GetOrg():

    try:
        response = requests.get(url=config.BASE_URL, headers=HEAD) # revoir url= avec le self d'une classe en python
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise(SystemExit(err))

    if response.status_code == 200:
        data_b_to_str=response.content.decode('utf-8')
        json_load=json.loads(data_b_to_str)
        data_json_format=json.dumps(json_load)
    return json_load 


def GetRepositories():
    organization_details=GetOrg()
    if "repos_url" in organization_details:
        repos_url=organization_details["repos_url"]
        response=requests.get(url=repos_url,headers=HEAD)
        data_b_to_str=response.content.decode('utf-8')
        json_load=json.loads(data_b_to_str)
        expectedResult = [d for d in json_load if d['private']== True]
        data_json_format=json.dumps(expectedResult)
        print(data_json_format)

    else:
        print("pas de dépot dans cet organisation")


    

   
# def GetLogin():
#     pass






def main():
    GetRepositories()
main()