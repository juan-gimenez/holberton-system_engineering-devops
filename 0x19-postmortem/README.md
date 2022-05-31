Postmortem

Google label issue January 31, 2009

Issue Summary
"This site may harm your computer" was the message that appeared every time you googled something between 6:30 a.m. PST and 7:25 a.m PST January 31, 2009.
Every single user was affected by this issue wich made them think the site they were visiting was malicious. The root cause was just human error.
-
-
Timeline
The issue was detected at 6:50 a.m aprox, by the google team. Fortunately, the error was fixed pretty quickly as it was not complex at all. This issue was escaled to the google engineering team. The incident was fixed by changing the list of harmfull URLs.
-
-
Root cause and resolution
Sites that may harm your computer usually are tagged with a message ,however, the URL of '/' was mistakenly checked in as a value so every website was detected to be harmfull('/' expands to all URLs). This was fixed by just deleting the reference to all websites so that it does not tell you that a website is harmfull if it is not.
-
-
Corrective and preventative measures
We maintain a list of such sites through both manual and automated methods, so automating tests to make sure non-harmfull sites are not labeled as harmfull.
Tasks to prevent this from happening:
- more processes before going to production
- better tests to prevent human errors
- more robust file checks in place to prevent it from happening again


source: https://googleblog.blogspot.com/2009/01/this-site-may-harm-your-computer-on.html
