# INFO

- [to do](#to-do)
- [config.ini](#configini)
- [main.py](#mainpy)

## to do

- [ ] implement version switching
- [x] implement adding mods
- [x] implement removing mods
- [ ] make a gui
    - [ ] choose a gui lib
    - [ ] desing a gui
    - [ ] make the gui interacive
- [ ] move logic from config.rm_version() to version.remove()
- [ ] rename version (as in what profile) to profile everywhere

## config.ini
(to save the version names) [see file](config.ini)
```ini
[version names]
version_name = modloader mod_version
```

- Version_name = The name of the profile
- Modloader = The modloader for the mods in the profile (Either Forge or Fabric)
- mod_version = The Minecraft version of the profile

## main.py
[see file](main.py)
