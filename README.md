# PrusaSlicer command line slicing scripts

Author: Mitchell Lane (theskyishard)

## Description:

This repo is intended to simplify the process of slicing multiple STLs using PrusaSlicer by leveraging the command line interface.

## Prerequisites:

* PrusaSlicer must be installed
* `prusa-slicer-console.exe` must be on your PATH
* Python 3 must be installed

## PrusaSlicer configuration profiles

The command line tooling for PrusaSlicer does not use the same configuration files available in the GUI application, as such any profiles you want to use must be exported and passed into the tool. If you want to use multiple profiles (for example to compartmentalize print/filament/printer settings) then this becomes a bit laborious to export from the GUI.

The `split-config-bundle.py` script included here simplifies the usage of configuration profiles. Export all your profiles as a bundle from the GUI (File > Export > Export Config Bundle...) and then run the script to extract every profile into individual files that can be used with the command line tooling.

### Usage

Call the script and pass a relative path to the exported config bundle from PrusaSlicer:  
`python split-config-bundle.py ".\export-profiles\PrusaSlicer_config_bundle.ini"`

## Slicing an STL

To slice an STL file using this tooling, first ensure that you have exported any print/filament/printer profiles you need to use from PrusaSlicer into the 'export-profiles' subfolder.

By default, the script requires a target STL file path (-t parameter) and a configuration profile file path to use for the slicing (-p parameter):  
`python export-and-slice.py -t .\fillet_gauge.stl -p '.\export-profiles\automated-slicing-config.ini'`

Optionally, any arbitrary parameters for the `prusa-slicer-console.exe` tool can be passed in via the user parameters option (--u parameter) to allow for more complex usage cases. For example, if you wish to combine specific print/filament/printer profiles like you would in the GUI application then you can just pass in some extra `--load` parameters:  
`python export-and-slice.py -t .\fillet_gauge.stl -p '.\export-profiles\print_Mitch 0.07mm ULTRADETAIL @MK3.ini' --u '--load \".\export-profiles\filament_Prusament PETG - Mitch.ini\" --load \".\export-profiles\printer_Mitch - Prusa i3 MK3S.ini\"'`

Information on the available command line parameters can be found in the [Slic3r manual](https://manual.slic3r.org/advanced/command-line).