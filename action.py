import os
from github import Github
from github.GithubException import BadCredentialsException

def greet(who):
    print(f"Hello, {who}!")

def main():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN environment variable not set. Exiting.")
        return

    try:
        github = Github(token)
        repo = github.get_repo(os.getenv("GITHUB_REPOSITORY"))
        who_to_greet = os.getenv("INPUT_WHO-TO-GREET", "World")
        greet(who_to_greet)
    except BadCredentialsException:
        print("Invalid GitHub token provided. Exiting.")

if __name__ == "__main__":
    main()
