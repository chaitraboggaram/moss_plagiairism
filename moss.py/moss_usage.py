import mosspy
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Now you can access the environment variables
USERID = os.getenv("PATH") # add your userid here

# m = mosspy.Moss(userid, "python")
m = mosspy.Moss(USERID, "c")

#m.addBaseFile("submission/a01.py")
#m.addBaseFile("submission/test_student.py")

# Submission Files
# m.addFile("submission/a01-sample.py")
# m.addFilesByWildcard("submission/*/*.py")
m.addFilesByWildcard("submission/*.c")
m.addFilesByWildcard("submission/*/*.c")
m.addFilesByWildcard("submission/*/*/*.c")
m.addFilesByWildcard("submission/*/*/*/*.c")
m.addFilesByWildcard("submission/*/*/*/*/*.c")
m.addFilesByWildcard("submission/*/*/*/*/*/*.c")
m.addFilesByWildcard("submission/*/*/*/*/*/*/*.c")
m.addFilesByWildcard("submission/*/*/*/*/*/*/*/*.c")
m.addFilesByWildcard("submission/*/*/*/*/*/*/*/*/*.c")
m.addFilesByWildcard("submission/*/*/*/*/*/*/*/*/*/*.c")
m.addFilesByWildcard("submission/*/*/*/*/*/*/*/*/*/*/*.c")


# progress function optional, run on every file uploaded
# result is submission URL
url = m.send(lambda file_path, display_name: print('*', end='', flush=True))
print()

print ("Report URL: " + url)

# Save report file
m.saveWebPage(url, "submission/report.html")

mosspy.download_report(url, "submission/report/", connections=8, log_level=10, on_read=lambda url: print('*', end='', flush=True)) 
# log_level=logging.DEBUG (20 to disable)
# on_read function run for every downloaded file


'''
# In case reports don't get downloaded to submissions comment all lines above and uncomment the below

import mosspy
from dotenv import load_dotenv
import os
load_dotenv()
USERID = os.getenv("PATH") # add your userid here
url = 'http://moss.stanford.edu/results/'    # replace with the correct home page link
m.saveWebPage(url, "submission/report.html")
mosspy.download_report(url, "submission/report/", connections=8, log_level=10, on_read=lambda url: print('*', end='', flush=True)) 
'''