# Server adminstration

If you log into a GreenToGo server (g2g.dreisbach.us or app.durhamgreentogo.com), you need to run a few commands before messing with the Django shell or the database.

```
su - greentogo
source env/bin/activate
source envvars
```

Logs are at:
/opt/greentogo/logs

Then you should be good to go!


If you ever run into a "sha1" issue when deploying, delete your temp greentogo files in /tmp/greentogo