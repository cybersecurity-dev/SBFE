# **SBFE** | _Static Binary Feature Extractor_
[![made-with-python](http://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![built-with-science](https://forthebadge.com/images/badges/built-with-science.svg)](https://cyberthreatdefence.com/)
[![open-source](https://forthebadge.com/images/badges/open-source.svg)](https://cyberthreatdefence.com/)

<details>

<summary>Install required tools on Linux</summary>

### For Ubuntu 18.04, 20.04, 22.04

```bash
sudo apt-get update
```
</details>

<details>

<summary>Install required tools on Windows</summary>

</details>


<details>

<summary>Install required python libs</summary>

### pip install
```bash
pip install -r requirements.txt
python3 setup.py install
```

### conda install
```bash
conda config --add channels conda-forge
conda install --file requirements_conda.txt
python3 setup.py install
```

</details>


## Supported File Formats

The analyzer supports multiple file formats including:
- Windows executables (.exe, .dll)
- Linux executables (.elf)
- Android executables (.apk)

### ToDo:

- Scripts (.ps1, .bat)
- Scripts (.sh)
- Scripts (.js, .hta)
- And more

