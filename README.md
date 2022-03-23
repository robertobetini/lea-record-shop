# lea-record-shop
Api for a ficticional record shop that deals with disco selling.

# How to run the application

### 1. Install python

If you don't already have python installed, go to [python website](https://www.python.org/) and download the latest version for your OS. Make sure to install pip and check the box `add python to PATH` when installing.

You can check your python version by running the command

```
> python --version
```

### 2. Install Pipenv and Flask modules in your machine

You can install Pipenv and Flask by running:

```
> pip install pipenv
```

Pipenv creates a virtual environment to run your application.

### 3. Setup the Google Cloud Project

Create a new project on GCP (Gooogle Cloud Platform) and enable Firestore.
Some queries will need to create some indexes, when tat happens you must click on the link returned by the API and create it in order to run.

You must also create a new Service Account with permission to Read and Write to Firestore, then generate a json key and download it to the API folder.

### 4. Setup the environment

After installing the necessary packages, go to console and hit the commands to create a virtual environment and install packages:

```
> pipenv shell
> pipenv install -r requirements.txt
```

Now let's set some necessary environment variables

* for Windows:

```
> set FLASK_APP=app
> set GOOGLE_APPLICATION_CREDENTIALS=<your-credential-file-here>
```

* for Linux:

```
$ export FLASK_APP=app
$ export GOOGLE_APPLICATION_CREDENTIALS=<your-credential-file-here>
```

### 5. Run the application

In order to run the application, just call

```
> flask run
```

while on the api folder (`src/flaskr/`).
