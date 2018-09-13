class User():
	def __init__(self,frist_name,last_name,user_name):
		self.frist_name = frist_name
		self.last_name = last_name
		self.age = 0
		self.user_name = user_name
		self.login_attempts = 0

	def	describe(self):
		long_name = self.last_name.title() + ' ' + self.last_name
		print(long_name)
		print('用户名：' + self.user_name)

	def	greet_user(self):
		print('你好啊，' + self.user_name + '!')

	def	increment_login_attempts(self):
		self.login_attempts += 1

	def	reset_login_attempts(self):
		self.login_attempts = 0

class Privileges():
	def __init__(self,privileges=[]):
		self.privileges = privileges

	def show_privileges(self):
		print('管理员的权限是：')
		if self.privileges:
			for privilege in (self.privileges):
				print('-' + privilege)
		else:
			print('这个管理员没有权限')

class Admin(User):
	def __init__(self,frist_name,last_name,user_name):
		super().__init__(frist_name,last_name,user_name)
		self.privilege1 = Privileges()

admin1 = Admin('allen','barry','哈利波特')
admin1.describe()
admin1.privilege1.show_privileges()

print('添加权限')
admin1_privileges = ['can add post','can delete post','can ban user']
admin1.privilege1.privileges = admin1_privileges
admin1.privilege1.show_privileges()

user1 = User('tom','cluse','汤姆克鲁斯')
user1.describe()
user1.greet_user()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
