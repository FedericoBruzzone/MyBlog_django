# The blog with django

[![Python](https://img.shields.io/badge/Python-3.8.8-orange)](https://docs.python.org/3/)
[![Django](https://img.shields.io/badge/Django-4.0.6-orange)](https://www.djangoproject.com/)
[![stability-stable](https://img.shields.io/badge/stability-stable-green.svg)](https://github.com/emersion/stability-badges#stable)

# Introduction


---

# Setup 

1. Install [Visual studio Code](https://visualstudio.microsoft.com) or your favourite text editor

2. Install [git](https://github.com/git-guides/install-git). 

    I would recommend you to use git bash to run terminal commands.

3. Intall [python](https://www.python.org/downloads/). 

    I would recommend you to install [3.8.8](https://www.python.org/downloads/release/python-388/) version.

### First step
Now, you can fork or clone this repository and in the folder you can try to set up the python development environment.

```cmd
    $ python -m venv virt
```

### Second step

In the JUCE folder in documents (JUCE/extras/AudioPluginHost), there is juce Host called AudioPluginHost, this allows to test our code without a DAW (Digital Audio Workstation).

You have to open AudioPluginHost.jucer on Projucer and later in Visual Studio 2022, and compile it in debug mode.

### Third step

Now, you can re-open the "Shimmer" project, and pressing with the right button on "Shimmer_VST3" and in debug menu you can set the path of your AudioPluginHost (.\Documents\JUCE\extras\AudioPluginHost\Builds\VisualStudio2022\x64\Debug\App\AudioPluginHost.exw) on command space.

And, pressing with the right button on "Shimmer_VST3" another time, and click
"Set as Sturtup project".

Now, try to run the Shimmer with Local Windows Debugger button.

# Troubleshooting
If you find problems with the source code or configuration, please contact me at federico.bruzzone.i@gmail.com.

If this is your first time using juce, i understand that the configuration of this project is not easy.

# Full screen GUI
![Shimmer_VST3](./Docs/Shimmer_VST3.png)

