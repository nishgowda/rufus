from git import Repo
from datetime import datetime, timezone
import sys

class Rufus:
	# Constructor sets the directory and checks if it is a valid git repo
	def __init__(self, dir):
		try:
			self.repo = Repo(dir)
			self.dir = dir
		except:
			print('Invalid directory')
			sys.exit(1)
	
	# Returns the current active branch
	def get_current_branch(self):
		return self.repo.active_branch.name

	# Returns true if there are untracked files, false otherwise
	def has_untracked_files(self):
		return True if self.repo.untracked_files else False

	# Returns true if the last commit was within the past week, false otherwise
	def is_within_past_week(self):
		now = datetime.now(timezone.utc)
		days_different = now.date() - self.repo.head.commit.authored_datetime.date()
		return True if days_different.days < 7 else False 

	# Returns true if the last commit was authored by Rufus, false otherwise
	def is_author_rufus(self):
		return True if self.repo.head.commit.author.name == 'Rufus' else False

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print('Please enter a directory')
		sys.exit(1)
	rufus = Rufus(dir=sys.argv[1])
	print('active branch: {}'.format(rufus.get_current_branch()))
	print('local changes: {}'.format(rufus.has_untracked_files()))
	print('recent commit: {}'.format(rufus.is_within_past_week()))
	print('blame Rufus: {}'.format(rufus.is_author_rufus()))