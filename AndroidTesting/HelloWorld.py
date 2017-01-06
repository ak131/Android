# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

def main():
    print('Testing Started...')

    # Connects to the current device, returning a MonkeyDevice object
    device = MonkeyRunner.waitForConnection()
    print("Device Connected")

    # Installs the Android package. Notice that this method returns a boolean, so you can test
    # to see if the installation worked.
    device.installPackage('app.apk')
    print("Application Installed")


    package = 'com.example.helloworld'
    activity = 'com.example.helloworld.MainActivity'
    runcomponent = package + '/' + activity
    # Runs the component
    device.startActivity(component=runcomponent)
    print('Application Started')

    MonkeyRunner.sleep(2)

    result = device.takeSnapshot()
    result.writeToFile('test.png','png')

    device.removePackage('com.example.helloworld')
    print('Application Uninstalled')

    print('\nDone! End of Testing.')
    return

if __name__ == "__main__":
    main()