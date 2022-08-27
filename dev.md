# INFO

- [to do](#to-do)
- [config.ini](#configini)
- [main.py](#mainpy)

## to do

- [ ] implement version switching
- [ ] ~implement adding mods
- [ ] ~implement removing mods
- [ ] make a gui
    - [ ] choose a gui lib
    - [ ] design a gui
    - [ ] make the gui interacive
    - [ ] change the system error `print()` to a error promt
- [x] move logic from `config.rm_version()` to `version.remove()`
- [ ] rename version (as in what profile) to profile everywhere
- [ ] replace the `version, modloader` in the functions where they are the name of the profile folder with `profile_name`
    - config
    - [ ] `add_version` (profile)
    - [x] `rm_version` (profile)
    - version
    - [ ] `switch_to`
    - [ ] `add`
    - [x] `remove`
    - mods
    - [ ] `get_all`
    - [ ] `add`
    - [ ] `remove`
- [ ] add a function to launch the minecraft launcher
    - maybe add a option to choose your launcher (file?)

## config.ini
(to save the version names) [see file](config.ini)
```ini
[version names]
"profile name" = modloader mod_version
```

- profile_name = The name of the profile.
- Modloader = The modloader for the mods in the profile (Either Forge or Fabric).
- mod_version = The Minecraft version of the mods in the  profile.

I know you shouldn't use stings in keys but it makes it easier to use in this specific case

## main.py
[see file](main.py)  
- Assuming that all instances of `profile_name` have `#`'s instead of spaces to .  
This will be done at te beginning
- double quotes are needed to get the value in the `.ini` like this:
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
