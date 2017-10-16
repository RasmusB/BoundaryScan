************************************************************************************
* @file    readme.txt                                                              
* @author  MCD Application Team                                                    
* @version V2.0                                                                    
* @date    01-September-2015                                                          
* @brief   Boundary Scan Description Language(BSDL) files for the STM32F1 MCUs.    
************************************************************************************
* COPYRIGHT(c) 2015 STMicroelectronics                                             
*                                                                                  
* Redistribution and use in source and binary forms, with or without modification, 
* are permitted provided that the following conditions are met:                    
*   1. Redistributions of source code must retain the above copyright notice,      
*      this list of conditions and the following disclaimer.                       
*   2. Redistributions in binary form must reproduce the above copyright notice,   
*      this list of conditions and the following disclaimer in the documentation  
*      and/or other materials provided with the distribution.                      
*   3. Neither the name of STMicroelectronics nor the names of its contributors    
*      may be used to endorse or promote products derived from this software       
*      without specific prior written permission.                                  
*                                                                                  
* THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"      
* AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE        
* IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE   
* DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE     
* FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL       
* DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR       
* SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER       
* CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,    
* OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE    
* OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.             
*************************************************************************************


=======================
How to use BSDL Files :
=======================

The STM32F1xx MCUs integrate two serially connected JTAG TAPs, the boundary scan
TAP (IR is 5-bit wide) and the Cortex-M3 TAP (IR is 4-bit wide).

The package contains :

   + A BSDL File for the Cortex-M3 TAP and is common to all STM32F2xx devices.

   + Boundary scan BSDL Files for each STM32F1xx, STM32F2xx and STM32L1xx device on different packages :
     o Low-density devices are STM32F101xx, STM32F102xx and STM32F103xx
       microcontrollers where the Flash memory density ranges between 16 and 32 Kbytes.
         ->LQFP64 - LQFP48 - VFQFPN36 - UFQFPN48 - TFBGA64.

     o Medium-density devices are STM32F101xx, STM32F102xx and STM32F103xx
       microcontrollers where the Flash memory density ranges between 64 and 128 Kbytes.
         ->LQFP100 - LQFP64 - LQFP48 - VFQFPN36 - UFQFPN48 - BGA100 - UFBGA100 - BGA64.

     o High-density devices are STM32F101xx and STM32F103xx microcontrollers where
       the Flash memory density ranges between 256 and 512 Kbytes.
         ->LQFP144 - LQFP100 - LQFP64 - LFBGA144 - LFBGA100 - WLCSP64.

     o XL-density devices are STM32F101xx and STM32F103xx microcontrollers where the
       Flash memory density ranges between 768 Kbytes and 1 Mbyte.
         ->LQFP144 - LQFP100 - LQFP64 - LFBGA144.

     o Connectivity line devices are STM32F105xx and STM32F107xx microcontrollers.
         ->LQFP100 - LQFP64 - LFBGA100.

     o Low-density value line devices and Medium-density value line are STM32F100xx
       microcontrollers where the Flash memory density ranges between 16 and 128 Kbytes.
        ->LQFP100 - LQFP64 - LQFP48 - TFBGA64.

     o High-density value line devices and Medium-density value line are STM32F100xx
       microcontrollers where the Flash memory density ranges between 256 and 512 Kbytes.
         ->LQFP144 - LQFP100 - LQFP64.

In order to run boundary scan, always provide two BSDL files to your JTAG Boundary scan tool:
the "CortexM3.bsd" and your selected "STM32xx_device_Package.bsd".  

WARNING : Do not combine both BSDL files in a single TAP with 9-bit wide !

For more details on the internal TAPs description refer to the Reference Manual
of the selected STM32xxxx device , Section : JTAG TAP connection.

==========================
* V2.0 - 01-September-2015  
==========================

New Features
************
    + Adding BSDL File of STM32F1xx Medium-density devices Boundary Scan TAP : UFBGA100

========================
* V1.2 - 03 January 2011
========================

New Features
************
    + Adding BSDL Files of STM32F1xx Value line High density devices Boundary Scan TAP

======================
* V1.1 - 30 Juin 2010 
======================

New Features
************
    + Adding BSDL Files of STM32F1xx Value line and XL density devices Boundary Scan TAP
    + Adding BSDL Files of STM32F1xx Connectivity devices Boundary Scan TAP
    + Adding BSDL Files of STM32F1xx High density devices Boundary Scan TAP
    + Adding BSDL Files of STM32F1xx Low density devices Boundary Scan TAP
    + Add    BSDL file for Cortex-M3 TAP

======================
* V1.0 - 16 May 2008  
======================
  Created.
  

******************* (C) COPYRIGHT 2015 STMicroelectronics *****END OF FILE
