import getpass
from installMissingModules import *
try:
    from git import Repo
except:
    install("gitpython")
    speak('I am missing the gitpython module')

userAccount = getpass.getuser()
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

    # except:
        # print('Some error occured while pushing the code')


def uploadToGit():
    try:
        git_push()
        speak("Upload was successful")
    except:
        speak("An error occured, gonna try again")
        git_push()

