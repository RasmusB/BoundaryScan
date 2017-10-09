# JTAG

## State handling
- [State handling in JTAG](http://www.fpga4fun.com/JTAG2.html)

## Project flow
- Figure out how to use the cable with OpenOCD
  - [This might be a good reference](https://www.allaboutcircuits.com/technical-articles/getting-started-with-openocd-using-ft2232h-adapter-for-swd-debugging/)
  - [JTAG reference](https://balau82.wordpress.com/2013/08/04/jtag-connection-with-openocd-and-ftdi-cable/)
- Start OpenOCD
  - Find a correct .cfg file for the FT232H cable you will be using
- Prepare a suitable target
  - Blue pill board
  - Some sources claim that NRST must be active during JTAG operations.
    - This makes a lot of sense but should be confirmed.
    - ~~Prepare the target with a jumper cable to ground the NRST pin. Perhaps this can be put under control of OpenOCD later on?~~
      - A reset pin is included in the interface of the FT232H. This _should_ mean that OpenOCD does the correct thing with it, and I should not add any jumper wires.
        - This is apparently handled by the configuration file. See [this link](http://openocd.org/doc-release/html/Debug-Adapter-Configuration.html#index-ftdi).
- Connect to OpenOCD through a telnet client
  - Start with a manual input to explore the options
  - OpenOCD has a lot of features to handle device states. Check if we can switch states through a single command; similar to `set_jtag_state(reset);`
  - One thing to start experimenting with early, is detecting the scain chain length (usign the `BYPASS` JTAG feature). If the autoprobing works as advertised, we should be able to map the BSDL file contents to the actual TAP:s automatically

## What I want the software to do
- Basically the software should have an expectation of what is connected to the scan chain. This can be accomplished by parsing the .bsdl files and creating corresponding data objects. For a first prototype, it should be enough to manually create .json files or similar to contain the same data.
- When connected, the software should check _at least_ the scan chain length first. This will function as a "sanity check" to make sure that the JTAG connection itself is working.
- When we have gotten this far, we can try to autoprobe the scan chain. If possible, the actual scan chain will be compared to the expected one and matched up. Is there is any ambiguity, the program might ask the user for input. (For example, the user might choose to ignore any unidentified targets in the chain with a `BYPASS` command.)
- At this point, we should be able to start a boundary scan. Each BS TAP in the chain should be indentified at this point.
  - This won't do much for us if we don't know what connections our target implements. We need some way to go from a netlist to a mapping of the actual I/O of the chips in the chain. This might both be tricky and impose some limitations for the footprints! A naive approach (but pretty fool-proof) would be to match the pin numbers that are present in both the netlist and the .bsdl file. This assumes unique pin numbers, but that is usually the case anyway. If the JTAG net names used in the netlist are known, we should be able to determine the scan chain order from the netlist.

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
