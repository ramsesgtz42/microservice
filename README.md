# microservice
Microservice to send emails to newly registered users.

1. If using gmail I recommend using an App Specific Password
   
   a. To do this, go to myaccount.google.com
   
   b. Search 'app passwords' in the top search bar
   
   c. create a name for your app and paste the password into emailsend.py password field

2. If using Python for app:
   
   a. You must add "import subprocess" to your app
   
   b. you must also add a line to call the subprocess in the route for registering new users (shown in video)
   
   c. the line should look like subprocess.run(["python", "emailsend.py", emailGoesHere])

   d. After sending the email, the microservice will write a confirmation message to "confirm.txt", you must add a line to your app that reads the confirm message from confirm.txt

3. If using Node.JS:
   
   a. You must add these lines to your main app script:
   
    const { spawn } = require('child_process');
   
    const pythonCommand = 'python';
   
    const pythonScript = 'emailsend.py';
   
    const argument = 'emailGoesHere';
   
    const pythonProcess = spawn(pythonCommand, [pythonScript, argument]);

   b. It doesn't have to be that specific as you can change variable names to your liking, but the way emailsend.py works is that it receives an argument when called and sends email to that argument.

   c. After sending the email, the microservice will write a confirm message to "confirm.txt". If you want a confirmation message you must add a line that reads from confirm.txt

4. After adding the lines, make sure to go into emailsend.py and configure the email sending fields to your liking
   
5. Also, configure the email subject and body within emailsend.py to your liking.


![firefox_dBynaH2YzT](https://github.com/ramsesgtz42/microservice/assets/101148268/f5f7d782-68f9-45d2-a71f-e69dc05063c5)

