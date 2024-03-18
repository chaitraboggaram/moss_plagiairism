# moss.py

A Python client for [Moss](http://theory.stanford.edu/~aiken/moss/): A System for Detecting Software Similarity

</br>

## Introduction

This is a Python interface for the [Moss](http://theory.stanford.edu/~aiken/moss/) client. It was developed for [AutoGrader](https://github.com/BilalZaib/AutoGrader) to handle similarity in Python assignment submissions. 

It was implemented based on the [original bash script/documentation](http://moss.stanford.edu/general/scripts.html) and its [PHP](https://github.com/Phhere/MOSS-PHP) dialect.


</br>

### Installation
 
```bash
pip install mosspy
pip install python-dotenv
```

**Create or edit the `.env` file in the moss.py directory of your project and update the UserID with your UserID**
```
USER_ID = "UserID"          # add your userid here 
```

**Run the below command in root directory of the project**
```bash
pip install python-dotenv
```


</br>

### Usage

```python
import mosspy
from dotenv import load_dotenv
import os
load_dotenv()
USER_ID = os.getenv("PATH")
m = mosspy.Moss(USER_ID, "python")

m.addBaseFile("submission/a01.py")
m.addBaseFile("submission/test_student.py")

# Submission Files
m.addFile("submission/a01-sample.py")
m.addFilesByWildcard("submission/a01-*.py")

# Progress function optional, runs on every file uploaded
# The result is submission URL
url = m.send(lambda file_path, display_name: print('*', end='', flush=True))
print()

print ("Report Url: " + url)

# Save report file
m.saveWebPage(url, "submission/report.html")

# Download the whole report locally, including code diff links
mosspy.download_report(url, "submission/report/", connections=8, log_level=10, on_read=lambda url: print('*', end='', flush=True)) 
# log_level=logging.DEBUG (20 to disable)
# on_read function runs for every downloaded file
```

</br>

### Download reports only
**In case reports don't get downloaded to submissions, comment out all lines above and uncomment the below**

```python
import mosspy
from dotenv import load_dotenv
import os
load_dotenv()
USER_ID = os.getenv("PATH") # add your userid here
url = 'http://moss.stanford.edu/results/'    # replace with the correct home page link
m.saveWebPage(url, "submission/report.html")
mosspy.download_report(url, "submission/report/", connections=8, log_level=10, on_read=lambda url: print('*', end='', flush=True)) 
```

</br>

## Python Compatibility

* [Python](http://www.python.com) - v3

</br>

## Similar Projects

* [ocaml-moss](https://github.com/Chris00/ocaml-moss) - OCaml client 
* [cl-moss](https://github.com/wsgac/cl-moss) - Common Lisp client
* [moji](https://github.com/nordicway/moji) - Java version
* [MOSS-PHP](https://github.com/Phhere/MOSS-PHP) - PHP version
* [GUI for Windows](https://onedrive.live.com/?cid=b418048abfa842a7&id=B418048ABFA842A7%2136714&ithint=folder,.txt&authkey=!ACqFMI0kmA4L1mc) - GUI for Windows

</br>

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/soachishti/moss.py/blob/master/LICENSE) file for details
