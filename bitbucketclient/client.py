import git


class Client:
  BASE_URL = 'https://{username}:{app_password}@bitbucket.org/{owner}/{repository}.git'

  def __init__(self, username, app_password, owner, remote='origin', local_path='./temp/repositories/{}/'):
    self.username = username
    self.app_password = app_password
    self.owner = owner
    self.remote = remote
    self.local_path = local_path

  def clone(self, repository_name, branch='master'):
    """

    clone repository
    :param repository_name:
    :param branch:
    :return:
    """
    try:
      print('cloning {} ...'.format(repository_name))
      repo = git.Repo.clone_from(
        url=self.BASE_URL.format(
          username=self.username,
          app_password=self.app_password,
          owner=self.owner,
          repository=repository_name
        ),
        to_path=self.local_path.format(repository_name),
        branch=branch
      )
      print('clone done')
      return repo
    except git.exc.GitCommandError:
      print('duplicate repository in local path')
      return git.Repo(self.local_path.format(repository_name))

  def pull(self, repository_name, branch='master'):
    """

    pull repository
    :param repository_name:
    """
    # try:
    print('pulling {} from branch {} ...'.format(repository_name, branch))
    # self.checkout(repository_name, branch)
    repo = git.Repo(self.local_path.format(repository_name))
    remote = repo.remote(self.remote)
    remote.pull(branch)
    print('pull done')

  def checkout(self, repository_name, branch='master'):
    """

    pull repository
    :param repository_name:
    """
    try:
      print('checkout {} to branch {}'.format(repository_name, branch))
      repo = git.Repo(self.local_path.format(repository_name))
      repo.git.checkout('HEAD', b=branch)
      print('checkout done')
    except git.exc.GitCommandError:
      print('A branch named {} at {} already exists.'.format(repository_name, branch))
