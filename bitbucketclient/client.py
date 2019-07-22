import git


class Client:
  BASE_URL = 'https://{username}:{app_password}@bitbucket.org/{owner}/{repository}.git'

  def __init__(self, username, app_password, owner, local_path):
    self.username = username
    self.app_password = app_password
    self.owner = owner
    self.local_path = local_path

  def clone(self, repository, branch='master'):
    """

    clone repository
    :param repository:
    :param branch:
    :return:
    """
    try:
      print('cloning {} ...'.format(repository))
      return git.Repo.clone_from(
        url=self.BASE_URL.format(
          username=self.username,
          app_password=self.app_password,
          owner=self.owner,
          repository=repository
        ),
        to_path=self.local_path,
        branch=branch
      )
    except git.exc.GitCommandError:
      print('duplicate repository in local path')
      return git.Repo(self.local_path)
