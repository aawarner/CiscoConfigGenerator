import jinja2
import os
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def webroot():
    return render_template('index.html')

@app.route("/config", methods = ["POST"])
def config():
    hostname = request.form["hostname"]
    dns_server = request.form["dns_server"]
    domain_name = request.form["domain_name"]
    dhcp_pool_name = request.form["dhcp_pool_name"]
    dhcp_pool_net = request.form["dhcp_pool_net"]
    dhcp_pool_mask = request.form["dhcp_pool_mask"]
    dhcp_router =  request.form["dhcp_router"]
    dhcp_dns_server = request.form["dhcp_dns_server"]
    dhcp_excluded = request.form["dhcp_excluded"]
    user = request.form["user"]
    priv = request.form["priv"]
    password = request.form["password"]
    loopback0_address = request.form["loopback0_address"]
    loopback0_mask = request.form["loopback0_mask"]
    tunnel0_description = request.form["tunnel0_description"]
    tunnel0_destination = request.form["tunnel0_destination"]
    g0_description = request.form["g0_description"]
    g1_description = request.form["g1_description"]
    g1_address = request.form["g1_address"]
    g1_mask = request.form["g1_mask"]

    data = [{
            "hostname": hostname,
            "dns_server": dns_server,
            "domain_name": domain_name,
            "dhcp_pool_name": dhcp_pool_name,
            "dhcp_pool_net": dhcp_pool_net,
            "dhcp_pool_mask": dhcp_pool_mask,
            "dhcp_router": dhcp_router,
            "dhcp_dns_server": dhcp_dns_server,
            "dhcp_excluded": dhcp_excluded,
            "user": user,
            "priv": priv,
            "password": password,
            "loopback0_address": loopback0_address,
            "loopback0_mask": loopback0_mask,
            "tunnel0_description": tunnel0_description,
            "tunnel0_destination": tunnel0_destination,
            "g0_description": g0_description,
            "g1_description": g1_description,
            "g1_address": g1_address,
            "g1_mask": g1_mask
            }]

    template_file = "ios-xe_template.j2"
    output_directory = "configs"
    # create the central Jinja2 environment and load template
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="."),
                             trim_blocks=True,
                             lstrip_blocks=True)
    template = env.get_template(template_file)

    # check for configs directory if not present create
    if not os.path.exists(output_directory):
        os.mkdir(output_directory)

    # create the config templates
    for p in data:
        result = template.render(p)
        f = open(os.path.join(output_directory, p['hostname'] + ".config"), "w")
        f.write(result)
        f.close()
    path = "configs/"
    with open(os.path.join(path, hostname + ".config")) as fp:
        v = fp.read().splitlines()
        for i in v:
            line = i.rstrip("\n")
            print(line)
    hl = ("Configuration for " + hostname + " created. Check configs directory for " + hostname + ".config file.\n")
    return hl


if __name__ == '__main__':
    app.run()