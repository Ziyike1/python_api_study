import requests
import plotly.express as px

#执行api调用并查看响应
url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars+stars:>10000'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#将响应转换为字典
response_dict = r.json()
# print(response_dict.keys())
# print(f"Total repositories: {response_dict['total_count']}")
# print(f"Complete results: {not response_dict['incomplete_results']}")

#搜索有关仓库的信息
repo_dicts = response_dict['items']
# print(f"Repositories returned: {len(repo_dicts)}")

#研究第一个仓库
# repo_dict = repo_dicts[0]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)

#打印仓库的具体信息
# print("\nSelected information about each repository:")
# for repo_dict in repo_dicts:
#     print(f"Name: {repo_dict['name']}")
#     print(f"Owner: {repo_dict['owner']['login']}")
#     print(f"Stars: {repo_dict['stargazers_count']}")
#     print(f"Repository: {repo_dict['html_url']}")
#     print(f"Created: {repo_dict['created_at']}")
#     print(f"Updated: {repo_dict['updated_at']}")
#     print(f"Description: {repo_dict['description']}")

repo_names, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    #创建悬停文本
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)


#可视化
title = "Most-Starred Python Projects"
labels = {'x':'Repositories', 'y':'Stars'}
fig = px.bar(x=repo_names, y=stars, title=title, labels=labels, hover_name=hover_texts)
fig.update_layout(title_font_size=20, xaxis_title_font_size=10, yaxis_title_font_size=10)
fig.show()