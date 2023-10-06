class SCARA:
    def __init__(self):
        self.maxStep = 1000
        self.vals = [0,0,0,0] # Current values
        self.mapped_vals = [0,0,0,0]
        self.motor_vals = [0,0,0,0]
        self.prev_vals = [0,0,0,0]


        self.MAX_BASE = 8000
        self.MIN_BASE = -8000
        self.BASE_STEP = 88 # ~1 degree
        self.base_val = 0

        self.MAX_GRIPPER = 1750
        self.MIN_GRIPPER = -1750
        self.GRIPPER_STEP = 19 # ~1 degree
        self.gripper_val = 0

        self.MAX_ARM = 6250
        self.MIN_ARM = -6250
        self.ARM_STEP = 69 # ~1 degree
        self.arm_val = 0

        self.baseFlg = False
        self.armFlg = False
        self.gripperFlg = False

    def _map(self,x, in_min, in_max, out_min, out_max):
        ratio = (out_max-out_min) / (in_max-in_min)
        mid = (in_max-in_min) / 2
        return int((x - mid) * ratio)

    def _check_value_change(self):
        if abs(self.prev_vals[0] - self.mapped_vals[0]) > 1: self.baseFlg = True
        if abs(self.prev_vals[1] - self.mapped_vals[1]) > 1: self.armFlg = True
        if abs(self.prev_vals[2] - self.mapped_vals[2]) > 1: self.gripperFlg = True

    def potentioMove(self,received_vals):
        self.vals = received_vals
        pub_vals = None
        for i in range(4):
            self.mapped_vals[i]= self._map(self.vals[i],0,2047,-90,90)

        self._check_value_change()

        if self.baseFlg:
            change_val = (self.mapped_vals[0] - self.prev_vals[0]) * self.BASE_STEP
            self.motor_vals[0] -= change_val
            self.prev_vals[0] = self.mapped_vals[0]
            pub_vals = ['/motor/base', -change_val, self.motor_vals[0], self.vals, self.mapped_vals, self.motor_vals]
            self.baseFlg = False
        
        if self.armFlg:
            change_val = (self.mapped_vals[1] - self.prev_vals[1]) * self.ARM_STEP
            self.motor_vals[1] -= change_val
            self.prev_vals[1] = self.mapped_vals[1]
            pub_vals = ['/motor/arm', -change_val, self.motor_vals[1], self.vals, self.mapped_vals, self.motor_vals]
            self.armFlg = False

        if self.gripperFlg:
            change_val = (self.mapped_vals[2] - self.prev_vals[2]) * self.GRIPPER_STEP
            self.motor_vals[2] += change_val
            self.prev_vals[2] = self.mapped_vals[2]
            pub_vals = ['/motor/gripper', change_val, self.motor_vals[2] ,self.vals, self.mapped_vals, self.motor_vals]
            self.gripperFlg = False
        
        return pub_vals

    def safe_exit(self):
        pub_vals = ['/motor/base', -self.motor_vals[0],'/motor/arm', -self.motor_vals[1],'/motor/gripper', -self.motor_vals[2]]
        for i in range(4):
            self.motor_vals[i] -=self.motor_vals[i]
        return pub_vals