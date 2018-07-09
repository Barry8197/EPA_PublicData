# EPA_PublicData

## Setting Up For MacOS

### 1. Clone the EPA_PublicData Repository

1. [Clone](https://help.github.com/articles/cloning-a-repository/) the repository.

#### Option A: Github Desktop

  1. If you don’t have a GitHub account, you’ll need to create one at [github.com](https://github.com). Since the database is a public repository, you’ll want to select a free public account (the option reads “Unlimited public repositories for free.”).
  2. Once you’ve created an account and confirmed your email address, you’ll want to download and install the GitHub desktop client at [desktop.github.com](https://desktop.github.com/).
  3. Use your new account credentials to log into the GitHub desktop client and select the option to clone a repository. Then, enter the URL `https://github.com/Barry8197/EPA_PublicData/`.
  4. Once you've cloned the repository you can use the `Repository -> Show In Finder` option in the desktop Github app to obtain the location of the repository directory so that you find it using Terminal.

#### Option B: Command line
(This may require installing Git if you don't already have it.)
```sh
git clone https://github.com/Barry8197/EPA_PublicData.git
```

### 2. Installing Anaconda and Python packages
1. Anaconda is a package manager, environment manager and Python distribution that contains many of the packages we’ll need to get the database up and running. Please select the Python 3.6 version on this [page](https://www.anaconda.com/download/). You can follow a step by step guide to completing the installation on the Graphical Installer [here](https://docs.continuum.io/anaconda/install/mac-os#macos-graphical-install).

### 3. Setting up PostgreSQL

1. Now that we have all the required packages installed, we can install the PostgreSQL database. It’s most straightforward to set up through Postgres.app, which is available [here](http://postgresapp.com/).
2. After installing PostgreSQL, open the application. Then we’ll set up command line access to PostgreSQL. In your terminal window, run `sudo mkdir -p /etc/paths.d &&
echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp`. Then close the Terminal window and open a new one for changes to take effect. In your new terminal window, run `which psql` and press enter to verify that the changes took effect.
3. We can now set up our PostgreSQL databases. In your terminal window, run `psql` to bring up the PostgreSQL prompt.
  1. Run `CREATE USER catalyst with CREATEDB;` to create the catalyst superuser.
  2. Run `CREATE DATABASE eia860;` to create the database that will receive data for all eia860.
  3. Run `CREATE DATABASE eia923;` to create the database that will receive data for all eia923.
  4. Run `\q` to exit the PostgreSQL prompt.
  
### 4. Import the data into PSQL

1. Open a terminal window (cmd + spacebar --> 'Terminal')
2. Navigate to EPA_PublicData --> cd /Users/youruser/EPA_PublicData
3. Run the python script
```sh
python __init__.py
```
This process will take ~30 - 40 mins. 

### 5. Automatically update database

1. Navigate to EPA_PublicData --> cd /Users/youruser/EPA_PublicData
2. Run the python script

```sh
python Automated_Update.py
```
This will automatically update the database at 10am on the first day of every month.
You're done!!

## Setting Up For windows

### 1. Clone the EPA_PublicData Repository

1. [Clone](https://help.github.com/articles/cloning-a-repository/) the repository.

#### Option A: Github Desktop

  1. If you don’t have a GitHub account, you’ll need to create one at [github.com](https://github.com). Since the database is a public repository, you’ll want to select a free public account (the option reads “Unlimited public repositories for free.”).
  2. Once you’ve created an account and confirmed your email address, you’ll want to download and install the GitHub desktop client at [desktop.github.com](https://desktop.github.com/).
  3. Use your new account credentials to log into the GitHub desktop client and select the option to clone a repository. Then, enter the URL `https://github.com/Barry8197/EPA_PublicData/`.
  4. Once you've cloned the repository you can use the `Repository -> Show In Finder` option in the desktop Github app to obtain the location of the repository directory so that you find it using Terminal.

#### Option B: Command line
(This may require [installing](https://gitforwindows.org/) Git if you don't already have it.)
```sh
git clone https://github.com/Barry8197/EPA_PublicData.git
```
### 2. Installing Anaconda and Python packages
1. Anaconda is a package manager, environment manager and Python distribution that contains many of the packages we’ll need to get the database up and running. Please select the Python 3.6 version on this [page](https://www.anaconda.com/download/). You can follow a step by step guide to completing the installation on the Graphical Installer [here](https://docs.continuum.io/anaconda/install/windows).

### 3. Setting up PostgreSQL


1. [Download](https://www.postgresql.org/download/windows/) the Postgres installer.
The EnterpriseDB version is fine; you don't need the extras included in BigSQL.
Install the latest PostgreSQL version (currently 10.2) for Windows (32- or 64-bit).

2. The installer requires you to set a password for the `postgres` user.
Remember this.
In the installation, do install you should install PostgreSQL server and pgAdmin 4.
The installer offers other things, like Stack Builder, that aren't necessary.

3. We can now set up our PostgreSQL databases. Open the pgAdmin 4 program.


4. In pgAdmin 4, log into the `postgres` account.
5. Right click "Login/Group Roles" and add a new user called `catalyst`. Set a password for the `catalyst` user.
    - Grant the catalyst users permissions to login and create databases.
6. Next, right-click on "databases" and open up the create database menu.
Create the `eia860` database with `catalyst` as the owner. This database will receive all `eia860` data.
7. Repeat #6 to create databases called `eia923`.
8. Set up a `pgpass.conf` file with the password you set:
    - In Windows Explorer, type %APPDATA%\postgresql into the address bar and press enter. This should take you to something like c:\users\username\appdata\local\postgresql, but don't worry if that's not the exact path.
    - See if there's already a file called pgpass.conf
    - If there is, open it. If not, use Notepad to create a text file called pgpass.conf in that folder.
    - Whether it previously existed or not, you're going to add a new line.
    - The contents of that line will be: `127.0.0.1:*:*:catalyst:the password you picked`, substituting in the password you picked for the catalyst user.
        - The line above says "whenever you try to connect to the local machine over IPv4 with the username `catalyst`, use the password ______".
    - Save and close.

### 4. Import the data into PSQL

1. Open a command prompt window (Start --> Program Files --> Accessories --> Command Prompt) 
See other methods [here](https://www.quora.com/How-do-I-open-terminal-in-windows)
2. Navigate to EPA_PublicData --> cd /Users/youruser/EPA_PublicData
3. Run the python script
```sh
python __init__.py
```
This process will take ~30 - 40 mins. 

### 5. Automatically update database

1. Navigate to EPA_PublicData --> cd /Users/youruser/EPA_PublicData
2. Run the python script

```sh
python Automated_Update.py
```
This will automatically update the database at 10am on the first day of every month.
You're done!!
