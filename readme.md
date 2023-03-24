
# STORM Agent - CS:GO

A python application that provides faster and user-friendly operations for cs:go server administrators via CLI or GUI.

Mainly meant to be used together with STORM Server and/or STORMsys appliances.
Supports Ubuntu 18.04+.

## Authors

- [@devdanetra](https://www.github.com/devdanetra)


## Features

- Easy to use **GUI**
- Install/Upgrade **SteamCMD**
- Install/Upgrade **CS:GO Dedicated Server**
- **Versions selector**
- Start server & easily access console
- **Auto update** **(Coming Soon)**
- Updates you via email or telegram if a new patch is available. **(Coming Soon)**


## Requirements

- Python 3.10
## Installation


To install **SA-CS:GO** you can use pip:
```bash
  pip install sa-csgo
```


## Documentation

show available commands and options
```bash
  sa-csgo --help
```

opens gui
```bash
  sa-csgo gui
```

Installs latest SteamCMD version
```bash
  sa-csgo install csgoserver
```

Installs Counter Strike server, multiple versions are available
```bash
  sa-csgo install csgoserver
```
