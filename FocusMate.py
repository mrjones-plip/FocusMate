import time, signal, sys, logging, os, glob, subprocess, powermate.powermate

logging.basicConfig(filename=os.path.dirname(os.path.abspath(__file__)) + "/error.log")
MAX_FOCUS = 100


def set_focus(depth):
    try:
        # /usr/bin/v4l2-ctl -d /dev/video0 -c focus_absolute=0
        subprocess.run(["/usr/bin/v4l2-ctl", "-d", "/dev/video0", "-c", "focus_absolute=" + str(depth)])
        print("focus to ", depth)
    except OSError as e:
        print("Execution failed:", e, file=sys.stderr)


def sigint_handler(signal, frame):
    print('Exit via ctrl + c')
    sys.exit(0)


class FocusMate(powermate.powermate.PowerMateBase):
    def __init__(self, path):

        print('Initializing PowerMate: ' + path)

        try:
            glob_path = glob.glob(path)[0]
            super(FocusMate, self).__init__(glob_path)
        except IndexError as e:
            logging.error(logging.exception(e))
            sys.exit("ERROR: Couldn't connect PowerMate at '" + path +
                     "'. Is it plugged in and is the udev file installed per readme.md?")

        print('Turning off Camera Autofocus')
        subprocess.run(["/usr/bin/v4l2-ctl", "-d", "/dev/video0", "--set-ctrl=focus_auto=0"])

        # v4l2 - ctl - -set - ctrl = focus_auto = 0
        self._macro = False
        self._paused = False
        self._focus = 20
        set_focus(self._focus)

        print('Successfully started!')

    def short_press(self):
        self._macro = not self._macro
        if self._macro:
            set_focus(100)
            return powermate.powermate.LedEvent.pulse()
        else:
            set_focus(self._focus)
            return powermate.powermate.LedEvent(brightness=self._focus)

    # def long_press(self):
    #     self._paused = not self._paused
    #     if self._paused:
    #         print('Paused')
    #     else:
    #         print('Playing')

    def rotate(self, rotation):
        self._focus = max(0, min(MAX_FOCUS, self._focus + rotation))
        self._macro = False
        set_focus(self._focus)

        return powermate.powermate.LedEvent(brightness=self._focus)

    # def push_rotate(self, rotation):
    #     if rotation > 0:
    #         action = 'ffwd'
    #     else:
    #         action = 'rrnd'
    #
    #     if config.use_display:
    #         try:
    #             self.screen.display(action)
    #         except Exception as e:
    #             logging.error(logging.exception(e))
    #
    #     if rotation > 0:
    #         self.cast.ffwd(2)
    #     else:
    #         self.cast.rewind(2)
    #
    #     print(action)


class ExampleBadHandler(powermate.powermate.PowerMateEventHandler):
    def rotate(self, rotation):
        while True:
            time.sleep(4)


if __name__ == "__main__":
    print("Trying to start...")
    signal.signal(signal.SIGINT, sigint_handler)
    pm = FocusMate('/dev/input/by-id/*PowerMate*')
    pm.add_listener(ExampleBadHandler())
    pm.run()
