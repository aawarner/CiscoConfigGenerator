import jinja2
import json
import os

template_file = "ios-xe_template.j2"
json_parameter_file = "parameters.json"
output_directory = "configs"

# read the contents from the JSON file
print("Reading in parameters from parameters.json")
config_parameters = json.load(open(json_parameter_file))

# create the central Jinja2 environment and load template
print("Creating Jinja2 environment...")
env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="."),
                         trim_blocks=True,
                         lstrip_blocks=True)
template = env.get_template(template_file)

# check for configs directory if not present create
if not os.path.exists(output_directory):
    os.mkdir(output_directory)

# create the config templates
print("Creating templates...")
for parameter in config_parameters:
    result = template.render(parameter)
    f = open(os.path.join(output_directory, parameter['hostname'] + ".config"), "w")
    f.write(result)
    f.close()
    print("Configuration '%s' created..." % (parameter['hostname'] + ".config"))
print("DONE")