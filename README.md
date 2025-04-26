# SBFE
SBFE | Static Binary Feature Extractor


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
- Linux ELF files (.elf)
- Android APK files (.apk)

### ToDo:

- Scripts (.ps1, .bat)
- Scripts (.sh)
- Scripts (.js, .hta)
- And more

