## Why?
A project I am working on uses MJML and Django templates to send email notifications. I noticed there are some significant differences in styling between the preview shown for MJML files and the actual email received by the recipient. The template tag for Django templates `{{` `}}` in MJML creates additional issues for MJML live preview as it doesn't parse it. For a strict design requirement, this is not acceptable.

This project is created to solve this problem. Here we can check not only how an MJML template is rendered with context in browser but also send the rendered HTML as an email. Thus making the job of the person working on MJML notification easier as he can easily view the rendered HTML with context in the browser as a normal page and email.

(and yes, there might be differences in rendered HTML viewed as page and viewed in Gmail as email!)
## Prerequisite
install `python` and `mjml` globally and verify with
- python `python --version`
- mjml `mjml --version`

### install virtualenv
```shell
pip install virtualenv
virtualenv --version
```

### setup virtualenv and install packages
- navigate to project directory
- create virtualenv: `virtualenv venv`
- activate virtualenv: `source venv/bin/activate`
- install packages: `pip3 install -r requirements.txt`

## Working Setup

### Gmail setting
Get app password for email:
>Since May 30 2022 the less secure apps feature has been disabled. Now, to let 3rd party apps access gmail you must generate an App password.
>
>To generate an app password you must first enable 2-factor authentication for your account and then go to https://myaccount.google.com/apppasswords

Open `settings.json` and put your email in `auth_user` and generated app password in `auth_password`. Also fill in `recipients` list with the intended email recipients.

## Workflow

### activate virtualenv
the virtualenv needs to be activated in terminal for any of the following commands to work. to activate `source venv/bin/activate`

### runserver
```shell
python manage.py runserver 9000
```

**Note: application logic depends upon the file name, therefore please make sure you use exact same file name noted by _[file_name]_ in following**

- create a mjml file _[file_name]_ in `templates/mjml` included django templating language.
- create a json file _[file_name]_ in `templates/context`, this must done, for empty context place `{}` in file.
- run server using above `runserver` section.
- navigate to `http://127.0.0.1:9000/[file_name]` to see preview.
- to send email run in venv `python manage.py send-email [file_name]`


## Static assets and it's urls
The icons and images served by the server, therefore if you want to use those in template, place respective files in `static/icons` or `static/images` and run
```shell
python manage.py collectstatic
```
check it's working by opening
```
http://127.0.0.1:9000/static/images/[image_name.extention]
http://127.0.0.1:9000/static/icons/[icon_name.extention]
```

**Note: you need to run above command everytime you update `static` directory**


Now you can use these url of static assets by placing the url in json file of the context like e.g
```json
{
  "logo_url": "http://127.0.0.1:9000/static/images/logo.png"
}
```
**Note: In gmail local urls are not loaded by default; you can enable them by running script provided in `script.js` in browser console.**

### Live Reload
By default, you need to reload every time the MJML or context is changed to see its effect in browser. The live reload feature helps to see live changes as you change the MJML or context by reloading the browser page. to activate run this command in separate console. Now your page will be updated when you save file in `templates` directory.
```shell
python manage.py livereload --ignore-file-extensions=.html
```
_( The HTML files are auto generated when we load the page in browser, hence we are ignoring those.)_
