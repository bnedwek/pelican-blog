Title: Uh oh, my root file system is full!
Date: 2020-08-19
Category: Projects
Tags: sun, solaris, retro computing
Description: If I hard code a summary...

I ran into a scary problem recently!

After getting my Solaris 7 install set up the way I wanted it on the Ultra 60, I decided a prudent thing to do would be to create some backups. From reading a bit of Solaris documentation I knew that the suggested way of backing up a complete filesystem is the `ufsdump` command, so I started fumbling around with that. In this case "fumbling around" without knowing the options (or their defaults) was a mistake.

In my case I was planning to save filesystem backups to a Raspberry Pi on my local network over NFS. From reading contemproaneous documentation I knew that, at the time, Sun were selling seperate backup utilities meant for network backups. This should have been a clue to check the defaults on the `ufsdump` utility.

I bumbled around with `ufsdump` and eventually found out how to send the backup to STDOUT, into `compress`, then into a file on an NFS share. However, unbeknownst to me, while messing around I used `ufsdump` without arguments which by default wants to write to a local tape drive.

Fun fact: even if you don't HAVE a local tape drive (/dev/rmt/0), ufsdump will happily write a dump file to that path! So if you don't have a ton of extra space in your root slice, and you clumsily try to back up a larger partition, it will fill up your root!