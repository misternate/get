# get.py
get.py is a simple file downloader for your CLI.
## Using get.py

### Installation and usage
```bash
$ pip install -r requirements.txt
```
```bash
$ python get.py (-n rename the file [optional]) (-d create or add the file to a directory ([optional]) path_to_file
```
#### Make it standalone
```bash
$ pyinstaller get.py
```
This will create `/dist/get` which can then be directly executed `get https://domainname.domain/file.extension`.

Additionally, you can add get as an alias. In zsh, as an example, add `alias get="./get"` to create a global alias for the app.