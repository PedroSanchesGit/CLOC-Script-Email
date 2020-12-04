# CLOC-Script-Email
A Python console application that can run command lines and retrieve the results to send them as an email using SMTP. This is an experiment to use the CLOC script via this app.

Before you run the main.py script, you should install some previous software for this app to work as intended.

First of all, you need to install the CLOC project into your machine. You can find the project in here: https://github.com/AlDanial/cloc
Every step to do that is very well discribed in the respective README file.

To test if the CLOC is working properly, you can open a command prompt and enter: cloc --version
If the command executes successfully, it means everything went fine. 
In case of some problem, please note that CLOC works with any kind of environment but each one has its own procedure to make it work. 
Pay special attention to the need of a PERL interpreter. If you don't have one installed, please procede to install one.

If everything works with CLOC, make sure that you have the python installed in your machine. You can install it directly from the website: https://www.python.org/


From the project, you will only need the main.py file. Save it into a directory that makes sense to you.
After that, use a command prompto to execute the py file: python main.py

This will run the script and you can start to use the application.

The app will ask you for a command. You can enter any command that your console can handle separated by spaces. If you need to insert a command that has spaces but they must be ignored to work, you can use quotation marks. Example: "/dir/something/Pedro Sanches"

The commands that we are looking for in this phase are: cloc *something*
*somthing* must be replaced with the respective script / folder / git repository that we want to evaluate.

Then, the application will ask you for the information to fill the email that will be send. The email will have an attachment with the result of the cloc scan.

You can only use Gmail as a sender and you must turn ON the "Allow less secure apps" option on the Security tab in your gmail account.

Any extra help that you need please let me know.
