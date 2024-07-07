Hey David!

This is a quick tutorial on how to get going with PyCharm and Python.

1. Download and install [Python 3.12.4](https://www.python.org/downloads/release/python-3124/)
2. Download the [PyCharm](https://www.jetbrains.com/pycharm/) IDE for your operating system.
3. The free Community Edition should work just fine. The Professional Edition offers a few more bells & whistles.
4. Install the app according to the directions.
5. Launch PyCharm, then Navigate to File -> Project from Version Control
6. You'll see a screen that looks like this: ![alt](images/repository.png)
7. In the `URL` field, enter `https://github.com/eddie199511/davidh.git`
8. Click the `Clone` button
9. This will pull all the files from the github repository to your local machine.
10. This assumes you have access to a `bash` or other similar Unix shell.
11. Change directories into the `davidh` directory that was created.
12. I've included a Python virtual environment for use with this project. You can activate it by running this command: `source venv/bin/activate`. Further reading on virtual environments can be found [here](https://docs.python.org/3/tutorial/venv.html)
13. Have a look at the first code example: [lists](lists.md)