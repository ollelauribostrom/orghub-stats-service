from src.stats import merge_languages, is_standalone, transform_repo, combine_repos

def test_merge_languages():
  a = ['Python', 'JavaScript']
  b = ['Python', 'Java']
  merged = merge_languages(a, b)
  assert len(merged) == 3
  assert 'Python' in merged
  assert 'JavaScript' in merged
  assert 'Java' in merged

def test_is_standalone():
  a = { 'fork': True }
  b = { 'fork': False }
  c = { }
  assert is_standalone(a) == False
  assert is_standalone(b) == True
  assert is_standalone(c) == True

def test_transform_repo():
  repo = { 
    'stargazers_count': 0,
    'open_issues_count': 0,
    'forks_count': 0,
    'language': ['Python']
  }
  transformedRepo = transform_repo(repo)
  assert 'stars' in transformedRepo
  assert 'issues' in transformedRepo
  assert 'forks' in transformedRepo
  assert 'languages' in transformedRepo

def test_combine_repos():
  a = { 'stars': 1, 'issues': 1, 'forks': 1, 'languages': ['JavaScript'] }
  b = { 'stars': 1, 'issues': 1, 'forks': 1, 'languages': ['Python'] }
  reduced = combine_repos(a, b)
  assert reduced['stars'] == 2
  assert reduced['issues'] == 2
  assert reduced['forks'] == 2
  assert len(reduced['languages']) == 2