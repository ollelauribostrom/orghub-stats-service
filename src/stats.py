import requests
from functools import reduce
from flask import abort

def fetch_property(url, headers):
  r = requests.get(url, headers)
  if r.status_code == requests.codes.ok:
    return r.json()
  else:
    abort(r.status_code)

def reduce_dict(dict_a, dict_b):
  dict_c = dict_a.copy()
  for key, value in dict_b.items():
    if key in dict_c:
      dict_c[key] += value
    else:
      dict_c[key] = value
  return dict_c

def reduce_commits(commits_a, commits_b):
  return [x + y for x, y in zip(commits_a, commits_b)]

def filter_repos(repo):
  return repo['fork'] == False

def map_repos(repo, headers):
  commits = fetch_property('{}/stats/commit_activity'.format(repo['url']), headers)
  return {
    'stars': repo['stargazers_count'],
    'issues': repo['open_issues_count'],
    'forks': repo['forks_count'],
    'languages': fetch_property(repo['languages_url'], headers),
    'commits': map(lambda x: x['total'], commits)
  }

def reduce_repos(repo_a, repo_b):
  return {
    'stars': repo_a['stars'] + repo_b['stars'],
    'issues': repo_a['issues'] + repo_b['issues'],
    'forks': repo_a['forks'] + repo_b['forks'],
    'languages': reduce_dict(repo_a['languages'], repo_b['languages']),
    'commits': reduce_commits(repo_a['commits'], repo_b['commits'])
  }

def get_stats(repo_list, headers):
  return reduce(reduce_repos, map(lambda x: map_repos(x, headers), filter(filter_repos, repo_list)))