import requests

#执行api调用并查看响应
url="http://api.github.com/search/repositories"
url+="?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json" }
r = requests.post(url,headers=headers)
print(f"Status code: {r.status_code}")

#将响应转化为字典
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")
print(f"Completed results: {not response_dict['incomplete_results']}")

#探索有关仓库信息
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

#研究第一个仓库

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars:{repo_dicts['stargazers_count']}")
    print(f"Responses: {repo_dicts['html_url']}")
    print(f"Description: {repo_dict['description']}")
    print(f"\nKeys:{len(repo_dicts)}")
for key in sorted(repo_dicts.keys()):
    print(key)

#处理结果
print(response_dict.keys())
           
