# Django Channels Chat App

Channels is a project that takes Django and extends its abilities beyond HTTP - to handle WebSockets, chat protocols, IoT protocols, and more. It’s built on a Python specification called ASGI.

It does this by taking the core of Django and layering a fully asynchronous layer underneath, running Django itself in a synchronous mode but handling connections and sockets asynchronously, and giving you the choice to write in either style.

## Prerequisites:

You will need the following programmes properly installed on your computer.

* [Python](https://www.python.org/) 3.6+

* Virtual Environment

To install virtual environment on your system use:
```bash
apt-get install python3-venv
```
* Redis Server

To install and run Redis Server in Ubuntu environment
```bash
# Installing Redis
sudo apt update
sudo apt install redis-server

# Enabling and starting Redis Server Service
systemctl enable redis-server
systemctl start redis-server
```
## Installation and Running :

```bash
git clone https://github.com/janak29292/chatproject.git

cd chatproject

python3 -m venv venv

source venv/bin/activate

# Install required packages for the project to run
pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

Open Browser and Type http://127.0.0.1:8000
