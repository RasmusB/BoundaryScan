# General Concept
There are a few different use cases I want to handle. Most of them revolve around being able to test and program my own designs. These will range from really simple (my keyboard adapter) to pretty advanced (PsioPi mainboard).

Some of this could be handled by a bed of nails approach only. But without special HW test software, this won't do much. Also, if something is keeping the MCU from operating and communicating (open solder joints on the crystal, communication interface, reset line etc.), the software is pretty useless.

1. Test the board for connectivity
  - This is what a boundary scan test was designed to do.
  - It is only possible to test connectivity for parts with TAP interfaces that are actually connected.
  - It should be possible to test each and every pin for connectivity by combining the boundary scan test with a bed-of-nails approach.
  - This also verifies that we have power to the ICs, and that the correct IC has been placed on the board.
1. Test other components
  - For this, an analog switching matrix is needed, and a lot of test points. Making the test program itself also requires some thought. But the basis is simple - I need at least one DAC channel and one ADC channel, preferrably two. I really need to think my analog MUXes through. For example, if I buy very large MUXes (8:1), I can only use one of the pins connected to it...
