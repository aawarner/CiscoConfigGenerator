"""
Copyright (c) 2019 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

Filename: config.py
Version: Python 3.7.2
Authors: Aaron Warner (aawarner@cisco.com)
Description:    Simple IOS-XE configuration Generator. Run program and browse to 127.0.0.1:5000
"""

import jinja2
import os
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
app = Flask(__name__)

@app.route("/")
def webroot():
    return render_template("index.html")

@app.route("/success", methods = ["GET"])
def success():
    return render_template("success.html")

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
    return redirect(url_for("success"))

if __name__ == '__main__':
    app.run()