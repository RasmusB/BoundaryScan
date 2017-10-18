# JTAG

## Project flow
- [X] - Figure out how to use the cable with OpenOCD
  - [This is a good reference](https://www.allaboutcircuits.com/technical-articles/getting-started-with-openocd-using-ft2232h-adapter-for-swd-debugging/)
  - ~~[JTAG reference](https://balau82.wordpress.com/2013/08/04/jtag-connection-with-openocd-and-ftdi-cable/)~~ (Uses the old SW interface)
- [X] Start OpenOCD
  - [X] Find a correct .cfg file for the FT232H cable you will be using
- [X] Prepare a suitable target
  - [X] Blue pill board
  - Some sources claim that NRST must be active during JTAG operations.
    - [X] This makes a lot of sense but should be confirmed. [CONFIRMED]
    - [X] Prepare the target with a jumper cable to ground the NRST pin.
      - [ ] Perhaps this can be put under control of OpenOCD later on?
      - ~~A reset pin is included in the interface of the FT232H. This _should_ mean that OpenOCD does the correct thing with it, and I should not add any jumper wires.~~
        - [ ] This is apparently handled by the configuration file. See [this link](http://openocd.org/doc-release/html/Debug-Adapter-Configuration.html#index-ftdi).
- [X] Connect to OpenOCD through a telnet client
  - [X] Start with a manual input to explore the options
  - [X] One thing to start experimenting with early, is detecting the scain chain length (usign the `BYPASS` JTAG feature). If the autoprobing works as advertised, we should be able to map the BSDL file contents to the actual TAP:s automatically
    - This seems to work as exptected with the target i used. STM32 support the JTAG IdCode, so mapping should be simple.
  - [X] OpenOCD has a lot of features to handle device states. Check if we can switch states through a single command; similar to `set_jtag_state(reset);`
    - Yes we can! The command mode is `pathmove start_state [next_state ... final_state]` where start/final_state is one of the [stable states](http://openocd.org/doc-release/html/JTAG-Commands.html#TAP-state-names):
      - `RESET`
      - `RUN/IDLE`
      - `DRSHIFT`
      - `DRPAUSE`
      - `IRSHIFT`
      - `IRPAUSE`

## What I want the software to do
- Basically the software should have an expectation of what is connected to the scan chain. This can be accomplished by parsing the .bsdl files and creating corresponding data objects. For a first prototype, it should be enough to manually create .json files or similar to contain the same data.
- When connected, the software should check _at least_ the scan chain length first. This will function as a "sanity check" to make sure that the JTAG connection itself is working.
- [X] When we have gotten this far, we can try to autoprobe the scan chain. If possible, the actual scan chain will be compared to the expected one and matched up.
  - [ ] If there is any ambiguity, the program should ask the user for input. (For example, the user might choose to ignore any unidentified targets in the chain with a `BYPASS` command.)
- [ ] At this point, we should be able to start a boundary scan. Each BS TAP in the chain should be indentified at this point.
  - [X] Figure out how BS is done.
  - The easiest way is to have OpenOCD play back an .SVF file. This contains all features we need, and we won't need to use the low level JTAG commands. The SVF file format also includes expected response data, so we don't need to do any response evaluation in my script.
  - Since this actually moves the focus from implementing a complete boundary scanner to creating an appropriate SVF file, this just turned into a different project.

## SVF file creation
The file format of SVF files is not very complex, and the specification is publically available. The complex part is to create the test patterns, since that is an amalgamation of the content of the BSDL file(s) and the actual design of the PCB. Visualizing errors could also be useful but difficult to do from scratch. If two nets seems to be shorted together, it would be nice to be able to highlight them in the layout.

The quickest way forward should be to implement these features in KiCAD. KiCAD (at least pcbnew) can run Python scripts and access the design. Some useful features would be:
- Adding the correct .bsdl files as custom user fields per each component with a TAP interface
- Extracting the connectivity netlist
- Highlighting nets with errors
- Actual calculation of the scan chain (what if non-standard net names are used? Can we extract the JTAG pins from the BSDL file?)
- Calculating the test patterns
  - Basic connectivity (pin-to-pin)
  - Pull-ups and pull-downs
    - How strong are the BSDL cells? They _should_ override normal IO behavior, so pretty strong...
  - We could also make the script aware of test points. Perhaps even automatically create a bed-of-nails test board from the testpoint coordinates?
  - Indicate which nets in the schematic that are not covered by JTAG tests alone (giving the designer the option to add test points)

## BSDL to Python device structure
- Device (top level representing a IC package)
  - List of TAPs
    - TAP
      - Package name (NONE for core)
      - Port list
        - Port name, Port type
      - Pin map
        - Port name, pin number
      - Compliance pattern
        - Port name, logic value
      - Instruction register length
      - Implemented instructions
        - Name, opcode
      - Instruction capture value
      - ID code register definition
        - Version
        - Part number
        - Manufacturer
        - Extra bit ('1')
      - Register access - not clear what this is for
      - Boundary length - the length of the BS register
      - Boundary register
      - Design warning


  - TAP #2
    - ... (as above)
