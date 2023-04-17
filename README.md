# verb_tense_study
Repo for verb tense study for Bucknell Linguistics Lab


## Instructions for Setting up Additional Experiments Online

### Hosting a website:
Bucknell has its own linux servers where you can easily set up and host a website, check out the instructions here: https://bucknell.teamdynamix.com/TDClient/40/LIT/KB/ArticleDet?ID=287 - you will have to log on to one of Bucknell’s remote linux servers, the instructions for how to set that up if you haven’t done it before are linked in the instructions above.

**IMPORTANT:**  if you want your website to be able to send data back to you, you will have to change the permission of public_html to **chmod ugo+rwx ~/public_html** instead of chmod go+x ~/public_html like the tutorial says.


Once you have your public_html directory set up, you will want your html file and any accompanying data files (likely csvs, images, audio files) to all go in that public_html folder. Here’s how: Say you have Ling_Site.html that you need everyone online to access, and myData.csv that Ling_Site needs to pull data from. Before you ssh onto the linux server, copy your files into your public_html folder from whichever local folder they are in using the scp command. The command will look like this:

**scp [local path to file] [bucknelluser] @linuxremote1.bucknell.edu/public_html**
	
If you want to copy an entire folder, use **scp -r [folder name/path]**
Next, ssh onto the linux server and use **cd public_html** and **ls -al**. This will show you the contents of public_html. You can navigate to any folders you might have in public_html and use ls -al to look in them as well.

Last, you will have to change the permissions of Ling_Site.html and myData.csv. You want everyone to be able to access the website, so change Ling_Site using chmod ugo+rwx Ling_Site.html myData.csv needs to be read by Ling_Site, so change that using **chmod ugo+r myData.csv**.
Now both Ling_Site and myData can be accessed at eg.bucknell.edu/~[username]/Ling_Site.html (or myData.csv)
