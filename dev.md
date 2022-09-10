# Dev

- [to do](#to-do)
- [config.ini](#configini)
- [main.py](#mainpy)
- [version.txt](#versiontxt)

## to do

- [ ] add the config.ini back in. (.gitignore wasnt leaving it alone)
- [ ] implement version switching
- [x] implement adding mods
- [x] implement removing mods (needs a gui window)
- [ ] make a gui
    - [x] choose a gui lib ([eel](https://github.com/ChrisKnott/Eel))
    - [ ] design a gui (bgcolor: #0d1117)
    - [ ] make the gui interacive
- [x] move logic from `config.rm_version()` to `version.remove()`
- [x] rename version (as in what profile) to profile everywhere
- [ ] replace the `version, modloader` in the functions where they are the name of the profile folder with `profile_name`
    - config
    - [x] `get_profiles`
    - [x] `add_profile`
    - [x] `rm_profile`
    - profile
    - [x] `get_current`
    - [ ] `switch_to`
    - [x] `add` (gui)
    - [x] `remove` (confirm promt when gui ready, the rest is finished)
    - mods
    - [x] `get_all`
    - [x] `add`
    - [x] `remove` confim promt?
- [ ] add a function to launch the minecraft launcher
    - maybe add a option to choose your launcher (file?)
- [ ] write docstrings 
- [ ] maybe combine `config.get_version` and `config.get_modloader` to a single function `config.get_info(profile_name: str, type: str)`

## config.ini
(to save the version names) [see file](config.ini)
```ini
[profiles]
"profile name" = modloader mod_version
```

- `profile_name` = The name of the profile.
- `Modloader` = The modloader for the mods in the profile (Either Forge or Fabric).
- `mod_version` = The Minecraft version of the mods in the  profile.

I know you shouldn't use stings in keys but it makes it easier to use in this specific case

## main.py
[see file](main.py)  

Double quotes are needed to get the key in the [`.ini` file](#configini) like this:
```py
>>> import configparser
>>> config = configparser.ConfigParser()
>>> config.read('config.ini')
['config.ini']
>>> profile_names = dict(config.items('profiles'))
>>> print(profile_names.get("fabric mods 1.19"))
None
>>> print(profile_names.get('"fabric mods 1.19"'))
fabric 1.19
```
I have written a couple of functions to help with this.
- `toDoubleStr(string)`
- `toSingleStr(doubleString)`
- `toSingleStrKey(dictionary)`

<br>

If a mod is needed somewhere, this is the syntax: 
```py
mod = {
    'file': '/file'
    'name': 'create.5'
    'version': '1.18.2'
    'modloader': 'forge'
}
```

## version.txt
To save the version, modloader of the currently installed profile.
```txt
profile_name version modloader
```
This gets split into:

- `profile_name` = The name of the profile
- `version` = The version of the profile
- `modloader` = The modloader of the version

By using:
```py
def get_current(): # V
    with open(f'{MINECRAFT_FOLDER}/mods/profile.txt', 'r') as pf:
        profile_name, version, modloader = pf.read().strip()
    return toSingleStr(profile_name), version, modloader
```