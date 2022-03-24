import getpass

userAccount = getpass.getuser()

from git import Repo

path = "C:\\Users\\"+userAccount+"\\Chaos\\.git"
PATH_OF_GIT_REPO = path  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'Chaotic update'

def git_push():
    # try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
        print("Upload was successful")
    # except:
        # print('Some error occured while pushing the code')

try:
    git_push()
except:
    print("An error occured, gonna try again")
    git_push()