# 'V' after a function means its finished

# imports
import os
import shutil
import platform
import configparser

# setup
MINECRAFT_FOLDER = os.path.expanduser('~/.minecraft')

# code
class config():

	def get_versions(modloader=None): # V
		
		"""
		returns all the registered versions
		only returns mods from a specific modloader if modloader is specified
		"""
		config = configparser.ConfigParser()
		config.read('config.ini')
		if modloader == None:
			version_names = dict(config.items('versions'))
			versions = list(version_names.keys())
		else:
			for key, value in config.items('versions'):
				if key.split('_')[0] == modloader:
					version_names = dict()
					versions = list(version_names.keys())
				else:
					return False
		return version_names, versions

	def add_version(version, modloader): # V
		"""
		registers specified version as new versions
		arguments: version, modLoader
		return: True when succesfull
				False when the specified version already exists
		"""
		config = configparser.ConfigParser()
		config.read('config.ini')
		if version in config.items():
			return False
		else:
			key = f'{modloader}_{version}'
			value = f'{modloader} mods {version}'
			config.set('versions', key, value)
			with open(r'config.ini', 'w') as configfile:
				config.write(configfile)
			return True

	def rm_version(version, modloader):
		"""
		remove the specified version and the mods
		argumwnts: version, modloader
		return: True when succesful
				False when tge version doesn't exist
		"""
# -----------------------------------------------
		confirm = input(f'Are you sure you want to delete the mods for {modloader} {version}? (y/n) ')
		if confirm == 'y' or confirm == 'yes':
			versions.remove(version, modloader) # ------------
			value = f'{modloader}_{version}'
			config = configparser.ConfigParser()
			config.read('config.ini')
			config.remove_option('versions', value)
			with open(r'config.ini', 'w') as configfile:
				config.write(configfile)
			print(f'removed version {value}')
		elif confirm == 'n' or confirm == 'no':
			print('deletion canceled')

class version():

	def get_current(): # V
		with open(f'{MINECRAFT_FOLDER}/mods/version.txt', 'r') as vf:
			return vf.read().strip()

# implement version switching
# -----------------------------------------------
	def switch_to(version, modloader):
		print(f'current version: {mods.get_current_version()}')
		if version == mods.get_current_version():
			print(f'mods are already for {version}')
			return False
		else:
			for mod in mods.get_all(version, modloader):
				pass
			print(f'switching to: {version}')
# -----------------------------------------------
	
	def add(version, modloader): # V
		if os.path.isdir(f'{MINECRAFT_FOLDER}/{modloader} mods {version}') == False:
			if config.add_version(version, modloader) == True:
				os.mkdir(f'{MINECRAFT_FOLDER}/{modloader} mods {version}')
				print(f'added mods version: {modloader} {value}')
				return True
			else:
				print(f'{modloader} {version} already exists')
				return False
		else:
			return False

	def remove(version, modloader):
		pass


class mods():

	def get_all(version, modloader): # V
		mods = []
		for mod in os.listdir(f'{MINECRAFT_FOLDER}/{modloader} mods {version}'):
			mods.append(mod)
		return mods


	def add(version, modloader, mod_file, mod_name): # V
		"""
		adds a mod to a existing version, if that version doesn't exists it will be created
		arguments: 
			version: the version the mod is made for
			modloader: the modloader the mod is made for (fabric, forge)
			mod_file: the modfile thats added
			mod_name: the name of the modfile
		returns:
			True: when succesfull
			False: when unsuccesfull
		"""
		if os.path.isdir(f'{MINECRAFT_FOLDER}/{modloader} mods {version}'):
			shutil.copy2(mod_file, f'{MINECRAFT_FOLDER}/{modloader} mods {version}/{mod_name}')
			return True
		else:
			print(f'Error: failed to add {mod_file} to {modloader} {version}') 
			return False
	
	def remove(version, modloader, mod_name): # V
		"""
		removes a mod from the specified version.
		arguments: 
			version: the version the mod is in
			modloader: the modloader the mod is in (fabric, forge)
			mod_name: the name of the mod removed
		returns:
			True: when succesfull
			False: when unsuccesfull
		"""
		try:
			os.remove(f'{MINECRAFT_FOLDER}/{modloader} mods {version}/{mod_name}')
			return True
		except:
			return False

def main(): 
	
	# below are options, THEY ARE NOT ALL UPDATED!
	
	# version_names, versions = config.get_versions('fabric')
	# mods.get_all('1.18.2', 'fabric')
	# print(f'{version_names},{versions}')
	# print(cversion)
	# mods.switch_to('1.18.2')
	# config.add_version('1.18.1', 'fabric')
	# config.rm_version('1.18.2')
	# print(version.get_current())
	# mods.add()
	pass

if __name__ == '__main__':
	if platform.system() == 'Linux':
			main()
	else:
		print('This software only works on Linux systems')


# TASKS
# - implement version switching
# V implement adding mods 
# V implement removing mods
# - make a gui
# V move the folder logic from config.add_version() to version.add()
# - move the folder logic from config.rm_version() to version.remove()
