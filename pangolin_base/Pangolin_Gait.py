from Pangolin_Config import PangolinConfiguration


class PangolinGait:
    def __init__(self):
        """Initialize the gait generator with default values from configuration."""

        self.pangolin_config = PangolinConfiguration()
        self.move_forward  = self.pangolin_config.move_forward
        self.move_backward = self.pangolin_config.move_backward

        self.turn_forward  = self.pangolin_config.turn_forward
        self.turn_backward = self.pangolin_config.turn_backward

        self.set_gait_dic() # Initialize the gait dictionary



    def set_gait_dic(self):
        """A dictionary for gait patterns."""

        self.gait_dic =    {
                            "move_linear": [[ self.move_forward, self.move_backward, self.move_backward,  self.move_forward],
                                            [ self.move_forward,                  0,                  0,  self.move_forward],
                                            [self.move_backward,                  0,                  0, self.move_backward],
                                            [self.move_backward,  self.move_forward,  self.move_forward, self.move_backward],
                                            [                 0,  self.move_forward,  self.move_forward,                  0],
                                            [                 0, self.move_backward, self.move_backward,                  0],
                            ],

                            "turn_left":   [[                 0,                  0,                  0,                  0],
                                            [self.turn_backward,                  0,                  0,  self.turn_forward],
                                            [self.turn_backward, self.turn_backward,  self.turn_forward,  self.turn_forward],
                                            [                 0, self.turn_backward,  self.turn_forward,                  0],
                            ],

                            "turn_right":  [[                 0, self.turn_backward,  self.turn_forward,                  0],
                                            [self.turn_backward, self.turn_backward,  self.turn_forward,  self.turn_forward],
                                            [self.turn_backward,                  0,                  0,  self.turn_forward],
                                            [                 0,                  0,                  0,                  0],
                            ],
                            "IDLE":         [[                0,                  0,                  0,                  0],
                                            [                 0,                  0,                  0,                  0],
                            ],
                            }

    