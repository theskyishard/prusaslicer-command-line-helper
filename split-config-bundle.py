# Run me with the target config bundle path passed in - e.g. python split-config-bundle.py ".\export-profiles\PrusaSlicer_config_bundle.ini"
import sys
import os

class Config:
    def __init__(self, fileName, contents):
        self.fileName = fileName
        self.contents = contents

def main(targetBundlePath):
    print("Looking for configuration sections in file '" + targetBundlePath + "'")

    with open(targetBundlePath, "r") as bundleContents:
        line = bundleContents.readline()

        # skip over the first few lines until we get to a valid config
        while line and not line.startswith("["):
            line = bundleContents.readline()

        configurationsFound = []
        while line:
             # Pull apart the first line, which contains a config header in the format '[<print/filament/printer>:<profile name>]'
            rawConfigHeader = line[1:-2] # Strip off the [ and ] characters at the start and end of the line

            # Bail out completely when we hit the presets section, it means we are past any meaningful config...
            if rawConfigHeader == "presets":
                break

            configHeaderComponents = rawConfigHeader.split(":", 1)
            configType = configHeaderComponents[0]
            fileName = (configType + "_" + configHeaderComponents[1] + ".ini") # Keep config type in the output file name so users can easily load multiple configuration files in
            
            print("Found config section: " + configHeaderComponents[1])

            # Read on to the config contents
            line = bundleContents.readline()
            contents = []

            while line and not line.startswith("["):
                contents.append(line)
                line = bundleContents.readline()

            configurationsFound.append(Config(fileName, contents))
        
        print("Found " + str(len(configurationsFound)) + " configurations in total")

        outputDir = "export-profiles"
        for configuration in configurationsFound:
            outputFileName = os.path.join(outputDir, configuration.fileName)

            print("Writing configuration to '" + outputFileName + "'")
            with open(outputFileName, "w") as outputFile:
                for configLine in configuration.contents:
                    if configLine.rstrip():
                        outputFile.write(configLine)

        print("All configuration written to separate files")

if __name__ == '__main__':
    main(str(sys.argv[1]))