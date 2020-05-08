# Cisco Configuration Generator
A sample Cisco IOS-XE configuration tool. This tool can produce IOS-XE
configurations by filling out a web form. 

## Usage
```
python web.py
``` 
Once the web server has started open a web browser and proceed to 
127.0.0.1:5000.

The following web page will be displayed.

*Insert Webpage photo here

Once all pertinent information has been filled in click submit.
The configuration will be found in the ~/configs directory.

## Changing the Configuration Template
The configuration template is a Jinja2 template with the file
name ios-xe_template.j2. This template can be
modified to include additional static configuration or variable
configuration per individual need. User input from index.html is used
in the config function of web.py to assign the user input to variables
in ios-xe_config.j2 template. 

