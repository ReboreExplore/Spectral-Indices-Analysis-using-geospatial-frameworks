# Local Project Scripts 👨🏼‍💻

This part of the work is intended to design a command line utility which can be executed with multiple arguments (based on the user input).

## Setting up your local system

1. Setup a an conda environment to organize your code in one workspace. You can refer here for the setup and all other necessary installations.
2. Sign in with Google Earth Engine with email id ( both gmail and edu emails work ).
3. Get the earthengine api for your system in the gee environment.

```python
 conda install -c conda-forge earthengine-api
 ```
4. Download gcloud. I am using a arch-based 64 bit linux system hence I am including the guide for that. You may refer the [official gcloud installation guide](https://cloud.google.com/sdk/docs/install) for the other operating systems.
- At the command line run - 
```bash
curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-396.0.0-linux-x86_64.tar.gz
```
- Extract the contents of the downloaded zip in the same directory. Do remove any previous instances of `google-sloud-sdk` if you have any.
```bash
tar -xf google-cloud-cli-396.0.0-linux-x86_64.tar.gz
```
- Add the google-cloud tools to PATH by executing the `install.sh` file from the downloaded google-cloud-sdk directory.
```bash
./google-cloud-sdk/install.sh
```
- Initialize the google cloud cli with the following command.
```bash
./google-cloud-sdk/bin/gcloud init
```
5. In the terminal run `gcloud help` to make sure gcloud cloud is installed properly.
6. Run `earthengine authenticate` in the terminal. This step with provide you with an url, which when navigated will direct you to choose your email. Choose the correct email and project for your work.
7. You will be authorized after agreeing and allowing a few clauses.

## Final code execution
1. Activate your gee conda environment by `conda activate <env-name>`.
2. Get to the directory where you have your `local_scripts`.
3. Run `python main.py`. This step will generate GEOtiff maps in your selected Google Drive.  

