[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# Censei

A Python script to search `Censys.io` for hosts and services using API. 

[![GitHub issues](https://img.shields.io/github/issues/sc4rfurry/Censei?style=flat-square&logo=github&logoColor=white&color=5194f0&bgcolor=110d17)](https://github.com/sc4rfurry/Censei/issues)
[![GitHub forks](https://img.shields.io/github/forks/sc4rfurry/Censei?style=flat-square&logo=github&logoColor=white&color=5194f0&bgcolor=110d17)](https://github.com/sc4rfurry/Censei/fork)
[![GitHub stars](https://img.shields.io/github/stars/sc4rfurry/Censei?style=flat-square&logo=github&logoColor=white&color=5194f0&bgcolor=110d17)]()
[![GitHub license](https://img.shields.io/github/license/sc4rfurry/Censei?style=flat-square&logo=github&logoColor=white&color=5194f0&bgcolor=110d17)]()
[![GitHub release](https://img.shields.io/github/release/sc4rfurry/Censei?style=flat-square&logo=github&logoColor=white&color=5194f0&bgcolor=110d17)]()
[![GitHub contributors](https://img.shields.io/github/contributors/sc4rfurry/Censei?style=flat-square&logo=github&logoColor=white&color=5194f0&bgcolor=110d17)]()
[![GitHub last commit](https://img.shields.io/github/last-commit/sc4rfurry/Censei?style=flat-square&logo=github&logoColor=white&color=5194f0&bgcolor=110d17)]()


## Table of Contents

- [Table of Contents](#Table-of-Contents)
- [📝 Description](#-Description)
- [🔧 Technologies & Tools](#-Technologies-&-Tools)
- [📚 Requirements](#-Requirements)
- [Installation](#Installation)
- [Config](#Config)
- [Usage](#Usage)
    - [Help Menu](#Help-Menu)
- [Todo](#Todo)
- [Contributing](#Contributing)
- [License](#License)

#

## 📝 Description

**Censei** is a python script that uses the `Censys.io` API to search for hosts and services.
> Censys.io (www.censys.io) is a web-based search platform for assessing attack surface for Internet connected devices.
The tool can be used not only to identify Internet connected assets and Internet of Things/Industrial Internet of Things
(IoT/IIoT), but Internet-connected industrial control systems and platforms. Leveraging ingestion formats supported by
WebUI, API, Raw Data, Google BigQuery, Censys.io provides maximum extensibility into any size cyber security ecosystem.
Integrations with leading vulnerability tools and platforms, logging aggregators and other scanning systems allow
Censys.io to be seamlessly integrated into an enterprise. [CISA](https://www.cisa.gov/sites/default/files/publications/Censys_Technical_508c.pdf)
    
* [Censys.io](https://censys.io/)
* [Censys API](https://search.censys.io/api)
* [Censys API Python](https://censys-python.readthedocs.io/en/stable/)

</br>

## 🔧 Technologies & Tools

![](https://img.shields.io/badge/OS-Linux-informational?style=flat-square&logo=kali-linux&logoColor=white&color=5194f0&bgcolor=110d17)
![](https://img.shields.io/badge/Editor-VS_Code-informational?style=flat-square&logo=visual-studio&logoColor=white&color=5194f0)
![](https://img.shields.io/badge/Language-python-informational?style=flat-square&logo=python&logoColor=white&color=5194f0&bgcolor=110d17)
![](https://img.shields.io/badge/Python_Version-3.10-informational?style=flat-square&logo=python&logoColor=white&color=5194f0&bgcolor=110d17)

## 📚 Requirements

- Python 3.9+
- pip3

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.
if not installed, install it using the following command.

```bash
sudo apt-get install python3-pip
```

> It is advised to install the python requirements in a virtual environment, for that install the venv package.

```bash
python3 -m pip install venv
cd Censei
python3 -m venv env
source env/bin/activate
```

After that run the following commands:

```bash
python3 -m pip install -r requirements.txt
```
</br>

## Config
Before running the script, you need to add your `Censys.io` API ID and API Secret in the `.configx` file or set **API_ID** and **API_SECRET** as environment variables.
> After Login to your censys.io account, you can get your **API ID** and **API SECRET** from [Here](https://search.censys.io/account/api).
    
```yaml
# Config File
- API_ID: < API ID Here >
- API_SECRET: < API Secret Here >
```

</br>

## Usage
```console
1) python3 main.py
2) python3 main.py -q wordpress
```

### Help Menu

```bash
usage: main.py [-h] [-q QUERY]

A Python script to search using Censys.io API.

options:
  -h, --help            show this help message and exit
  -q QUERY, --query QUERY
                        The query to search for

```
</br>

## Todo
- [ ] Add Certificate Search.
- [ ] Add more search options.
- [ ] Add more filters.
- [ ] Add output options.

</br>

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

#

## License

[MIT](https://choosealicense.com/licenses/mit/)

#
## Feedback

If you have any feedback, please reach out to us at akalucifr@protonmail.ch
