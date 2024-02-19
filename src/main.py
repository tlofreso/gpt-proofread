import os

github_token = os.getenv('INPUT_GITHUB-TOKEN')
openai_api_key = os.getenv('INPUT_OPENAI-API-KEY')

print(github_token,openai_api_key)