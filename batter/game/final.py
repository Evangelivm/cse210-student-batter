from asciimatics.event import KeyboardEvent
from asciimatics.screen import Screen

class Final:
    """Helps with the final part to print when the user press ESC
    Stereotype: 
        Service Provider"""



    def __init__(self):

        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self.screen = Screen
        
    def demo(self):
        final_text = f" _____                                            \
\n|  __ \                                           \
\n| |  \/ __ _ _ __ ___   ___    _____   _____ _ __ \
\n| | __ / _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|\
\n| |_\ \ (_| | | | | | |  __/ | (_) \ V /  __/ |   \
\n \____/\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|   \
\n                                                  \
\n                                                  \
\n _____ _                 _                        \
\n|_   _| |               | |                       \
\n  | | | |__   __ _ _ __ | | __  _   _  ___  _   _ \
\n  | | | '_ \ / _` | '_ \| |/ / | | | |/ _ \| | | |\
\n  | | | | | | (_| | | | |   <  | |_| | (_) | |_| |\
\n  \_/ |_| |_|\__,_|_| |_|_|\_\  \__, |\___/ \__,_|\
\n                                 __/ |            \
\n                                |___/             "
        return print(final_text)