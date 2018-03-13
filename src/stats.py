import requests
from functools import reduce
from flask import abort

def merge_languages(languages_a, languages_b):
  return list(set(languages_a + languages_b))

def filter_repos(repo):
  return repo['fork'] == False

def map_repos(repo):
  return {
    'stars': repo['stargazers_count'],
    'issues': repo['open_issues_count'],
    'forks': repo['forks_count'],
    'languages': [repo['language']]
  }

def reduce_repos(repo_a, repo_b):
  return {
    'stars': repo_a['stars'] + repo_b['stars'],
    'issues': repo_a['issues'] + repo_b['issues'],
    'forks': repo_a['forks'] + repo_b['forks'],
    'languages': merge_languages(repo_a['languages'], repo_b['languages'])
  }

def get_stats(repo_list):
  return reduce(reduce_repos, map(lambda x: map_repos(x), filter(filter_repos, repo_list)))