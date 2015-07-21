import math, time

class System:
    
    def __init__(self, stars, radius):
        self.stars = stars
        self.angular_speed = 1
        self.radius = radius
        self.total_brightness = self.stars[0].brightness + self.stars[1].brightness
        self.distance = radius * 2
        self.stars[0].pos = 2 * -self.radius
        self.stars[0].angle = 0
        self.stars[1].pos = 2 * self.radius
        self.stars[1].angle = 180
    
    def update(self):
        self.distance = 0
        for star in self.stars:
            star.move(self)
            if star.pos > 0:
                self.distance += star.pos
            else:
                self.distance -= star.pos
        print(self)
        
    def getOverlap(self):
        d = self.distance
        r = []
        for star in self.stars:
            r.append(star.radius)
        if d >= r[0] + r[1]:
            return 0
        else:
            theta = [0,0]
            x = [0,0]
            c = (-(d)**2-(r[1])**2+(r[0])**2)/2
            discriminant = math.sqrt(d**2 - (4*c))
            x[1] = (d+discriminant)/2
            x[0] = d - x[1]
            y = math.sqrt(r[0]**2-x[0]**2)
            theta[0] = math.acos((x[0]/r[0])*math.pi/180)
            theta[1] = math.acos((x[1]/r[1])*math.pi/180)
            area_s = [0,0]
            area_s[0] = (theta[0]*math.pi*(r[0]**2))/180
            area_s[1] = (theta[1]*math.pi*(r[1]**2))/180
            area_t = [0,0]
            area_t[0] = x[0] * y
            area_t[1] = x[1] * y
            area = [0,0]
            area[0] = area_s[0] - area_t[0]
            area[1] = area_s[1] - area_t[1]
            return area[0] + area[1]
    
    def getTotalBrightness(self):
        intersection = self.getOverlap()
        total = 0
        for star in self.stars:
            total += star.radius**2 * math.pi
        union = total - intersection
        return union
    
    def __str__(self):
#         toReturn = ""
#         for i in range(-self.radius, self.radius+1):
#             done = False
#             for star in self.stars:
#                 if int(star.pos) == i:
#                     toReturn = toReturn + "*"
#                     done = True
#             if done == True:
#                 pass
#             else:
#                 toReturn = toReturn + " "
#         return toReturn
        return str(self.distance) + " " +  str(self.getTotalBrightness())

class Star:
    
    def __init__(self, radius, brightness):
        self.pos = 0
        self.angle = 0
        self.radius = radius
        self.brightness = brightness

    def move(self, system):
        self.angle += system.angular_speed
        if self.angle > 360:
            self.angle -= 360
        self.pos = system.radius * math.cos(self.angle * math.pi/180)
    
binary = System([Star(5,100),Star(5,100)],50)

while True:
    binary.update()
    time.sleep(1)

