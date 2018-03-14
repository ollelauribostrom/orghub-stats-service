from functools import reduce

def merge_languages(languages_a, languages_b):
  return list(set(languages_a + languages_b))

def is_standalone(repo):
  if 'fork' in repo:
    return repo['fork'] is not True
  return True

def transform_repo(repo):
  return {
    'stars': repo['stargazers_count'],
    'issues': repo['open_issues_count'],
    'forks': repo['forks_count'],
    'languages': [repo['language']]
  }

def combine_repos(repo_a, repo_b):
  return {
    'stars': repo_a['stars'] + repo_b['stars'],
    'issues': repo_a['issues'] + repo_b['issues'],
    'forks': repo_a['forks'] + repo_b['forks'],
    'languages': merge_languages(repo_a['languages'], repo_b['languages'])
  }

def get_stats(repo_list):
  return reduce(combine_repos, map(lambda x: transform_repo(x), filter(is_standalone, repo_list)))