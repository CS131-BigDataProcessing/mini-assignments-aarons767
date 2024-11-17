#The goal of this project is to set up three basic automated tasks
#We will be scheduling daily file cleanups, weekly system backups, and sending
routine emails about our system's disk usage to a certain user

###We start by creating test files in our current working directory named ./tester
*Our daily file clean up will run the following cron job:*
0 2 * * * /bin/rm -rf /Users/aarond/Documents/adsouza_A9/tester/*

To test this, you'll need to create a tester directory and add a sample file like file1.txt
using touch file1.txt(make sure you're in the tester directory when doing so)

Then run the command: /bin/rm -rf /Users/aarond/Documents/adsouza_A9/tester/*
The file1.txt file should be deleted after this statement
verify using the ls statement in the tester directory

###For the Weekely Home directory backup task, we will use the following cron jon
*The following will comress the files in the test folder with a timestamped file name and save it in the backups folder:*
0 3 * * 0 tar -czf /Users/aarond/Documents/adsouza_A9/backups/$(date +\%Y-\%m-\%d).tar.gz /Users/aarond/Documents/adsouza_A9/test/

To test, run the following: tar -czf /Users/aarond/Documents/adsouza_A9/backups/$(date +%Y-%m-%d).tar.gz /Users/aarond/Documents/adsouza_A9/test/
and then cd into he backups folder. There should be a tar file with a time and date stamp.


###Daily Disk Usage Report
*The goal of this task will be to send daily email resports about the disk usage to the specified email*
We'll use the cron job: 30 8 * * * df -h | mail -s "Daily Disk Usage Report" aarondsouza42@gmail.com
To test this make we'll need to have mail installed first. Then test this command on the command line using df -h | mail -s "Daily Disk Usage Report" aarondsouza42@gmail.com.
