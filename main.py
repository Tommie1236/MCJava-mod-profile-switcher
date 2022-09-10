# imports
import os
import shutil
import platform
import configparser

# setup
MINECRAFT_FOLDER = os.path.expanduser('~/.minecraft')

# code
class config():

	def get_profiles(modloader=None, version=None): # done but could probably be optimised/shrinked
		"""
		returns a dict of all registered profiles that match to
		the modloader, version if specified
		parameters: modloader, version  #both are set to None when not specified
		returns: profiles (list)
				 None when None exists
		"""
		config = configparser.ConfigParser()
		config.read('config.ini')
		profiles = dict(config.items('profiles'))
		if modloader == None and version == None: # if none are specified
			return profiles
		newprofiles = {} # setup empty dict for the other possibilities
		if modloader != None and version == None: # if only the modloader is specified
			for key, value in profiles.items():
				if value.split(' ')[0] == modloader:
					newprofiles[key] = value
			if newprofiles != {}:
				return newprofiles
			else:
				return None
		elif modloader == None and version != None: # if only the version is specified
			for key, value in profiles.items():
				if value.split(' ')[1] == version:
					newprofiles[key] = value
			if newprofiles != {}:
				return newprofiles
			else:
				return None
		else: # if both are specified
			for key, value in profiles.items():
				if value.split(' ')[0] == modloader and value.split(' ')[1] == version:
					newprofiles[key] = value
			if newprofiles != {}:
				return newprofiles
			else:
				return None

	def add_profile(profile_name: str, version: str, modloader: str): # Done
		"""
		registers specified profile as a new profile
		parameters: profile_name, version, modloader
		return: True when succesfull
				False when the specified version already exists
		"""
		config = configparser.ConfigParser()
		config.read('config.ini')
		if profile_name in toSingleStrKey(dict(config.items('profiles'))).keys():
			return False
		else:
			key = toDoubleStr(profile_name)
			value = f'{modloader} {version}'
			config.set('profiles', key, value)
			with open(r'config.ini', 'w') as configFile:
				config.write(configFile)
			return True
		pass

	def rm_profile(profile_name: str): # Docsting
		key = profile_name
		config = configparser.ConfigParser()
		config.read('config.ini')
		config.remove_option('profiles', key)
		with open(r'config.ini', 'w') as configfile:
			config.write(configfile)
			return True

	def get_modloader(profile_name: str): # Done
		"""
		get the modloader of the selected profile
		parameters: profile_name
		returns: (str) the modloader of the profile
		"""
		config = configparser.ConfigParser()
		config.read('config.ini')
		profile_names = toSingleStrKey(dict(config.items('profiles')))
		print(profile_names[profile_name].split(' ')[0])

	def get_version(profile_name: str):	# Done
		"""
		get the version of the selected profile
		parameters: profile_name
		returns: (str) the version of the profile
		"""
		config = configparser.ConfigParser()
		config.read('config.ini')
		profile_names = toSingleStrKey(dict(config.items('profiles')))
		print(profile_names[profile_name].split(' ')[1])


class profile():

	def get_current(): # Done
		"""
		Gets the current installed profile name, version and modloader
		Parameters: None
		Returns: profile_name (str)
				 version (str)
				 modloader (str)
		"""
		with open(f'{MINECRAFT_FOLDER}/mods/profile.txt', 'r') as pf:
			profile_name, version, modloader = pf.read().strip()
		return toSingleStr(profile_name), version, modloader

# implement version switching
# -----------------------------------------------
	def switch_to(version, modloader): # --------------------
		
		pass

		# print(f'current version: {mods.get_current_version()}')
		# if version == mods.get_current_version():
		# 	print(f'mods are already for {version}')
		# 	return False
		# else:
		# 	for mod in mods.get_all(version, modloader):
		# 		pass
		# 	print(f'switching to: {version}')
# -----------------------------------------------
	
	def add(profile_name: str, version: str, modloader: str): # Done
		"""
		adds a new profile
		parameters:
			profile_name (str)
			version (str)
			modloader (str)
		returns:
			True when succesfull
			False when the profile already exists
		"""
		if os.path.isdir(f'{MINECRAFT_FOLDER}/mod-profiles/{profile_name}') == False and \
			config.add_profile(profile_name, version, modloader) == True:
			os.mkdir(f'{MINECRAFT_FOLDER}/mod-profiles/{profile_name}')
			return True
		else:
			# gui.promt('version already exists')
			return False

	def remove(profile_name: str): # Done
		# ----------
		# gui confirm promt
		# ----------
		if confirm == True:
			if config.rm_profile(profile_name) == True:
				shutil.rmtree(f'{MINECRAFT_FOLDER}/mod-profiles/{profile_name}')
		return True




class mods(): 

	def get_all(profile_name: str): # Done
		"""
		gets all mod names of the specified profile
		parameters:
			profile_name (str)
		returns
			mods (list)
		"""
		mods = []
		for mod in os.listdir(f'{MINECRAFT_FOLDER}/mod-profiles/{profile_name}'):
			mods.append(mod)
		return mods


	def add(profile_name: str, mod: dict): # Done
		"""
		adds a mod to a existing version 
		parameters: 
			profile_name (str)
			mod (dict)
		returns:
			True: when succesfull
			False: when version doesn't exist
		"""
		version = config.get_version(profile_name)
		modloader = config.get_version(profile_name)

		if version in config.get_profiles(modloader=config.get_modloader(profile_name), version=config.get_version(profile_name)) and \
			os.path.isdir(f'{MINECRAFT_FOLDER}/mod-profiles/{profile_name}'):
			if mod[version] == version and mod[modloader] == modloader:
				shutil.copy2(mod[file], f'{MINECRAFT_FOLDER}/mod-profiles/{profile_name}/{mod[name]}')
				return True
			else:
				# gui.prompt('this mod is not compatible with this version')
				return False
		else:
			# gui.prompt('this version doesn't exist')
			return False
	
	def remove(profile_name, mod): # Done
		"""
		removes a mod from the specified profile.
		parameters: 
			profile_name (str)
			mod (dict)
		returns:
			True: when succesfull
			False: when unsuccesfull
		"""
		try:
			os.remove(f'{MINECRAFT_FOLDER}/mod-profiles/{profile_name}/{mod[name]}')
			# Confirm promt?
			return True
		except:
			return False


def toDoubleStr(string): # Done
	return f'"{string}"'

def toSingleStr(doubleString): # Done
	return doubleString[1:-1]

def toSingleStrKey(dictionary): # Done
	newdict = {}
	for key, value in dictionary.items():
		newkey = toSingleStr(key)
		newdict[newkey] = value
	return newdict



def main():
	# version_names, versions = config.get_versions('fabric')
	# mods.get_all('1.18.2', 'fabric')
	# print(f'{version_names},{versions}')
	# print(cversion)
	# mods.switch_to('1.18.2')
	# config.add_version('1.18.1', 'fabric')
	# config.rm_profile('1.18.2')
	# print(version.get_current())
	# config.get_modloader('fabric mods 1.18.1')
	# print(toSingleStr('"hi"'))
	# print(config.get_profiles(version='1.18.1', modloader='fabric'))
	# config.add_profile('fabric mods 1.19', '1.19', 'fabric')
	pass

if __name__ == '__main__':
	if platform.system() == 'Linux':
			main()
	else:
		print('This software only works on Linux systems')

