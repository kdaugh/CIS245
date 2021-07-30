class Vehicle:

    def __init__(self, make, model, color, fuelType, options):
        self.make = make
        self.model = model
        self.color = color
        self.fuelType = fuelType
        self.options = options

    def getMake(self):
        self.make = input('\nPlease enter the vehicle make: ').title()
        return self.make

    def getModel(self):
        self.model = input('Please enter the vehicle model: ').title()
        return self.model

    def getColor(self):
        self.color = input('Please enter the vehicle color: ').lower()
        return self.color

    def getFuelType(self):
        self.fuelType = input('Please enter the vehicle fuel type: ').lower()
        return self.fuelType

    def getOptions(self):
        optionslist = []
        print('\nEnter "Y" or "N" for the following options:')
        entry = input('Does your vehicle have keyless entry? ').lower()
        bluetooth = input('Does your vehicle have bluetooth? ').lower()
        hseats = input('Does your vehicle have heated seats? ').lower()
        window = input('Does your vehicle have power windows? ').lower()
        lock = input('Does your vehicle have power locks? ').lower()
        mirror = input('Does your vehicle have power mirrors? ').lower()
        rstart = input('Does your vehicle have remote start? ').lower()
        camera = input('Does your vehicle have a backup camera? ').lower()

        if entry == 'y':
            optionslist.append('keyless entry')
        if bluetooth == 'y':
            optionslist.append('Bluetooth')
        if hseats == 'y':
            optionslist.append('heated seats')
        if window == 'y':
            optionslist.append('power windows')
        if lock == 'y':
            optionslist.append('power locks')
        if mirror == 'y':
            optionslist.append('power mirrors')
        if rstart == 'y':
            optionslist.append('remote start')
        if camera == 'y':
            optionslist.append('backup camera')

        self.options = optionslist
        return self.options


class Car(Vehicle):
    def __init__(self, make, model, color, fuelType, options, engineSize, numDoors):
        self.engineSize = engineSize
        self.numDoors = numDoors
        Vehicle.__init__(self, make, model, color, fuelType, options)

    def getEngineSize(self):
        self.engineSize = input('Please enter your engine size in liters: ')
        return self.engineSize

    def getNumDoors(self):
        self.numDoors = input('Please enter the number of doors: ')
        return self.numDoors



class Pickup(Vehicle):
    def __init__(self, make, model, color, fuelType, options, cabStyle, bedLength):
        self.cabStyle = cabStyle
        self.bedLength = bedLength
        Vehicle.__init__(self, make, model, color, fuelType, options)

    def getCabStyle(self):
        self.cabStyle = input('Please enter the cab style: ')
        return self.cabStyle

    def getBedLength(self):
        self.bedLength = float(input('Please enter the bed length (in feet): '))
        return self.bedLength


instances = []
Exit = 'n'
x = 0
while Exit == 'n':
    print('\n----Press "1" to add a car')
    print('----Press "2" to add a pickup truck')
    print('----Press "3" to quit')
    carTruck = input('\nWhat is your selection? ')
    instances.append(carTruck)

    if carTruck == '1':

        instances[x] = Car('', '', '', '', '', '', '')

        instances[x].getMake()
        instances[x].getModel()
        instances[x].getColor()
        instances[x].getFuelType()
        instances[x].getEngineSize()
        instances[x].getNumDoors()
        instances[x].getOptions()
        if not instances[x].options:
            print('\nYou need to select at least one option.')
            Vehicle.getOptions(instances[x])

    elif carTruck == '2':
        instances[x] = Pickup('', '', '', '', '', '', '')

        instances[x].getMake()
        instances[x].getModel()
        instances[x].getColor()
        instances[x].getFuelType()
        instances[x].getCabStyle()
        instances[x].getBedLength()
        instances[x].getOptions()
        if not instances[x].options:
            print('\nYou need to select at least one option.')
            Vehicle.getOptions(instances[x])

    elif carTruck == '3':
        print('\nGoodbye')
        exit()

    else:
        print(f'"{carTruck}" is not a valid selection.')

    Exit = input('\nAre you done adding vehicles? (Y/N): ').lower()
    x = x + 1

b = 0
print("\n----My Virtual Garage----")
while b < len(instances):
    if isinstance(instances[b], Pickup):
        print(f'\nVehicle {b + 1}: A {instances[b].color} {instances[b].make} {instances[b].model} {instances[b].cabStyle} and a {instances[b].bedLength} ft bed that runs on {instances[b].fuelType}.')
        print(f'\t\t   This pickup comes with ' + ", ".join(instances[b].options) + '.\n')
    elif isinstance(instances[b], Car):
        print(f'\nVehicle {b + 1}: A {instances[b].color} {instances[b].make} {instances[b].model} {instances[b].numDoors} door with a {instances[b].engineSize} liter {instances[b].fuelType} engine.')
        print(f'\t\t   This car comes with ' + ", ".join(instances[b].options) + '.\n')
    b = b + 1