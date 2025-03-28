# Multigroup PSO GUI

This application provides an interface for setting up, configuring, running, and the visualization of multigroup PSO training.

## Instructions for Ubuntu

To run the interface you must also install Tkinter:

```bash
sudo apt install python-tk
```

To install the interface simply run:

```bash
python3 -m pip install mg-pso-gui
```

Once the package is downloaded and install run this command to open the interface:

```bash
mgpsogui
```

You may need to add a folder to PATH.

**Note:** If you run into an error saying that PIL.Image was not able to be imported on Ubuntu please force reinstall Pillow.

```bash
python3 -m pip install --upgrade --force-reinstall Pillow
```

## Instructions for Windows

Download and install Python 3.10 through the Microsoft Store, this makes Python easily accessible in Windows Terminal.

Once installed run this command to install the interface:

```bash
python3 -m pip install mg-pso-gui
```

You may need to add the folder the application was downloaded to into PATH. At the end of the installation message it will say the folder location (e.g. C:\Users\robertcordingly\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts). After adding that location to PATH, you can use this command to open the interface:

```bash
mgpsogui
```

If you did not add the directory to PATH, it can be ran like this:

```bash
C:\Users\robertcordingly\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts\mgpsogui.exe
```

## Instructions for MacOS

To install Tkinter and Python 3 it is best to use Homebrew:

Install Homebrew

```bash
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Install Python3 and Tkinter

```bash
brew install python3
```

```bash
brew install tkinter
```

Then install MG PSO Gui:

```bash
python3 -m pip install mg-pso-gui
```

You may need to add /Library/Frameworks/Python.framework/Versions/3.10/bin to path to run the interface with 'mgpsogui,' otherwise run the interface:

```bash
/Library/Frameworks/Python.framework/Versions/3.10/bin/mgpsogui
```

# Getting Started

After getting the GUI to launch, it is first recommended to start with one of the default config files. Default config files are available here: https://drive.google.com/file/d/1Ra4Um7KgCghMidyrrLrD6wFSXJZd3zkX/view?usp=share_link

To load a config simply click the "load" button in the left side bar and select the file using the file picker. After a config has been loaded, enter a service URL, and click "Connect".  If the connection is successful the other tabs on the interface will be unlocked and you will have full access to all of the interface's features.

# Tab Overview

Each tab of the interface serves a different purpose described here.

## Platform

The platform tab is where you defined the backend service used to train the model. If the service already exists, simply add the URL to the service field and press connect to get parameters from the service. After doing this the other tabs will unlock.

If you do not already have a backend service deployed, the platform tab provides tools to create a local environment using Docker and Minikube.

## Setup

The setup tab is where all parameters about the training process are defined. The Group Editor allow you to define groups, the parameters each group uses, and the functions used. The available parameters are defined by the service.

Alongside the Group Editor is the Static Parameter and Calibration Parameter editors. These editors allow further customization of the training process.

## Run

The run tab allows you to start the training process, stop it, and view the progress. If there is an error in the training process information will be shown in the text box.

## Visualize

The Visualize tab allows you to generate a variety of different graphs and tables. Some graphs are filled in while the training process occurs while other require full steps to complete training. To export and further view graphs the "Open in Browser" allows a figure to be opened in your default web browser and open and interactive version of the graph.

# Example Configuration

```json
{
    "arguments": {
        "param": [
            {
                "name": "startTime",
                "value": "2002-01-01"
            },
            {
                "name": "endTime",
                "value": "2006-12-31"
            },
            {
                "name": "dataStartTime",
                "value": "2002-01-01"
            },
            {
                "name": "dataEndTime",
                "value": "2006-12-31"
            },
            {
                "name": "cal_startTime",
                "value": "2003-01-01"
            },
            {
                "name": "cal_endTime",
                "value": "2006-12-31"
            },
            {
                "name": "parallelismThreads",
                "value": "2"
            },
            {
                "name": "flagLoadState",
                "value": "True"
            },
            {
                "name": "payload",
                "value": "false"
            },
            {
                "name": "project",
                "value": "SFIR3"
            }
        ],
        "url": "http://csip.engr.colostate.edu:8087/csip-oms/m/ages/0.3.0",
        "files": {}
    },
    "calibration_parameters": [
        {
            "name": "min_rounds",
            "value": "1"
        },
        {
            "name": "max_rounds",
            "value": "2"
        },
        {
            "name": "n_particles",
            "value": "10"
        },
        {
            "name": "iters",
            "value": "20"
        },
        {
            "name": "n_threads",
            "value": "10"
        },
        {
            "name": "ftol",
            "value": "NULL"
        },
        {
            "name": "options_c1",
            "value": "2"
        },
        {
            "name": "options_c2",
            "value": "2"
        },
        {
            "name": "options_w",
            "value": "0.8"
        },
        {
            "name": "strategy_w",
            "value": "adaptive"
        },
        {
            "name": "strategy_c1",
            "value": "adaptive"
        },
        {
            "name": "strategy_c2",
            "value": "adaptive"
        },
        {
            "name": "service_timeout",
            "value": "400"
        },
        {
            "name": "http_retry",
            "value": "5"
        },
        {
            "name": "allow_redirects",
            "value": "True"
        },
        {
            "name": "async_call",
            "value": "False"
        },
        {
            "name": "conn_timeout",
            "value": "10"
        },
        {
            "name": "read_timeout",
            "value": "400"
        },
        {
            "name": "particles_fail",
            "value": "5"
        }
    ],
    "steps": [
        {
            "param": [
                {
                    "name": "soilOutLPS",
                    "bounds": [
                        0.0,
                        2.0
                    ]
                },
                {
                    "name": "lagInterflow",
                    "bounds": [
                        10.0,
                        80.0
                    ]
                }
            ],
            "objfunc": [
                {
                    "name": "ns",
                    "of": "ns",
                    "weight": 1.0,
                    "data": [
                        "obs_data02_14.csv/obs/orun[1]",
                        "output/csip_run/out/Outlet.csv/output/catchmentSimRunoff"
                    ]
                }
            ]
        },
        {
            "param": [
                {
                    "name": "flowRouteTA",
                    "bounds": [
                        0.4,
                        5.0
                    ]
                },
                {
                    "name": "soilMaxDPS",
                    "bounds": [
                        0.0,
                        5.0
                    ]
                }
            ],
            "objfunc": [
                {
                    "name": "ns",
                    "of": "ns",
                    "weight": 1.0,
                    "data": [
                        "obs_data02_14.csv/obs/orun[1]",
                        "output/csip_run/out/Outlet.csv/output/catchmentSimRunoff"
                    ]
                }
            ]
        }
    ]
}
```
