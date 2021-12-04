# FocusMate

A quick hack to add a manual, physical focus knob to webcam:



https://user-images.githubusercontent.com/8253488/144701611-5f131b07-f3ba-4408-bb25-e96bb649a4c4.mp4



Specifically, the Logitech C920 is notorious for regularly re-focussing:

> The webcam will refocus regularly, making the entire video flash out of and then back into focus (another issue is that it often focuses on the wrong thing, but that's less common [SNIP] ). I actually just had a call yesterday with a friend of mine who was using a different setup than I'd normally seen him with, the mediocre but perfectly acceptable macbook webcam. His video was going in and out of focus every 10-30 seconds, so I asked him if he was using [the Logitech C920] and of course he was 
> _[- Dan Luu](https://danluu.com/why-benchmark/)_

Also see [here](https://support.logi.com/hc/en-001/community/posts/360049083554-C920-Webcam-Focus-issues) and [here](https://support.logi.com/hc/en-001/community/posts/360052156173-C920-Focus-Issues).

This quick hack solves the focus issue by:
* Turns off autofocus
* Sets the focus to 0 (should be in focus if you 20"+ away)
* Allows you to use your [PowerMate](https://support.griffintechnology.com/product/powermate/) to focus
* Push PowerMate to snap to macro for when you inevitably need to share a picture on your phone by shoving in you webcam's face.
* Push PowerMate to snap back to prior focus

This is done by repurposing the awesome [Cattmate code](https://github.com/mrjones-plip/cattmate) I wrote some years ago. Now I have one knob for volume and one for focus on my desk! I'm going to need more knobs soon ...

## Status   

This project is very much a work in progress. Don't 
use unless you're looking to learn and experiment like am right now ;)

It is hard coded to use `/dev/video0` for your webcam and assumes `v4l-utils` is installed.

## Hardware

* PowerMate - Hopefully you can find one used on eBay if you don't already have one
* A webcam, hopefully not the janky focus ridden C920

## Install

1. Make sure the following requirements are installed:
   * [pip3](https://pip.pypa.io/en/stable/installing/)
   * [virtualenv](https://virtualenv.pypa.io/en/stable/) (_optional_)
1. Clone this repo `git clone https://github.com/Ths2-9Y-LqJt6/cattmate.git`
1. Change directories to cattmate `cd focusmate`
1. Create your own virtualenv and activate it `python3 -m venv venv;. venv/bin/activate` (_optional_)
1. Install all the python prerequisites with `pip3 install -r requirements.txt`
1. Start the cattmate controller `python3 FocusMate.py`

## Use

After getting your hardware and software set up per above, cattmate supports:
* Increase focus - rotate clockwise
* Decrease focus - rotate counter-clockwise
* Toggle Macro mode - push down


## Releases

* 3 Dec 2021 v0.1.0 - first PoC hack
