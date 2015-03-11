import os, subprocess

if os.environ.get('CONFIG_FILE'):
    conf = __import__(os.environ.get('CONFIG_FILE'))
else:
    import settings as conf
l = ["-n", "-t", conf.JMX_SCRIPT, "-Jjourneys_results",
    conf.RESULT_FILE, "-Jjourneys_dataset", conf.SOURCE_FILE, "-Jserver_url",
    conf.URL, "-Jserver_port", conf.PORT, "-Jserver_key", conf.TOKEN]
print l
os.execv("/usr/bin/jmeter", l)
