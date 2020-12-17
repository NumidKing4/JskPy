from os import rename
from os import system as shell_execute
from sys import platform, executable

__name__ = "\x4a\x73\x6b\x50\x79\x2e\x70\x79"
__description__ = "Jsk Troll's Python toolkit to handle both Python and system packages + additional helpful functions ;) "
if not __name__ in __file__:
	rename(__file__, __name__)
	message = "Try again."
	raise Exception(message)

def shell_response(command):
	from os import popen
	output = popen(command).read()
	if not output: # if output gives error message
		from sys import stdout
		stdout.write("\033[F\033[K") # clear error message
		stdout.flush() # makes sure error message is cleared
	return output

if "linux" in platform:
	isTermux = shell_response("termux-info")
	if isTermux:
		platform = "termux"

class yella:
	# a class that contains static methods used to check if a variable/module/package is installed/exists
	# system packages manager
	if platform=="win32" :
		package_manager = False
	elif shell_response("apt-get")=="":
		package_manager = False
	else:
		package_manager = True
	@staticmethod
	def module(name):
		# 	Usage Example : print(yella.module("colorama"))
		# 	checks if module is installed
		try:
			exec(f"import {name}")
			exec(f"del {name}")
			isInstalled = True
		except:
			isInstalled = False
		return isInstalled
	# -- #
	@staticmethod
	def package(pkgName):
		#		checks if package is installed
		# 	Usage Example : 	print(yella.package("apache2"))
		if not yella.package_manager: raise Exception("Your OS has no package manager.")
		pkgInfo = shell_response(f"dpkg -s {pkgName}")
		if "ok" in pkgInfo:
			return True
		else:
			return False
	# -- #


def install_modules(*Modules, **kwargs):
	#			installs module 
	#	 Usage Example : install_modules("colorama", check=False)
	#  	 <check> is an optional argument used to check if Modules are successfully installed. Possible values : (True, False). Default Value is False
	#	You can also enter multiple arguments like :
	#									 install_modules("git", "kivy", "os")
	if "check" not in kwargs:
		kwargs["check"] = False
	global executable
	if ' ' in executable:
		executable = '"' + executable + '"'
	for Module in Modules:
		installer = shell_response("{} -m pip install {}".format(executable, Module))
		if kwargs["check"]:
			if not yella.module(Module):
				raise Exception(f"[!] - PIP Could not install {Module} correctly.\n\n{installer}")


def importf(*libs):
	"""
			This function force-imports modules
					(imports already installed modules and installs+imports uninstalled ones)
						
					 How to use :			
						 		 	  from JskPy import *
									  importf(modules)     	  
									  from JskPy import *   	# THIS LINE IS NECESSARY AFTER CALLING THE <importf> FUNCTION
							
		Examples : importf("math") 	 							(One argument)
				   importf("re", "sys")							(Multiple arguments)
		
		IMPORTANT NOTES : 	Module names should be strings
													It only works if you write again from JskPy import *
	
	"""
	for lib in libs:
		if type(lib)!=str:
			raise TypeError("[!] - Pass modules as strings, not variables.")
		if not yella.module(lib):
			print(f"{lib} module not found.")
			print(f"Installing {lib} module...\n")
			install_modules(lib)
		globals()[lib] = __import__(lib)
	
	if len(libs) != 1:
		print(f"\nModules {libs} imported successfully !")
	else:
		print(f"\nModule {libs[0]} imported successfully !")


def pkg_install(*pkgArray):
	#		installs packages
	# 	Usage Example : 	JskPy.pkg_install("git")
	#	  This function allows multiple arguments
	if not yella.package_manager(): raise Exception("Your OS has no package manager.")
	print("Checking for updates...")
	shell_execute("apt-get upgrade")
	for pkgName in pkgArray:
		if not package(pkgName):
			shell_execute(f"apt-get install {pkgName}")
			print(f"{pkgName} installed successfully.")
		else:
			print(f"{pkgName} is already installed.")


