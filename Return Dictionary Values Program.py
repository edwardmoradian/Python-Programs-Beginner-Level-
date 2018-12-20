# Author:  Edward Moradian


MeanRadius = {"Io":1821.6, "Europa":1560.8, "Ganymede":2634.1, "Callisto":2410.3}

SurfaceGravity = {"Io":1.796, "Europa":1.314, "Ganymede":1.428, "Callisto":1.235}

OrbitalPeriod = {"Io":1.769, "Europa":3.551, "Ganymede":7.154, "Callisto":16.689}

def main():
    UserInput = input("Enter the moon name: ")
    
    MeanRadiusOutput = MeanRadius.get(UserInput,"Entry not found")
    print("Mean Radius:", MeanRadiusOutput, "kilometers")

    SurfaceGravityOutput = SurfaceGravity.get(UserInput,"Entry not found")
    print("Surface Gravity:", SurfaceGravityOutput, "mps^2")
    
    OrbitalPeriodOutput = OrbitalPeriod.get(UserInput,"Entry not found")
    print("Orbital Period:", OrbitalPeriodOutput, "days")

main()