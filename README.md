Django boilerplate
==========

A Django 'hello world' example.

# Installation checklist:
    * [ ] Install git, python, pip and virtualenv
    * [ ] Import your public key to gitlab
    * [ ] Configure Git and checkout the project
    * [ ] Create a virtualenv
    * [ ] Run the project, run migration
    * [ ] Modify settings - Optional

# Installation details:
## Install python 3.6

Follow the instruction here: https://www.python.org/downloads/mac-osx/. Recommend installing to `C:\Python36`. On Windows, you might have to manually add the path to python (`C:\Python36` and `C:\Python36\Scripts`) to the environment variable `PATH`.

Open a command line window (Windows) or a terminal and type in:
```shell
python --version
pip --version
```

You should see something similar to this, or else you need to fix the problem before moving to the next step.
```text
python 3.6.5
pip 9.0.2 from C:/Python36/Script (python 3.6)
```

## Install git
### On Linux
#### Debian based linux systems (e.g. Ubuntu)
**Open a terminal. Copy & paste the following** into the terminal window and **hit `Return`**. You may be prompted to enter your password.

```shell
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git
```
#### Red Hat based linux systems (e.g. CentOS)
**Open a terminal. Copy & paste the following** into the terminal window and **hit `Return`**. You may be prompted to enter your password.
```shell
sudo yum upgrade
sudo yum install git
```
### On MacOS
**Open a terminal**

#### Step 1 – Install Homebrew
**Copy & paste the following** into the terminal window and **hit `Return`**.
```shell
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew doctor
```
You will be offered to install the *Command Line Developer Tools* from *Apple*. **Confirm by clicking *Install***. After the installation finished, continue installing *Homebrew* by **hitting `Return`** again.

#### Step 2 – Install Git
**Copy & paste the following** into the terminal window and **hit `Return`**.
```shell
brew install git
```
### On Windows
**Download** Git from http://msysgit.github.io and **install it**.

## Install virtualenv
Open a terminal or cmd window and type:
```shell
pip install virtualenv
```

## Configure Git and checkout the project:
Set your username and email for git if you haven't done so already:
```shell
git config --global user.name "John Doe"
git config --global user.email "john@doe.com"
```
Generate a pair of SSH keys and import the public key to gitlab:
```shell
ssh-keygen # Leave the passphrase empty. Default path to the keys is ~/.ssh/id_rsa.pub and ~/.ssh/id_rsa.pub
```
Copy the content of ~/.ssh/id_rsa.pub **NOT THE OTHER ONE** and import it to gitlab
Checkout the project:
```shell
mkdir ~/workspace
cd ~/workspace
git clone git@gitlab.com:unifier/helloworld.git
cd helloworld
```
## Create a virtual environment:
```shell
virtualenv -p `which python` .venv
```

## Run the project:
### Source the virtual environment.
#### On windows:
##### Using command line (`cmd`)
```shell
.venv\Scripts\activate.bat
```
##### Using POSIX terminal e.g. git bash, cygwin, Mingw
```shell
source .venv/Scripts/activate
```
#### On Linux and Mac
```shell
source .venv/bin/activate
```
### Now run for the first time
```shell
pip install -r requirements.txt
python manage.py runserver 8001
# Now press Ctrl + C to quit, then
python manage.py migrate
# Now run it again
python manage.py runserver localhost:8001
The website is now available at http://localhost:8001/
# Change 8001 to any port you like
```
## Modify settings
After running the project for the first time, a file named `settings.yaml` is created. If you want to change anything - edit this file and rerun the app. You don't have to modify it - the default settings should work fine.
