BC660K-GL&BC950K-GL

AT Commands Manual

### NB-IoT Module Series

### Version: 1.

### Date: 2024-01-2 6

### Status: Released


At Quectel, our aim is to provide timely and comprehensive services to our customers. If you
require any assistance, please contact our headquarters:

Quectel Wireless Solutions Co., Ltd.
Building 5, Shanghai Business Park Phase III (Area B), No.1016 Tianlin Road, Minhang District, Shanghai
200233, China
Tel: +86 21 5108 6236
Email: info@quectel.com

Or our local offices. For more information, please visit:
[http://www.quectel.com/support/sales.htm.](http://www.quectel.com/support/sales.htm.)

For technical support, or to report documentation errors, please visit:
[http://www.quectel.com/support/technical.htm.](http://www.quectel.com/support/technical.htm.)
Or email us at: support@quectel.com.

Legal Notices

We offer information as a service to you. The provided information is based on your requirements and we
make every effort to ensure its quality. You agree that you are responsible for using independent analysis
and evaluation in designing intended products, and we provide reference designs for illustrative purposes
only. Before using any hardware, software or service guided by this document, please read this notice
carefully. Even though we employ commercially reasonable efforts to provide the best possible
experience, you hereby acknowledge and agree that this document and related services hereunder are
provided to you on an “as available” basis. We may revise or restate this document from time to time at
our sole discretion without any prior notice to you.

Use and Disclosure Restrictions

### License Agreements

Documents and information provided by us shall be kept confidential, unless specific permission is
granted. They shall not be accessed or used for any purpose except as expressly provided herein.

### Copyright

Our and third-party products hereunder may contain copyrighted material. Such copyrighted material shall
not be copied, reproduced, distributed, merged, published, translated, or modified without prior written
consent. We and the third party have exclusive rights over copyrighted material. No license shall be
granted or conveyed under any patents, copyrights, trademarks, or service mark rights. To avoid
ambiguities, purchasing in any form cannot be deemed as granting a license other than the normal
non-exclusive, royalty-free license to use the material. We reserve the right to take legal action for
noncompliance with abovementioned requirements, unauthorized use, or other illegal or malicious use of
the material.


### Trademarks

Except as otherwise set forth herein, nothing in this document shall be construed as conferring any rights
to use any trademark, trade name or name, abbreviation, or counterfeit product thereof owned by Quectel
or any third party in advertising, publicity, or other aspects.

### Third-Party Rights

This document may refer to hardware, software and/or documentation owned by one or more third parties
(“third-party materials”). Use of such third-party materials shall be governed by all restrictions and
obligations applicable thereto.

We make no warranty or representation, either express or implied, regarding the third-party materials,
including but not limited to any implied or statutory, warranties of merchantability or fitness for a particular
purpose, quiet enjoyment, system integration, information accuracy, and non-infringement of any
third-party intellectual property rights with regard to the licensed technology or use thereof. Nothing herein
constitutes a representation or warranty by us to either develop, enhance, modify, distribute, market, sell,
offer for sale, or otherwise maintain production of any our products or any other hardware, software,
device, tool, information, or product. We moreover disclaim any and all warranties arising from the course
of dealing or usage of trade.

Privacy Policy

To implement module functionality, certain device data are uploaded to Quectel’s or third-party’s servers,
including carriers, chipset suppliers or customer-designated servers. Quectel, strictly abiding by the
relevant laws and regulations, shall retain, use, disclose or otherwise process relevant data for the
purpose of performing the service only or as permitted by applicable laws. Before data interaction with
third parties, please be informed of their privacy and data security policy.

Disclaimer

a) We acknowledge no liability for any injury or damage arising from the reliance upon the information.
b) We shall bear no liability resulting from any inaccuracies or omissions, or from the use of the
information contained herein.
c) While we have made every effort to ensure that the functions and features under development are
free from errors, it is possible that they could contain errors, inaccuracies, and omissions. Unless
otherwise provided by valid agreement, we make no warranties of any kind, either implied or express,
and exclude all liability for any loss or damage suffered in connection with the use of features and
functions under development, to the maximum extent permitted by law, regardless of whether such
loss or damage may have been foreseeable.
d) We are not responsible for the accessibility, safety, accuracy, availability, legality, or completeness of
information, advertising, commercial offers, products, services, and materials on third-party websites
and third-party resources.

Copyright © Quectel Wireless Solutions Co., Ltd. 2024. All rights reserved.


## About the Document

Revision History

```
Version Date Author Description
```
- 2020 - 01 - 12 Jacobi RAO Creation of the document

```
1 .0 2021 - 01 - 27 Jacobi RAO First official release
```
```
1 .1 2021 - 11 - 05 Jacobi RAO
```
1. Updated the following commands:
    AT+QENG (Chapter 4.8);
    AT+CGDCONT (Chapter 5.4);
    AT+QBAND (Chapter 7.5);
    AT+QCFG="statisr" (Chapter 11.1.7).
2. Added the following commands:
    AT+QESMC (Chapter 4.9);
    AT+QEMMS (Chapter 4.10);
    AT+QOOSAIND (Chapter 4.11);
    AT+CGAUTH (Chapter 5.3);
    AT+CIPCA (Chapter 5. 5 );
    AT+CRTDCP (Chapter 7.3);
    AT+CSODCP (Chapter 7.4);
    AT+QLAPI (Chapter 7.9);
    AT+QLEDMOD (Chapter 7.10);
    AT+QIPERF (Chapter 7.11);
    AT+QSIMSLEEP (Chapter 8.13);
    AT+QDRX (Chapter 9.5);
    AT+QPSMS (Chapter 9.9);
    AT+QPSC (Chapter 9.11);
    AT+QCFG="NcellMeas" (Chapter 11.1.14);
    AT+QCFG="SimBip" (Chapter 11.1.15).
3. Added the URC +RECVNONIP (Chapter 7.12).
4. Added MQTT related commands (Chapter 13.2).
5. Updated error codes (Chapter 14).


##### 1 .2 2023 - 04 - 25

```
Yance YANG/
Randy LI Added^ the^ applicable module BC950K-GL.^
```
##### 1 .3 2023 - 08 - 09

```
Theo QIN/
Lewis LIU
```
1. Added the following commands:
    AT+QEMMTIMER (Chapter 4.12);
    AT+QNBPARA (Chapter 7.8);
    AT+QRHPLMNS (Chapter 7.10);
    AT+QCFG="activetimer" (Chapter 11.1.16);
    AT+QCFG="simpsm" (Chapter 11.1.17).
2. Updated the following commands:
    AT+QENG (Chapter 4.8);
    AT+CFUN (Chapter 0 );
    AT+QCFG (Chapter 11.1);
    AT+QCFG="NBcategory" (Chapter 11.1.10).
3. Deleted AT+QPSC.
4. Added SMS related commands (Chapter 13 ).
5. Added the CMS ERROR: <err> (Table 6).

1 .4 20 24-01-2 6 Lewis LIU

1. Added the description of AT+QCFG (Chapter 6.3).
2. Added AT+QBANDSCAN (Chapter 7.14).
3. Updated the values of <mode> in AT+QDRX
    (Chapter 9.5).
4. Updated the response to test command in
    AT+QPSMS (Chapter 9.9).
5. Updated the values of <value> in
    AT+QCFG="OOSScheme" (Chapter 11.1.3).


## Contents

## Contents




## Table Index

- About the Document
- Contents
- Table Index
- 1 Introduction
   - 1.1. Definitions
   - 1.2. AT Command Syntax
   - 1.3. AT Command Responses
   - 1.4. Description of Data Mode
   - 1.5. Declaration of AT Command Examples
- 2 Product Information Query Commands
   - 2.1. ATI Display Product Identification Information
   - 2.2. AT+CGMI Request Manufacturer Identification
   - 2.3. AT+CGMM Request Model Identification
   - 2.4. AT+CGMR Request Manufacturer Revision
   - 2.5. AT+CGSN Request Product Serial Number
- 3 UART Function Commands
   - 3.1. ATE Set Command Echo Mode
   - 3.2. AT+IPR Set TE-TA Local Rate
- 4 Network Status Related Commands
   - 4.1. AT+CEREG EPS Network Registration Status
   - 4.2. AT+CESQ Extended Signal Quality
   - 4.3. AT+CGATT PS Attach or Detach
   - 4.4. AT+CGPADDR Show PDP Addresses
   - 4.5. AT+CREG Network Registration
   - 4.6. AT+CSCON Signaling Connection Status
   - 4.7. AT+CSQ Signal Quality Report
   - 4.8. AT+QENG Engineering Mode
   - 4.9. AT+QESMC Query Cause to the Rejection of a Session Request
   - 4.10. AT+QEMMS Query EMM State of UE
   - 4.11. AT+QOOSAIND Enable or Disable OOSA URC
   - 4.12. AT+QEMMTIMER Gets EMM Timer Status
- 5 PDN and APN Commands
   - 5.1. AT+CGACT PDP Context Activate/Deactivate
   - 5.2. AT+CGAPNRC APN Rate Control
   - 5.3. AT+CGAUTH Define PDP Context Authentication Parameters
   - 5.4. AT+CGDCONT Define PDP Context
   - 5.5. AT+CIPCA Initial PDP Context Activation
   - 5.6. AT+QCGDEFCONT Set Default PSD Connection Settings
- 6 3GPP R14 Protocol Commands
   - 6.1. AT+CNMPSD Trigger R14 RAI
   - 6.2. AT+QR14FEATURE Query Status of R14 Features
   - 6.3. AT+QCFG Configure System
- 7 Other Network Commands................................................................................................................
   - 7.1. AT+CCIOTOPT CloT Optimization Configuration
   - 7.2. AT+COPS Operator Selection
   - 7.3. AT+CRTDCP Reporting of Terminating Data via the Control Plane
   - 7.4. AT+CSODCP Sending of Originating Data via Control Plane
   - 7.5. AT+QBAND Get and Set Mobile Operation Band
   - 7.6. AT+QCSEARFCN Clear Stored NB-IoT EARFCN List
   - 7.7. AT+QLOCKF Lock NB-IoT Frequency and PCI
   - 7.8. AT+QNBPARA Query Timing Advance Value
   - 7.9. AT+QPLMNS Search PLMN
   - 7.10. AT+QRHPLMNS Enable or Disable HPLMN and Higher Priority PLMN Searching
   - 7.11. AT+QLAPI Enable or Disable the NAS Low Access Priority Indicator
   - 7.12. AT+QLEDMODE Set NETLIGHT Mode................................................................................
   - 7.13. AT+QIPERF Throughput Test
   - 7.14. AT+QBANDSCAN Speed Up First Roaming Search
   - 7.15. +RECVNONIP Incoming Downlink Non-IP Data
- 8 USIM Related Commands
   - 8.1. AT+CCHO Open Logical Channel
   - 8.2. AT+CCHC Close Logical Channel
   - 8.3. AT+CGLA Generic UICC Logical Channel Access
   - 8.4. AT+CIMI Request International Mobile Subscriber Identity
   - 8.5. AT+CLCK Facility Lock
   - 8.6. AT+CPIN Enter PIN
   - 8.7. AT+CPINR Remaining PIN Retries
   - 8.8. AT+CPWD Change Password
   - 8.9. AT+CRSM Restricted USIM Access
   - 8.10. AT+CSIM Generic USIM Access
   - 8.11. AT+QCCID USIM Card Identification
   - 8.12. AT+QSIMPOLL USIM Card Polling.......................................................................................
   - 8.13. AT+QSIMSLEEP USIM Sleep Control
- 9 Power Consumption Commands
   - 9.1. AT+CEDRXS eDRX Setting
   - 9.2. AT+CEDRXRDP eDRX Read Dynamic Parameters
   - 9.3. AT+CFUN Set UE Functionality
   - 9.4. AT+CPSMS Power Saving Mode Setting
   - 9.5. AT+QDRX Query DRX Status
   - 9.6. AT+QEDRXCFG Configure eDRX and PTW
   - 9.7. AT+QNBIOTRAI NB-IoT Release Assistance Indication
   - 9.8. AT+QNBIOTEVENT Enable/Disable NB-IoT Related Event Report
   - 9.9. AT+QPSMS Power Saving Mode Setting
   - 9.10. AT+QSCLK Configure Sleep Mode
- 10 Platform Related Commands
   - 10.1. AT+CBC Query Power Supply Voltage
   - 10.2. AT+CMEE Report Mobile Termination Error
   - 10.3. AT+QADC Query the Input Voltage of Dedicated ADC Channel
   - 10.4. AT+QRST Module Reset
   - 10.5. AT+QRFSTAT Query RF Status
- 11 General Configuration Commands
   - 11.1. AT+QCFG System Configuration
      - 11.1.1. AT+QCFG="EPCO" Enable/Disable EPCO
      - 11.1.2. AT+QCFG="DataInactTimer" Configure Inactivity Timer
      - 11.1.3. AT+QCFG="OOSScheme" Configure Network Searching Mechanism in OOS
      - 11.1.4. AT+QCFG="logbaudrate" Configure Baud Rate.......................................................
      - 11.1.5. AT+QCFG="slplocktimes" Configure Countdown to Entering Sleep Mode
      - 11.1.6. AT+QCFG="dsevent" Control the Reporting of URC Indicating Deep Sleep
      - 11.1.7. AT+QCFG="statisr" Configure Report Interval of Statistics URC
      - 11.1.8. AT+QCFG="MacRAI" Enable/Disable RAI in MAC Layer
      - 11.1.9. AT+QCFG="relversion" Configure Protocol Release Version
      - 11.1.10. AT+QCFG="NBcategory" Configure UE Category
      - 11.1.11. AT+QCFG="wakeupRXD" Enable/Disable RXD to Wake Up UE
      - 11.1.12. AT+QCFG="faultaction" Configure UE Reaction to System Crash
      - 11.1.13. AT+QCFG="GPIO" Configure GPIO Status
      - 11.1.14. AT+QCFG="NcellMeas" Enable or Disable Neighbor Cell Measurement
      - 11.1.15. AT+QCFG="SimBip" Enable or Disable SIMBIP
      - 11.1.16. AT+QCFG="activetimer" Configure Active Timer Value............................................
      - 11.1.17. AT+QCFG="simpsm" Configure USIM Power Saving Mode
- 12 Time Related Commands
   - 12.1. AT+CCLK Set and Get Current Date and Time
   - 12.2. AT+CTZR Time Zone Reporting
- 13 SMS-Related Commands
   - 13.1. AT+CMGF Configure Message Format
   - 13.2. AT+CSCA Update SMSC Address
   - 13.3. AT+CMGS Send Message
   - 13.4. +CMT Receive New Message
- 14 Other Commands
   - 14.1. TCP/IP Related Commands
   - 14.2. MQTT Related Commands
   - 14.3. DFOTA Related Commands
- 15 Summary of Error Codes
- 16 Appendix References
- Table 1: Types of AT Commands Table Index
- Table 2 : List of TCP/IP Related AT Commands
- Table 3 : List of MQTT Related AT Commands
- Table 4 : List of DFOTA Related AT Commands
- Table 5 : CME ERROR: <err>
- Table 6 : CMS ERROR: <err>
- Table 7: Related Documents
- Table 8 : Terms and Abbreviations


## 1 Introduction

This document gives details of the AT Commands set supported by the Quectel NB-IoT modules
BC660K-GL and BC950K-GL.

### 1.1. Definitions

⚫ <CR> Carriage return character.
⚫ <LF> Line feed character.
⚫ <...> Parameter name. Angle brackets do not appear on the command line.
⚫ [...] Optional parameter of a command or an optional part of TA information response.
Square brackets do not appear on the command line. When an optional parameter is
not given in a command, the new value equals its previous value or the default settings,
unless otherwise specified.
⚫ Underline Default setting of a parameter.

### 1.2. AT Command Syntax

All command lines must start with AT or at and end with <CR>. Information responses and result codes
always start and end with a carriage return character and a line feed character:
<CR><LF><response><CR><LF>. In tables presenting commands and responses throughout this
document, only the commands and responses are presented, and <CR> and <LF> are deliberately
omitted.

AT commands implemented by BC660K-GL and BC950K-GL fall into two categories syntactically: Basic
and Extended. They are listed as follows:

⚫ Basic

Basic command format is AT<x><n>, or AT&<x><n>, where <x> is the command, and <n> is/are the
argument(s) of the command. For example, ATE<n> tells the DCE (Data Circuit-terminating Equipment)
whether received characters should be echoed back to the DTE (Data Terminal Equipment) according to
the value of <n>. <n> is optional and a default will be used if it is omitted.


⚫ Extended

These AT commands have four types as explained in the following table:

Table 1 : Types of AT Commands

Multiple commands can be placed on a single line using a semi-colon (;) between commands. In such
cases, only the first command should have AT prefix. Commands can be in upper or lower case.

Spaces should be ignored when you enter AT commands, except in the following cases:

⚫ Within quoted strings, where spaces are preserved;
⚫ Within an unquoted string or numeric parameter;
⚫ Within an IP address;
⚫ Within the AT command name up to and including a =,? or =?.

On input, at least a carriage return is required. A newline character is ignored so it is permissible to use
carriage return/line feed pairs on the input.

If no command is entered after the AT token, OK will be returned. If an invalid command is entered,
ERROR will be returned.

Optional parameters, unless explicitly stated, need to be provided up to the last parameter being entered.

Every AT command must be inputted separately. Execute a new AT command only when the previous one
is finished.

Command Type Syntax Description

Test Command AT+<cmd>=?

```
Test the existence of the corresponding
command and return information about the
type, value, or range of its parameter.
```
Read Command AT+<cmd>?
Check the current parameter value of a
corresponding Command.

Write Command AT+<cmd>=<p1>[,<p2>[,<p3>[...]]] Set user-definable parameter value.

Execution Command AT+<cmd>
Return a specific information parameter or
perform a specific action.

##### NOTE


### 1.3. AT Command Responses

When the AT command processor has finished processing a line, it will output OK, ERROR or +CME
ERROR: <err> to indicate that it is ready to receive a new command. Solicited informational responses
are displayed before the final OK, ERROR or +CME ERROR: <err>.

Responses will be in the format of:

<CR><LF>+CMD1:<parameters><CR><LF>
<CR><LF>OK<CR><LF>

Or

<CR><LF><parameters><CR><LF>
<CR><LF>OK<CR><LF>

### 1.4. Description of Data Mode

BC660K-GL and BC950K-GL support two working modes of the COM port: AT command mode and data
mode. In the AT command mode, the data inputted via a COM port is treated as AT commands; while in
the data mode, it is treated as data.

In the AT command mode (the default mode), the BC660K-GL and BC950K-GL modules enter the data
mode in 500 ms after the > response, after which if “Ctrl" + “Z" is entered, the module will exit data mode
and send the data to a COM port; if “Esc" is entered, the module will exit data mode and cancel the
sending.

1. After the > response, it is recommended for the MCU to wait for 500 ms before sending the data.
2. In the data mode, URCs will be lost. To avoid this, please enter the data to be sent immediately
    500 ms after the > response and then exit the data mode as soon as possible.

##### NOTE


### 1.5. Declaration of AT Command Examples

The AT command examples in this document are provided to help you learn about the use of the AT
commands introduced herein. The examples, however, should not be taken as Quectel’s
recommendations or suggestions about how to design a program flow or what status to set the module
into. Sometimes multiple examples may be provided for one AT command. However, this does not mean
that there is a correlation among these examples, or that they should be executed in a given sequence.


## 2 Product Information Query Commands

### 2.1. ATI Display Product Identification Information

This Execution Command returns product identification information including the identifier of device type
and the revision of software.

#### Parameter

#### Example

##### ATI

Quectel_Ltd
Quectel_BC660K-GL
Revision: BC660KGLAAR01A

OK

#### ATI Display Product Identification Information

```
Execution Command
ATI
```
```
Response
Quectel_Ltd
<objectID>
Revision: <revision>
```
```
OK
Maximum Response Time 5 s
Characteristics /
```
```
<objectID> String type. Identifier of device type.
<revision> String type. Revision of software release.
```

### 2.2. AT+CGMI Request Manufacturer Identification

This Execution Command returns manufacturer information.

#### Parameter

#### Example

##### AT+CGMI

Quectel_Ltd
Quectel_BC660K-GL
Revision: QCX

OK

### 2.3. AT+CGMM Request Model Identification

This Execution Command returns the model information of the product.

#### AT+CGMI Request Manufacturer Identification

```
Test Command
AT+CGMI=?
```
```
Response
OK
Execution Command
AT+CGMI
```
```
Response
Quectel_Ltd
<objectID>
Revision: QCX
```
```
OK
Maximum Response Time 5 s
Characteristics /
```
<objectID> String type. Identifier of device type.

#### AT+CGMM Request Model Identification

```
Test Command
AT+CGMM=?
```
```
Response
OK
Execution Command
AT+CGMM
```
```
Response
<objectID>
```

#### Parameter

#### Example

##### AT+CGMM

Quectel_BC660K-GL

OK

### 2.4. AT+CGMR Request Manufacturer Revision

This Execution Command returns the manufacturer revision.

#### Parameter

#### Example

##### AT+CGMR

##### OK

```
Maximum Response Time 5 s
Characteristics /
```
<objectID> String type. Identifier of device type.

#### AT+CGMR Request Manufacturer Revision

```
Test Command
AT+CGMR=?
```
```
Response
OK
Execution Command
AT+CGMR
```
```
Response
Revision: <revision>
```
```
OK
Maximum Response Time 5 s
Characteristics /
```
<revision> String type. Manufacturer revision (Revision of software release).


Revision: BC660KGLAAR01A0 3

OK

### 2.5. AT+CGSN Request Product Serial Number

This Execution Command returns the IMEI (International Mobile Equipment Identity) number and related
information. For a TA which does not support <snt>, only OK is returned.

#### AT+CGSN Request Product Serial Number

```
Test Command
AT+CGSN=?
```
```
Response
When TE supports <snt> and the command is executed
successfully:
+CGSN: (range of supported <snt>s)
```
```
OK
Write Command
AT+CGSN=<snt>
```
```
Response
When <snt>=0:
<SN>
```
```
OK
```
```
When <snt>=1:
+CGSN: <IMEI>
```
```
OK
```
```
When <snt>=2:
+CGSN: <IMEISV>
```
```
OK
```
```
When <snt>=3:
+CGSN: <SVN>
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
```

#### Parameter

#### Example

AT+CGSN=1 //Request the IMEI number
+CGSN: 866818039921444

OK

```
Execution Command
AT+CGSN
```
```
Response
<SN>
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
Characteristics /
```
<snt> Integer type. The serial number type requested.
0 Returns <SN>
1 Returns the IMEI number
2 Returns the IMEISV (International Mobile Equipment Identity and Software
Version) number
3 Returns the SVN (Software Version Number)
<SN> String type. One or more lines of information text determined by the MT manufacturer.
<IMEI> String type. The IMEI number in decimal format.
<IMEISV> String type. The IMEISV in decimal format.
<SVN> String type. The current SVN in decimal format, and it is a part of IMEISV.
<err> Error code. See Chapter 15 for details.


## 3 UART Function Commands

### 3.1. ATE Set Command Echo Mode

This Execution Command determines whether or not the UE echoes characters received from external
MCU in the AT command mode.

#### Parameter

#### Example

##### ATE

##### OK

Quectel_Ltd
Quectel_BC660K-GL
Revision: BC660KGLAAR01A

#### ATE Set Command Echo Mode

```
Execution Command
ATE<value>
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect immediately.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM automatically.
```
<value> Integer type. Whether to echo commands.
0 OFF
1 ON
<err> Error code. See Chapter 15 for details.


##### OK

##### ATE

##### OK

##### ATI

Quectel_Ltd
Quectel_BC660K-GL
Revision: BC660KGLAAR01A

OK

### 3.2. AT+IPR Set TE-TA Local Rate

This command sets the TE-TA local rate.

#### Parameter

#### AT+IPR Set TE-TA Local Rate

```
Test Command
AT+IPR=?
```
```
Response
+IPR: (list of supported <rate>s)
```
```
OK
Read Command
AT+IPR?
```
```
Response
+IPR: <rate>
```
```
OK
Write Command
AT+IPR=<rate>
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect immediately.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM automatically.
```
```
<rate> Integer type. Baud rate per second. Unit: bps.
2400
4800
```

#### Example

AT+IPR=115200 //Set the baud rate to 115200 bps.
OK
AT+IPR? //Query the current configuration.
+IPR: 115200

OK
AT+IPR=? //Query the baud rates supported.
+IPR: (2400,4800,9600,19200,38400,57600,115200,230400,460800)

OK

##### 9600

##### 19200

##### 38400

##### 57600

##### 115200

##### 230400

##### 460800

```
<err> Error code. See Chapter 15 for details.
```

## 4 Network Status Related Commands

### 4.1. AT+CEREG EPS Network Registration Status

This Write Command configures the presentation of unsolicited result codes for EPS Network Registration
Status.

⚫ When <n>=1 and there is a change in the MT's EPS network registration status in E-UTRAN, an
unsolicited result code (URC) +CEREG: <stat> is presented.
⚫ When <n>=2 and there is a change of the network cell in E-UTRAN, URC +CEREG: <stat>[,
[<tac>],[<ci>],[<AcT>]] is presented. <AcT>, <tac> and <ci> are provided only if available.
⚫ When the value of <stat> changes, <n>=3 further extends +CEREG: <stat>[,[<tac>],[<ci>],[<AcT>]]
with [,<cause_type>,<reject_cause>] if available.

If the UE applies for entering PSM to reduce power consumption, the Write Command controls the
presentation of the following URC:
+CEREG: <stat>[,[<tac>],[<ci>],[<AcT>][,[<cause_type>],[<reject_cause>][,[<Active-Time>],[<Peri
odic-TAU>]]]].

⚫ When <n>=4, the URC provides the UE with additional information including the active time value
<Active-Time> and the periodic TAU value <Periodic-TAU> if there is a change to the network cell
in E-UTRAN.
⚫ <n>=5 further enhances the URC with <cause_type> and <reject_cause> when the value of <stat>
changes. The parameters <tac>, <ci>, <AcT>, <cause_type>, <reject_cause>, <Active-Time>
and <Periodic-TAU> are provided only if available.

This Read Command returns the status of result code presentation and an integer <stat> which shows
whether the network has currently indicated the registration of the MT. Location information elements
<tac>, <ci> and <AcT>, if available, are returned only when <n>=2 and MT is registered in the network.
The parameters [,<cause_type>,<reject_cause>], if available, are returned when <n>=3.

This Test Command returns supported parameter values.

#### AT+CEREG EPS Network Registration Status

```
Test Command
AT+CEREG=?
```
```
Response
+CEREG: (range of supported <n>s)
```

#### Parameter

##### OK

```
Read Command
AT+CEREG?
```
```
Response
When <n>=0, 1, 2 or 3 and the command is executed
successfully:
+CEREG: <n>,<stat>[,[<tac>],[<ci>],[<AcT>[,<cause_typ
e>,<reject_cause>]]]
```
```
When<n>=4 or 5 and the command is executed successfully:
+CEREG: <n>,<stat>[,[<tac>],[<ci>],[<AcT>][,[<cause_ty
pe>],[<reject_cause>][,[<Active-Time>],[<Periodic-TA
U>]]]]
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Write Command
AT+CEREG=<n>
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect immediately.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM automatically.
```
<n> Integer type. Disable or enable network registration URC.
0 Disable network registration URC
1 Enable network registration URC: +CEREG: <stat>
2 Enable network registration and location information URC:
+CEREG: <stat>[,[<tac>],[<ci>],[<AcT>]]
3 Enable network registration, location information and EMM cause value information
URC:
+CEREG: <stat>[,[<tac>],[<ci>],[<AcT>][,<cause_type>,<reject_cause>]]
4 For a UE that requests PSM, enable network registration and location information
URC:


+CEREG: <stat>[,[<tac>],[<ci>],[<AcT>][,,[,[<Active-Time>],[<Periodic-TAU>]]]]
5 For a UE that requests PSM, enable network registration, location information and
EMM cause value information URC:
+CEREG: <stat>[,[<tac>],[<ci>],[<AcT>][,[<cause_type>],[<reject_cause>][,[<Act
ive-Time>],[<Periodic-TAU>]]]]
<stat> Integer type. EPS registration status.
0 Not registered, MT is not currently searching an operator to register to
1 Registered, home network
2 Not registered, but MT is currently trying to attach or searching an operator to register
to
3 Registration denied
4 Unknown (e.g. out of E-UTRAN coverage)
5 Registered, roaming
<tac> String type. Two-byte tracking area code in hexadecimal format (e.g., 00C3 equals 195 in
decimal).
<ci> String type. Four-byte E-UTRAN cell ID in hexadecimal format.
<AcT> Integer type. Access technology of the serving cell.
7 E-UTRAN
9 E-UTRAN (NB-S1 mode)
<cause_type> Integer type. Type of <reject_cause>.
0 <reject_cause> contains an EMM cause value (see 3GPP TS 24.008 Annex G).
1 <reject_cause> contains a manufacturer-specific cause value.
<reject_cause> Integer type. Contains the cause of the registration failure. The value is of type as
defined by <cause_type>.
<Active-Time> String type. One byte in an 8-bit format. Active time value (T3324) allocated to the UE
in E-UTRAN. The active time value is coded as one byte (octet 3) of the GPRS Timer
2 information element coded as bit format (e.g. "00100100" equals 4 minutes). For the
coding and the value range, see the GPRS Timer 2 IE in 3GPP TS 24.008 Table
10.5.163/3Gpp TS 24.008, 3GPP TS 23.682 and 3GPP TS 23.401.
Bits 5 to 1 represents the binary coded timer value.
Bits 8 to 6 defines the timer value unit for the GPRS timer as follows:
Bits
8 7 6
0 0 0 value is incremented in multiples of 2 seconds
0 0 1 value is incremented in multiples of 1 minute
0 1 0 value is incremented in multiples of 6 minutes
1 1 1 value indicates that the timer is deactivated
<Periodic-TAU> String type. One byte in an 8-bit format. Indicates the extended periodic TAU value
(T3412) allocated to the UE in E-UTRAN. The extended periodic TAU value is coded
as one byte (octet 3) of the GPRS Timer 3 information element coded as bit format
(e.g. "01000111" equals 70 hours). For the coding and the value range, see GPRS
Timers 3 IE in 3GPP TS 24.008 Table 10.5.163a/3GPP TS 24.008, 3GPP TS 23.682
and 3GPP TS 23.401.
Bits 5 to 1 represents the binary coded timer value.


#### Example

##### AT+CEREG=1

##### OK

##### AT+CEREG?

##### +CEREG: 1,1

##### OK

##### AT+CEREG=?

##### +CEREG: (0-5)

##### OK

### 4.2. AT+CESQ Extended Signal Quality

This Execution Command makes the module returns a numeral from 0 to 99 to indicate the strength of the
signal it has just received, and the larger the number is, the better the quality of the signal.

This Test Command returns supported values as compound values.

Bits 8 to 6 defines the timer value increment as follows:
Bits
8 7 6
0 0 0 value is incremented in multiples of 10 minutes
0 0 1 value is incremented in multiples of 1 hour
0 1 0 value is incremented in multiples of 10 hours
0 1 1 value is incremented in multiples of 2 seconds
1 0 0 value is incremented in multiples of 30 seconds
1 0 1 value is incremented in multiples of 1 minute
1 1 0 value is incremented in multiples of 320 hours
1 1 1 value indicates that the timer is deactivated
<err> Error code. See Chapter 15 for details.

#### AT+CESQ Extended Signal Quality

```
Test Command
AT+CESQ=?
```
```
Response
+CESQ: (list of supported <rxlev>s),(list of supported
<ber>s),(list of supported <rscp>s),(list of supported
<ecno>s),(list of supported <rsrq>s),(list of supported
<rsrp>s)
```
```
OK
```

#### Parameter

```
Execution Command
AT+CESQ
```
```
Response
+CESQ: <rxlev>,<ber>,<rscp>,<ecno>,<rsrq>,<rsrp>
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
Characteristics /
```
<rxlev> Integer type. Received signal strength level.
0 <rssi> < -110 dBm
1 - 110 dBm ≤ <rssi> < -109 dBm
2 - 109 dBm ≤ <rssi> < -108 dBm
...
61 - 50 dBm ≤ <rssi> < -49 dBm
62 - 49 dBm ≤ <rssi> < -48 dBm
63 - 48 dBm ≤ <rssi>
99 Not known or not detectable
<ber> Integer type. Channel bit error rate (in percent).
0 – 7 RxQual values RXQUAL_0–RXQUAL_7 as defined in 3GPP TS 45.008
99 Not known or not detectable
<rscp> Integer type. Received signal code power (See 3GPP 25.133 and 3GPP 25.123).
0 <rscp> < -120 dBm
1 - 120 dBm ≤ <rscp> < -119 dBm
2 - 119 dBm ≤ <rscp> < -118 dBm
...
94 - 27 dBm ≤ <rscp> < -26 dBm
95 - 26 dBm ≤ <rscp> < -25 dBm
96 - 25 dBm ≤ <rscp>
255 Not known or not detectable
<ecno> Integer type. Ratio of the received energy per PN chip to the total received power spectral
density (Ec/No) (See 3GPP 25.133).
0 <ecno> < -24 dBm
1 - 24 dBm ≤ <ecno> < -23.5 dBm
2 - 23.5 dBm ≤ <ecno> < -23 dBm
...
47 - 1 dBm ≤ <ecno> < -0.5 dBm


1. For details of <rssi>, see AT+CSQ.
2. <rxlev> and <ber> are not applicable to NB-IoT network and should be set to "not known or not
    detectable" ( 99 ) for the module.
3. <rscp> and <ecno> are not applicable to NB-IoT network and should be set to "not known or not
    detectable" (255) for the module.

#### Example

##### AT+CESQ

##### +CESQ: 99,99,255,255,25,61

##### OK

48 - 0.5 dBm ≤ <ecno> < 0 dBm
49 0 dBm ≤ <ecno>
255 Not known or not detectable
<rsrq> Integer type. Reference signal received quality (RSRQ, see 3GPP 36.133). When sending
data is needed, RSRQ is recommended to be greater than -10 dB.
0 <rsrq> < -19.5 dB
1 - 19.5 dB ≤ <rsrq> < -19 dB
2 - 19 dB ≤ <rsrq> < -18.5 dB
...
32 - 4 dB ≤ <rsrq> < -3.5 dB
33 - 3.5 dB ≤ <rsrq> < -3 dB
34 - 3 dB ≤ <rsrq>
255 Not known or not detectable
<rsrp> Integer type. Reference signal received power (RSRP, see 3GPP 36.133). When sending
data is needed, RSRP is recommended to be greater than -115 dbm.
0 <rsrp> < - 140 dBm
1 - 140 dBm ≤ <rsrp> < -139 dBm
2 - 139 dBm ≤ <rsrp> < -138 dBm
...
95 - 46 dBm ≤ <rsrp> < -45 dBm
96 - 45 dBm ≤ <rsrp> < -44 dBm
97 - 44 dBm ≤ <rsrp>
255 Not known or not detectable
<err> Error code. See Chapter 15 for details.

##### NOTE


### 4.3. AT+CGATT PS Attach or Detach

This Write Command attaches the MT to, or detach the MT from, the packet domain service. After the
command has completed, the MT remains in V.250 command state. If the MT is already in the requested
state, the command ignores and the OK response is still returned. If the requested state cannot be
achieved, an ERROR or +CME ERROR response is returned. Refer to Chapter 15 for possible <err>
values. Any active PDP contexts are automatically deactivated when the attachment state changes to
detached.

This Read Command returns the current packet domain service state.

This Test Command requests information on the supported packet domain service states.

#### Parameter

#### AT+CGATT PS Attach or Detach

```
Test Command
AT+CGATT=?
```
```
Response
+CGATT: (list of supported <state>s)
```
```
OK
Read Command
AT+CGATT?
```
```
Response
+CGATT: <state>
```
```
OK
Write Command
AT+CGATT=<state>
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 70 s, determined by network.
Characteristics /
```
<state> Integer type. Indicates the state of PS attachment.
0 Detached
1 Attached
<err> Error code. See Chapter 15 for details.


The initial PDP context with <cid>= 0 is automatically defined at startup.

#### Example

##### AT+CGATT?

##### +CGATT: 1

##### OK

##### AT+CGATT=1

##### OK

##### AT+CGATT=?

##### +CGATT: (0,1)

##### OK

### 4.4. AT+CGPADDR Show PDP Addresses

This command returns the IP address of the device.

This Execution Command returns a list of PDP addresses for the specified context identifiers. If no <cid>
is specified, the addresses for all defined contexts are returned.

This Test Command returns a list of defined <cid>s. These are <cid>s that have been activated and may
or may not have an IP address associated with them.

#### AT+CGPADDR Show PDP Addresses

```
Test Command
AT+CGPADDR=?
```
```
Response
[+CGPADDR: (list of defined <cid>s)]
```
```
OK
Read Command
AT+CGPADDR?
```
```
Response
[+CGPADDR: <cid>[,<PDP_addr_1>[,<PDP_addr_2>]]]
[+CGPADDR: <cid>[,<PDP_addr_1>[,<PDP_addr_2>]]]
[...]
```
```
OK
Write Command
AT+CGPADDR=<cid>
```
```
Response
+CGPADDR: <cid>[,<PDP_addr_1>[,<PDP_addr_2>]]
```
##### NOTE


#### Parameter

1. In dual-stack terminals (<PDP_type>="IPV4V6"), the IPv6 address is provided in <PDP_addr_
    2>.
2. For terminals with a single IPv6 stack (<PDP_type>="IPV6") or due to backwards compatibility, the
    IPv6 address can be provided in <PDP_addr_1>.

#### Example

##### AT+CGPADDR= 0

##### +CGPADDR: 0,"100.68.114.220"

##### OK

```
Execution Command
AT+CGPADDR
```
```
Response
[+CGPADDR: <cid>[,<PDP_addr_1>[,<PDP_addr_2>]]]
[+CGPADDR: <cid>[,<PDP_addr_1>[,<PDP_addr_2>]]]
[...]
```
```
OK
Maximum Response Time 5 s
Characteristics /
```
<cid> Integer type. A numeric parameter which specifies a particular PDP context definition
(see AT+CGDCONT). If no <cid> is specified, the addresses for all defined
contexts are returned.
<PDP_addr_1> and <PDP_addr_2>
String type. Identify the MT in the address space applicable to the PDP. The
address may be static or dynamic.
For a static address, it will be the one set by AT+CGDCONT when the
context was defined.
For a dynamic address it will be the one assigned during the last PDP context
activation that used the context definition referred to by <cid>. <PDP_address> is
omitted if none is available.
Both <PDP_addr_1> and <PDP_addr_2> are included when both IPv4 and IPv6
addresses are assigned, with <PDP_addr_1> containing the IPv4 address and
<PDP_addr_2> containing the IPv6 address. <PDP_addr_1> is preferred for
containing address information when there is only one address.
The string is given as a dot-separated numeric (0–255) parameter in this form:
a1.a2.a3.a4 for IPv4 and a1:a2:a3:a4:a5:a6:a7:a8 for IPv6.

##### NOTE


##### OK

##### AT+CGPADDR=?

##### +CGPADDR: ( 0 )

##### OK

### 4.5. AT+CREG Network Registration

This Write Command controls the presentation of an unsolicited result code +CREG: <stat>

⚫ When <n>=1 and there is a change in the circuit mode network registration status of the MT
in GERAN/UTRAN/E-UTRAN, or unsolicited result code +CREG: <stat>[,[<lac>],[<ci>],[<Ac
T>]]
⚫ When <n>=2 and there is a change of the network cell in GERAN/UTRAN/E-UTRAN. The
parameters <AcT>, <lac> and <ci> are sent only if available.
⚫ When the value of <stat> changes, the value <n>=3 further extends the unsolicited result code with
[,<cause_type>,<reject_cause>], when available.

This Read Command returns the status of result code presentation and an integer <stat> which shows
whether the network has currently indicated the registration of the MT. Location information elements
<lac>, <ci> and <AcT>, if available, are returned only when <n>=2 and MT is registered in the network.
The parameters [,<cause_type>,<reject_cause>], if available, are returned when <n>=3.

This Test Command returns values supported as a compound value.

#### AT+CREG Network Registration

```
Test Command
AT+CREG=?
```
```
Response
+CREG: (list of supported <n>s)
```
```
OK
Read Command
AT+CREG?
```
```
Response
+CREG: <n>,<stat>[,[<lac>],[<ci>],[<AcT>][,<cause_typ
e>,<reject_cause>]]
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
```

#### Parameter

```
Write Command
AT+CREG=<n>
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect immediately.
Remain valid after deep-sleep wakeup.
The configurations are saved to NVRAM automatically.
```
<n> Integer type.
0 Disable network registration unsolicited result code.
1 Enable network registration unsolicited result code +CREG: <stat>
2 Enbale network registration and location information unsolicited result code
+CREG: <stat>[,[<lac>],[<ci>],[<AcT>]]
3 Enable network registration, location information and cause value information
unsolicited result code +CREG: <stat>[,[<lac>],[<ci>],[<AcT>][,<cause_typ
e>,<reject_cause>]]
<stat> Integer type.
0 Not registered, MT is not currently searching a new operator to register to
1 Registered, home network
2 Not registered, but MT is searching a new operator to register to
3 Registration denied
4 Unknown. (for example, out GERAN/UTRAN/E-UTRAN coverage)
5 Registered, roaming
6 Registered for “SMS only", home network (applicable only when <AcT> indicates
E-UTRAN)
7 Registered for “SMS only", roaming (applicable only when <AcT> indicates
E-UTRAN)
<lac> String type. Location area code in hexadecimal format, two bytes.( e.g."00C3" equals
195 in decimal).
<ci> String type. Four-byte E-UTRAN Cell ID in hexadecimal format.
<AcT> Integer type. Access technology of the serving cell.
9 E-UTRAN (NB-S1 mode)
<cause_type> Integer type. Indicates the type of <reject_cause>.
0 <reject_cause> contains an EMM cause value (see 3GPP TS 24.008 Annex G)
1 <reject_cause> packet contains a manufacturer specific cause.
<reject_cause> Integer type. Contains the cause of the failed registration. The value is of type as
defined by <cause_type>. (See 3 GPP TS 24.301)


#### Example

##### AT+CREG?

##### +CREG: 0 , 6

##### OK

### 4.6. AT+CSCON Signaling Connection Status

This command gives details of the TA’s perceived radio connection status (i.e. with a base station). It
returns an indication of the current state. Please note that this state is only updated when radio events,
such as sending and receiving, take place. This means that the current state may be out of date. The
terminal may think it is "Connected" yet cannot currently use the base station due to a change in the link
quality.

This Write Command controls the presentation of an URC. If <n>=1, +CSCON: <mode> is sent from the
MT when the connection mode of the MT is changed. When the MT is in E-UTRAN, the mode of the MT
refers to idle when no PS signaling connection and to connected mode when a PS signaling connection
between MT and network is setup. The <state> value indicates the state of the MT when the MT is in
E-UTRAN.

This Read Command returns the status of result code presentation and an integer <mode> which shows
whether the MT is currently in idle mode or connected mode.

This Test Command returns supported values as a compound value.

<err> Error code. See Chapter 15 for details.

#### AT+CSCON Signaling Connection Status

```
Test Command
AT+CSCON=?
```
```
Response
+CSCON: (list of supported <n>s)
```
```
OK
Read Command
AT+CSCON?
```
```
Response
+CSCON: <n>,<mode>
```
```
OK
```
```
If there is any error:
ERROR
Or
```

#### Parameter

#### Example

##### AT+CSCON=0

##### OK

##### AT+CSCON?

##### +CSCON: 0, 0

##### OK

##### AT+CSCON=?

##### +CSCON: (0,1)

##### OK

### 4.7. AT+CSQ Signal Quality Report

This Execution Command returns the received signal strength level <rssi> and the channel bit error rate
<ber> from the MT.

```
+CME ERROR: <err>
Write Command
AT+CSCON=<n>
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect immediately.
Remain valid after deep-sleep wakeup.
The configurations are saved to NVRAM automatically.
```
<n> Integer type. Enable/disable the URC.
0 Disable the URC
1 Enable URC +CSCON: <mode>
<mode> Integer type. Signaling connection status.
0 Idle
1 Connected
<err> Error code. See Chapter 15 for details.


This Test Command returns supported values as a compound value.

#### Parameter

#### Example

##### AT+CSQ

##### +CSQ: 22,0

##### OK

#### AT+CSQ Signal Quality Report

```
Test Command
AT+CSQ=?
```
```
Response
+CSQ: (list of supported <rssi>s),(list of supported <ber>s)
```
```
OK
Execution Command
AT+CSQ
```
```
Response
+CSQ: <rssi>,<ber>
```
```
OK
```
```
If there is any error:
ERROR
or
+CME ERROR: <err>
Maximum Response Time 5 s
Characteristics /
```
<rssi> Integer type. Received signal strength level.
0 - 113 dBm or less
1 - 111 dBm
2 – 30 - 109 to -53 dBm
31 - 51 dBm or greater
99 Not known or not detectable
<ber> Integer type. Channel bit error rate (in percent).
0 – 7 RxQual values RXQUAL_0–RXQUAL_7 as defined in 3GPP TS 45.008
99 Not known or not detectable
<err> Error code. See Chapter 15 for details.


### 4.8. AT+QENG Engineering Mode

This command queries current modem status information of serving cell and current network status in
Engineering Mode.

#### Parameter

#### AT+QENG Engineering Mode

```
Test Command
AT+QENG=?
```
```
Response
+QENG: (range of supported <mode>s)
```
```
OK
Write Command
AT+QENG=<mode>[,<accuracy>]
```
```
Response
When <mode>=0:
+QENG: 0,<sc_EARFCN>,<sc_EARFCN_offset>,<sc_pc
i>,<sc_cellID>,[<sc_RSRP>],[<sc_RSRQ>],[<sc_RSSI>],
[<sc_SINR>],<sc_band>,<sc_TAC>,[<sc_ECL>],[<sc_Tx_
pwr>],<operation_mode>
[+QENG: 1,<nc_EARFCN>,<nc_pci>,<nc_RSRP>,<nc_R
SRQ> [...]]
```
```
OK
```
```
When <mode>=2:
+QENG: 3,<sleep_duration>,<Rx_time>,<Tx_time>
```
```
When <mode>= 3 :
+QENG: 4,<EMM_state>,<EMM_mode>,<PLMN_state>,<
PLMN_type>,<selectPLMN>
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 15 s
Characteristics /
```
<mode> Integer type. Requested engineering information.
0 Display radio information of serving and neighbor cells


1 Display data transfer information only if modem in RRC-CONNECTED
state (not supported currently)
2 Display Tx/Rx total working duration (time)
3 Display PLMN Status
<sc_EARFCN> Integer type. EARFCN of the serving cell. Range: 0 – 262143.
<sc_EARFCN_offset> Integer type. EARFCN offset for the serving cell:
0 Offset of invalid
1 Offset of - 10
2 Offset of - 9
3 Offset of - 8
4 Offset of - 7
5 Offset of - 6
6 Offset of - 5
7 Offset of - 4
8 Offset of - 3
9 Offset of - 2
10 Offset of - 1
11 Offset of - 0.5
12 Offset of 0
13 Offset of 1
14 Offset of 2
15 Offset of 3
16 Offset of 4
17 Offset of 5
18 Offset of 6
19 Offset of 7
20 Offset of 8
21 Offset of 9
<sc_pci> Integer type. Physical cell ID of the serving cell. Range: 0 – 503.
<sc_cellID> String type. Four-byte (28-bit) cell ID in hexadecimal format for the serving
cell.
<sc_RSRP> Signed integer. RSRP value in dBm for the serving cell. (can be negative).
<sc_RSRQ> Signed integer. RSRQ value in dB for the serving cell. (can be negative).
<sc_RSSI> Signed integer. RSSI value in dBm for the serving cell. (can be negative).
<sc_SINR> Signed integer. Last SINR value in dB for the serving cell. (can be negative).
<sc_band> Integer type. Current serving cell band.
<sc_TAC> String type. Two-byte tracking area code (TAC) in hexadecimal format (e.g.
"00C3" equals 195 in decimal).
<sc_ECL> Integer type. Last Enhanced Coverage Level (ECL) value for the serving
cell. Range: 0 – 2. Only available in RRC connected state.
<sc_Tx_pwr> Signed integer. Current transmission power of UE. Unit: dBm.
Range: - 45 – 23 ,128 means an invalid value. (0 dBm = 1 mW, and this
parameter can be a negative value)
<operation_mode> Integer type. Operation mode of the serving cell:


0 In-band same PCI
1 In-band different PCI
2 Guard band
3 Stand alone
<nc_EARFCN> Integer type. The EARFCN of neighbor cell(s). Range: 0 – 262143.
<nc_pci> Integer type. Physical cell ID of the neighbor cell(s). Range: 0 – 503.
<nc_RSRP> Signed integer. RSRP value in dBm for neighbor cell(s) (can be negative).
<nc_RSRQ> Signed integer. RSRQ value in dB for neighbor cell(s) (can be negative).
<sleep_duration> Integer type. The total sleep duration from the latest boot-up or deep sleep.
Unit: 0.1 s.
<Rx_time> Integer type. The total Rx time since the latest boot-up or deep sleep. Unit:
0.1 s.
<Tx_time> Integer type. The total Tx time since the latest boot-up or deep sleep. Unit:
0.1 s.
<accuracy> Integer type. The resolution of <Rx_time> and <Tx_time>, which are both
0.1 second by default if <accuracy> is omitted.
0 1 ms.
Other value 0.1 s.
<EMM_state> String type. EMM state.
"NULL"
"DEREG"
"REG INIT"
"REG"
"DEREG INIT"
"TAU INI"
"SR INIT"
"UNKNOWN"
<EMM_mode> Sting type. Modem state.
"UNKNOWN"
"IDLE"
"PSM"
"CONNECTED"
<PLMN_state> String type. PLMN state.
"NO PLMN"
"SEARCHING"
"SELECTED"
"UNKNOWN" (deregistering or other unknown states)
<PLMN_type> String type. PLMN type.
"HPLMN"
"EHPLMN"
"VPLMN"
"UPLMN"
"OPLMN"
"OTHERS"


1. If the response of AT+QENG=0 is not in the range above defined, it is invalid.
2. For a better understanding of the Internet environment, the following criteria can be used to assess
    the network quality:
    Strong: RSRP ≥ - 100 dBm, SNR ≥ 3 dB, RSRQ > - 7 ;
    Medium: -100 dBm ≥ RSRP ≥ - 110 dBm, 3 dB > SNR > - 3 dB, - 7 > RSRQ > - 11 ;
    Weak: RSRP < -110 dBm or SNR < - 3 dB or RSRQ < - 11.
3. This parameter ‘<accuracy>’ only applies if <mode>=2.

#### Example

##### AT+QENG=0

##### +QENG: 0,3688,11,121,"05C4EF33",-72,-8,-64,14,8,"4C10",0,-128,3

##### OK

##### AT+QENG=3

+QENG: 4,"REG","PSM","SELECTED","EHPLMN","0x460,0xf000"

OK

### 4.9. AT+QESMC Query Cause to the Rejection of a Session Request

This command queries the cause to the rejection of a session establishment request, as is the use of
AT+CEREG.

##### "UNKNOWN"

<selectPLMN> String type. Current PLMN in numeric form.
<err> Integer type. Error code. See Chapter 15 for details.

#### AT+QESMC Query Cause to the Rejection of a Session Request

```
Test Command
AT+QESMC=?
```
```
Response
OK
Read Command
AT+QESMC?
```
```
Response
+QESMC: <rejCausePresent>,<causeType>,<rejCauseVa
lue>
```
```
OK
```
```
If there is any error:
ERROR
```
##### NOTE


#### Parameter

#### Example

##### AT+QESMC?

##### +QESMC: 1 ,0,26

##### OK

### 4.10. AT+QEMMS Query EMM State of UE

This command queries the EMM main state/sub-state.

```
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics /
```
```
<rejCausePresent> Integer type.
1 rejcause present.
<CauseType> Integer type. The type of <reject_cause>.
0 Indicates that <reject_cause> contains an ESM related cause value
1 Indicates that <reject_cause> contains a manufacturer specific cause value
<rejCauseValue> Integer type. Contains the cause of the failed registration. The value is of the
type defined by <CauseType>. For details about the cause value, see 3GPP TS
24.301.
<err> Error code. See Chapter 15 for details.
```
#### AT+QEMMS Query EMM State of UE

```
Test Command
AT+QEMMS=?
```
```
Response
OK
Read Command
AT+QEMMS?
```
```
Response
+QEMMS: <Mainstate>[,<Substate>]
```
```
OK
```
```
If there is any error:
ERROR
Or
```

#### Parameter

#### Example

##### AT+QEMMS?

##### +QEMMS: "EMM_REGISTERED,NORMAL_SERVICE"

```
+CME ERROR: <err>
```
```
Maximum Response Time 5 s
```
```
Characteristics /
```
```
<MainState> String type. Indicates the main state in EMM sublayer. See 3GP TS 24.301
5.3.1.3.2.2.
"NULL"
"EMM_REGISTERED_INITIATED"
"EMM_DEREGISTERED_INITIATED"
"EMM_TRACKING_AREA_UPDATING_INITIATED"
"EMM_SERVICE_REQUEST_INITIATED"
"EMM_DEREGISTERED"
"EMM_REGISTERED"
"UNKNOWN"
<Substate> String type. Indicates the substate in EMM sublayer.
When the main state is “EMM_DEREGISTERED", the substate can be as
follows:
"NORMAL_SERVICE"
"LIMITED_SERVICE"
"ATTEMPTING_TO_ATTACH"
"PLMN_SEARCH"
"NO_IMSI"
“ATTACH_NEEDED"
"NO_CELL_AVAILABLE"
When the main state is "EMM_REGISTERED", the substate can be as follows:
"NORMAL_SERVICE"
"ATTEMPTING_TO_UPDATE"
"LIMITED_SERVICE"
"PLMN_SEARCH"
"UPDATE_NEEDED"
"NO_CELL_AVAILABLE"
"ATTEMPTING_TO_UPDATE_MM"
"IMSI_DETACH_INITIATED"
<err> Error code. See Chapter 15 for details.
```

##### OK

### 4.11. AT+QOOSAIND Enable or Disable OOSA URC

This Write Command enables or disables OOSA URC +QOOSAIND: [<state>,<remaining_time>].

#### Parameter

#### AT+QOOSAIND Enable or Disable OOSA URC

```
Test Command
AT+QOOSAIND=?
```
```
Response
+QOOSAIND: (list of supported <OOSAIND>s)
Read Command
AT+QOOSAIND?
```
```
Response
+QOOSAIND: <OOSAIND>
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Write Command
AT+QOOSAIND=<QOOSAIND>
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect after the module is rebooted.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM automatically.
```
```
<QOOSAIND> Integer type.
0 Disable the OOSA URC indicator
1 Enable the OOSA URC indicator
<state> Integer type. PLMN state in NAS.
0 PLMN searching is inactivated. PLMN is not searched
1 PLMN is being searched
```

#### Example

##### AT+QOOSAIND=1

##### OK

### 4.12. AT+QEMMTIMER Gets EMM Timer Status

This command reports and gets the EMM timer status, including T3346, T3448, and T3412 or
T3412_EXT.

```
2 PLMN is selected
3 UE is in OOS status. The PLMN search timer is started
<remaining_time> Integer type. Remaining time of PLMN search timer. Unit: second. Only valid
when <state>=3.
<err> Error code. See Chapter 15 for details.
```
#### AT+QEMMTIMER Gets EMM Timer Status

Test Command
AT+QEMMTIMER=?

```
Response
+QEMMTIMER: (range of supported <bitmap>s)
```
OK
Read Command
AT+QEMMTIMER?

```
Response
+QEMMTIMER: <timerID>,<timer_state>[,<remain_time_value>]
+QEMMTIMER: <timerID>,<timer_state>[,<remain_time_value>]
+QEMMTIMER: <timerID>,<timer_state>[,<remain_time_value>]
```
```
OK
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Write Command
AT+QEMMTIMER=<bitmap>

```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
```
Maximum Response Time 5 s


#### Parameter

#### Example

##### AT+QEMMTIMER?

##### +QEMMTIMER: 0,1

##### +QEMMTIMER: 1,1

##### +QEMMTIMER: 2,0,1688

##### OK

Characteristics

```
The command takes effect immediately.
Remain valid after deep-sleep wakeup.
The configurations are saved to NVRAM automatically.
```
```
<bitmap> Integer type. Default value: 0. Range: 0 - 7, 0 (binary 000) means disable all
URCs, 7 (binary 111) means enable all URCs. This value is automatically
converted into binary format, with each bit representing a specific URC as
follows:
Bit 0 Enable/disable unsolicited result code T3346
Bit 1 Enable/disable unsolicited result code T334 8
Bit 2 Enable/disable unsolicited result code T3412 or T3412_EXT
The meaning of the value for each Bit:
0 Disable
1 Enable
<timerID> Integer type.
0 Emm timer: T3346
1 Emm timer: T3448
2 Emm timer: T 3412 or T3412_EXT
<timer_state> Integer type. Timer status.
0 Start
1 Stop
2 Expire
<remain_time_value> Integer type. Remaining time value. Unit: second. This parameter can be
reported only when <timer_state> is 0.
<err> Integer type. Error code. See Chapter 15 for details.
```

## 5 PDN and APN Commands

### 5.1. AT+CGACT PDP Context Activate/Deactivate

This Write Command activates or deactivates the specified PDP context(s). After the command has
completed, the MT remains in V.250 command state. The state of a PDP context already in the requested
state remains unchanged. If the requested state for any specified context cannot be achieved, an ERROR
or +CME ERROR response is returned. Extended error responses are enabled by AT+CMEE.

If the UE is not PS attached when the activation form of the command is executed, the UE first performs a
PS attachment and then attempts to activate the specified contexts. If the attachment fails then the MT
responds with an error or, if extended error responses are enabled, with the appropriate failure-to-attach
error message.

In the 3GPP TS 27.007 specification are the following statements:

For EPS, if an attempt is made to disconnect the last PDN connection, then the UE responds with
ERROR or if extended error responses are enabled, a +CME ERROR.

For EPS, the activation request for an EPS bearer resource will be answered by the network by either an
EPS dedicated bearer activation or EPS bearer modification request. The request must be accepted by
the UE before the PDP context can be set into established state.

If no <cid>s are specified, the activation form of the command activates all defined non-emergency
contexts, and the deactivation form of the command deactivates all active contexts.

This Read Command returns the current activation states for all the defined PDP contexts.

This Test Command is used for requesting information on the supported PDP context activation states.

#### AT+CGACT PDP Context Activate/Deactivate

```
Test Command
AT+CGACT=?
```
```
Response
+CGACT: (list of supported <state>s)
```
```
OK
Read Command
AT+CGACT?
```
```
Response
[+CGACT: <cid>,<state>]
```

#### Parameter

1. The initial PDP context with <cid>= 0 is automatically defined at startup.
2. This Write Command must and only specify one <cid>.
3. The maximum number of PDN connections that can be activated simultaneously is 11 and an
    established PDN connection is not allowed to be re-established.

#### Example

##### AT+CGACT=0,1

##### OK

##### AT+CGACT?

##### +CGACT: 1,0

##### OK

##### AT+CGACT=?

##### +CGACT: (0,1)

##### OK

```
[+CGACT: <cid>,<state>]
[...]
```
```
OK
Write Command
AT+CGACT=<state>,<cid>
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 70 s, determined by network.
Characteristics /
```
<state> Integer type. The state of PDP context activation.
0 Deactivated
1 Activated
<cid> Integer type. A numeric parameter which specifies a particular PDP context definition (see
AT+CGDCONT).
<err> Error code. See Chapter 15 for details.

##### NOTE


### 5.2. AT+CGAPNRC APN Rate Control

This Write Command returns the APN rate control parameters (see 3GPP TS 24.008) associated with the
provided context identifier <cid>.

This Test Command returns a list of <cid>s associated with secondary and non-secondary active PDP
contexts.

#### Parameter

#### AT+CGAPNRC APN Rate Control

```
Test Command
AT+CGAPNRC=?
```
```
Response
+CGAPNRC: (list of <cid>s associated with active contexts)
```
```
OK
Write Command
AT+CGAPNRC=<cid>
```
```
Response
+CGAPNRC: <cid>[,<additional_exception_reports>[,<u
plink_time_unit>[,<maximum_uplink_rate>]]]
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
Characteristics /
```
<cid> Integer type. A particular PDP context definition (see
AT+CGDCONT).
<additional_exception_reports> Integer type. Whether additional exception reports are allowed to
be sent or not when the maximum uplink rate is reached. This
refers to bit-4 of octet-1 of the APN rate control parameters IE as
specified in 3GPP TS 24.008 subclause 10.5.6.3.2.
0 Additional exception reports at maximum rate reached are
not allowed to be sent.
1 Additional exception reports at maximum rate reached are
allowed to be sent.
<uplink_time_unit> Integer type. The time unit to be used for the maximum uplink rate.
This refers to bits 1 to 3 of octet-1 of the APN rate control
parameters IE as specified in 3GPP TS 24.008 subclause


### 5.3. AT+CGAUTH Define PDP Context Authentication Parameters

The Write Command allows the TE to specify authentication parameters for a PDP context identified by
the (local) context identification parameter <cid> used during the PDP context activation and the PDP
context modification procedures. Since the <cid> is the same parameter as that used in AT+CGDCONT
and AT+QCGDEFCONT commands, AT+CGAUTH is effectively as an extension to these commands.

The Test Command returns values supported as compound values. The Read Command returns the
current settings for each defined context.

##### 10.5.6.3.2.

0 Unrestricted
1 Minute
2 Hour
3 Day
4 Week
<maximum_uplink_rate> Integer type. The maximum number of messages the UE is
restricted to send per uplink time unit. This refers to octets 2 to 4 of
the APN rate control parameters IE as specified in 3GPP TS
24.008 subclause 10.5.6.3.2.
<err> Error code. See Chapter 15 for details.

#### AT+CGAUTH Define PDP Context Authentication Parameters

```
Test Command
AT+CGAUTH=?
```
```
Response
+CGAUTH: (range of supported <cid>s),(list of
supported <auth_proto>s),(max length of
<userid>),(max length of <password>)
```
```
OK
Read Command
AT+CGAUTH?
```
```
Response
[+CGAUTH: <cid>,<auth_proto>[,<userid>,<pas
sword>]]
[+CGAUTH: <cid>,<auth_proto>[,<userid>,<pas
sword>]]
[...]
```
```
OK
Write Command
AT+CGAUTH=<cid>[,<auth_proto>[,<userid>[,
<password>]]]
```
```
Response
OK
```
```
If there is any error:
```

#### Parameter

#### Example

##### AT+CGAUTH=?

##### +CGAUTH: (0-10),(0-1),(20),(20)

##### OK

##### AT+CGAUTH?

##### +CGAUTH: 0,0,"",""

##### OK

##### AT+CGDCONT=1,IP

##### OK

AT+CGAUTH=1,1,"userid","psw"
OK

##### ERROR

```
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect immediately.
The configurations are not saved to NVRAM and will
be deleted after deep-sleep wakeup.
```
<cid> Integer type. A numeric parameter that specifies a particular PDP context
definition (see AT+CGDCONT for details).
<auth_proto> Integer type. Authentication protocol used for this PDP context.
0 None. Used to indicate that no authentication protocol is used for
this PAP
1 PAP
<userid> String type. User ID string, the max length is 20 characters with 1 line
end mark.
<password> String type. Password string, the max length is 20 characters with 1 line
end mark.
<err> Error code. See Chapter 15 for details.


### 5.4. AT+CGDCONT Define PDP Context

This Write Command specifies PDP context parameters for a PDP context identified by the (local) context
identification parameter <cid>. It also allows the TE to specify whether security protected transmission of
ESM information is requested, because the PCO can include information that requires ciphering. There
can be other reasons for the UE to use security protected transmission of ESM information, e.g. if the UE
needs to transfer an APN. The number of PDP contexts that may be in a defined state at the same time is
given by the range returned by the Test Command.

For EPS the PDN connection and its associated EPS default bearer is identified herewith. For EPS the
<PDP_addr> shall be omitted.

A special form of the Write Command, AT+CGDCONT=<cid> causes the values for context number
<cid> to become undefined.

This Read Command returns the current settings for each defined context.

This Test Command returns values supported as a compound value. If the UE supports several PDP
types, <PDP_type>, the parameter value ranges for each <PDP_type> are returned on a separate line.

By default, the initial PDP context with <cid>=0 is defined upon startup and cannot to be defined with the
AT+CGDCONT command. Please configure the initial PDP context (<cid>=0) with AT+QCGDEFCONT.
When in E-UTRAN, the initial PDP context is automatically activated by the MT following a successful
registration to the network depending on the setting of AT+CIPCA. If all active contexts are deactivated,
the initial PDP context can be (re)established.

#### AT+CGDCONT Define PDP Context

```
Test Command
AT+CGDCONT=?
```
```
Response
+CGDCONT: (range of supported <cid>s),(list of
supported <PDP_type>s),,,,,(list of supported
<IPv4_addr_alloc>s),(range of supported
<request_type>s),(range of supported
<P-CSCF_discovery>s),(list of supported
<IM_CN_signaling_flag_ind>s),(list of supported
<NSLPI>s),(list of supported <securePCO>s),(list
of supported <IPv4_MTU_discovery>s),(list of
supported <local_addr_ind>s),(list of supported
<Non-IP_MTU_discovery>s),(list of supported
<Reliable_Data_Service>s)
```
```
OK
Read Command
AT+CGDCONT?
```
```
Response
[+CGDCONT: <cid>,<PDP_type>,<APN>,<PDP_a
```

#### Parameter

```
ddr>,<d_comp>,<h_comp>[,<IPv4_addr_alloc>[,
<request_type>[,<P-CSCF_discovery>[,<IM_CN_
signaling_flag_ind>[,<NSLPI>[,<securePCO>[,<I
Pv4_MTU_discovery>[,<local_addr_ind>[,<Non-I
P_MTU_discovery>]]]]]]]]]]
[+CGDCONT: <cid>,<PDP_type>,<APN>,<PDP_a
ddr>,<d_comp>,<h_comp>[,<IPv4_addr_alloc>[,
<request_type>[,<P-CSCF_discovery>[,<IM_CN_
signaling_flag_ind>[,<NSLPI>[,<securePCO>[,<I
Pv4_MTU_discovery>[,<local_addr_ind>[,<Non-I
P_MTU_discovery>]]]]]]]]]]
[...]
```
```
OK
Write Command
AT+CGDCONT=<cid>[,<PDP_type>[,<APN>[,<
PDP_addr>[,<d_comp>[,<h_comp>[,<IPv4_ad
dr_alloc>[,<request_type>[,<P-CSCF_discove
ry>[,<IM_CN_signaling_flag_ind>[,<NSLPI>[,<
securePCO>[,<IPv4_MTU_discovery>[,<local
_addr_ind>[,<Non-IP_MTU_discovery>]]]]]]]]]]
]]]]
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
```
```
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect immediately.
Besides the initial PDP context (<cid>=0), the
configurations of the first two defined PDP contexts
are saved to NVRAM automatically. The
configurations of other PDP contexts are not saved
to NVRAM.
If the defined <cid> is activated, the configuration
will be valid after deep-sleep wakeup. Otherwise, it
will be deleted after deep-sleep wakeup.
```
<cid> Integer type. A numeric parameter that specifies a particular PDP context definition.
The parameter is local to the UE-TE interface and is used in other PDP context-related
commands. Range: 0 – 10. 0 only appears in the response of Read Command.
<PDP_type> String type. A string parameter which specifies the type of packet data protocol.
"IP" Internet Protocol (IETF STD 5)
"IPV6" Internet Protocol version 6
"IPV4V6" Virtual <PDP_type> introduced to handle dual-IP-stack UE capability
"Non-IP" None IP


<APN> String type. A logical name that is used to select the GGSN or the external packet data
network. The maximum configurable APN length is 99 bytes. If the value is null or
omitted, then the subscription value will be requested.
<PDP_addr> String type. A string parameter that identifies the UE in the address space applicable to
the PDP. If the value is null or omitted, then a value may be provided by the TE during
the PDP startup procedure or, failing that, a dynamic address will be requested. The
read form of the command continues to return the null string even if an address has
been allocated during the PDP startup procedure. The allocated address may be read
by AT+CGPADDR.
<d_comp> Integer type. Controls PDP data compression.
0 Off
1 On (manufacturer preferred compression)
2 V.42bis
3 V.44
<h_comp> Integer type. Controls PDP header compression.
0 Off
1 On
2 RFC 1144 (applicable for SNDCP only)
3 RFC 2507
4 RFC 3095[ROHC] (applicable for PDCP only)
<IPv4_addr_alloc> Integer type. Controls how the MT/TA requests to get the IPv4 address
information.
0 IPv4 address allocation through NAS signaling
1 IPv4 address allocated through DHCP
<request_type> Integer type. The type of PDP context activation request for the PDP
context. See 3GPP TS 24.301 (subclause 6.5.1.2) and 3GPP TS 24.008
(subclause 10.5.6.17). It is not allowed to set <cid> to 0 for emergency
bearer services. According to 3GPP TS 24.008 (subclause 4.2.4.2.2 and
subclause 4.2.5.1.4) and 3GPP TS 24.301 (subclause 5.2.2.3.3 and
subclause 5.2.3.2.2), a separate PDP context must be established for
emergency bearer services.
If the PDP context for emergency bearer services is the only activated
context, then only emergency calls are allowed (see 3GPP TS 23.401
subclause 4.3.12.9).
0 PDP context is for new PDP context establishment or for handover
from a non-3GPP access network (how the MT decides whether the
PDP context is for new PDP context establishment or for handover
is implementation specific).
1 PDP context is for emergency bearer services
2 PDP context is for new PDP context establishment
3 PDP context is for handover from a non-3GPP access network
<P-CSCF_discovery> Integer type. Influences how the MT/TA requests to get the P-CSCF
address (refer to 3GPP TS 24.229 Annex B and Annex L).
0 Preference of P-CSCF address discovery not influenced by


#### Example

##### AT+CGDCONT=?

+CGDCONT: (0- 10 ),("IP","IPV6","IPV4V6","Non-IP"),,,,,(0,1),(0-3),(0-2),(0,1),(0,1),(0,1),(0,1),(0,1),(0,
1),(0,1)

##### AT+CGDCONT

1 Preference of P-CSCF address discovery through NAS signaling
2 Preference of P-CSCF address discovery through DHCP
<IM_CN_signaling_flag_ind> Integer type. Indicates to the network whether the PDP context is for IM
CN subsystem related signaling only or not.
0 UE indicates that the PDP context is not for IM CN
subsystem-related signaling only
1 UE indicates that the PDP context is for IM CN subsystem-related
signaling only
<NSLPI> Integer type. The NAS signaling priority requested for this PDP context.
MT utilizes the provided NSLPI information as specified in 3GPP TS
24.301 and 3GPP TS 24.008.
0 Indicates that this PDP context is to be activated with the value for
the low priority indicator configured in the MT.
1 Indicates that this PDP context is to be activated with the value for
the low priority indicator set to "MS is not configured for NAS
signaling low priority".
<securePCO> Integer type. Specifies whether security protected transmission of PCO
is requested or not (applicable for EPS only).
0 Security protected transmission of PCO is not requested
1 Security protected transmission of PCO is requested
<IPv4_MTU_discovery> Integer type. Influences how the MT/TA requests to get the IPv4 MTU
size, see 3GPP TS 24.008 subclause 10.5.6.3.
0 Preference of IPv4 MTU size discovery not influenced by
AT+CGDCONT
1 Preference of IPv4 MTU size discovery through NAS signaling
<local_addr_ind> Integer type. Indicates whether MS supports local IP address in TFTs
0 Indicates that the MS does not support local IP address in TFTs
1 Indicates that the MS supports local IP address in TFTs
<Non-IP_MTU_discovery> Integer type. Influences how the MT/TA requests to get the Non-IP MTU
size (see 3GPP TS 24.008 subclause 10.5.6.3).
0 Preference of Non-IP MTU size discovery not influenced by
AT+CGDCONT
1 Preference of Non-IP MTU size discovery through NAS signaling
<Reliable_Data_Service> Integer type. Whether UE supports reliable transmission.
0 Not support
1 Support (currently not support)
<err> Error code. See Chapter 15 for details.


##### OK

##### AT+CGDCONT=1,"IP","CMNET"

##### OK

##### AT+CGDCONT?

##### +CGDCONT: 0 ,"IP","CMNBIOT","100.81.144.240"

##### +CGDCONT: 1,"IP","CMNET"

##### OK

1. The value of <APN> is case-insensitive, and the reads are converted to uppercase regardless of
    whether the input is uppercase or lowercase.
2. <cid>=0 can be configured by AT+QCGDEFCONT.

### 5.5. AT+CIPCA Initial PDP Context Activation

This Write Command controls whether the UE is attached to E-UTRAN with or without a PDN connection.
The setting of <n>=3 applies to E-UTRAN RATs.

For <attach_without_PDN>=1, the EPS attachment is performed without a PDN connection.

This Read Command returns the current settings of the command.

This Test Command returns values supported as a compound value.

#### AT+CIPCA Initial PDP Context Activation

```
Test Command
AT+CIPCA=?
```
```
Response
+CIPCA: (list of supported <n>s),(list of supported <attac
h_without_PDN>s)
```
```
OK
Read Command
AT+CIPCA?
```
```
Response
+CIPCA: <n>,<attach_without_PDN>
```
```
OK
```
```
If there is any error:
ERROR
Or
```
##### NOTE


#### Parameter

#### Example

##### AT+CIPCA=?

##### +CIPCA: (3),(0,1)

##### OK

### 5.6. AT+QCGDEFCONT Set Default PSD Connection Settings

This Write Command sets the PSD connection settings for PDN connection on power-up. When MT
attaches to the NB-IoT network on power-up, a PDN connection is established. Therefore, PDN
connection settings are stored in NVRAM so that they can be used by the modem during the attachment.

```
+CME ERROR: <err>
Write Command
AT+CIPCA=<n>,<attach_without_PD
N>
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 300 ms
```
```
Characteristics
```
```
The command takes effect immediately.
Remain valid after deep-sleep wakeup.
The configurations are saved to NVRAM.
```
<n> Integer type. Activation of PDP context upon attaching.
3 This is the current setting and does not need to be changed
<attach_without_PDN> Integer type. Whether EPS attachment is performed with or without PDN
connection.
0 EPS attachment is performed with a PDN connection
1 EPS attachment is performed without a PDN connection
<err> Error code. See Chapter 15 for details.

#### AT+QCGDEFCONT Set Default PSD Connection Settings

```
Test Command
AT+QCGDEFCONT=?
```
```
Response
+QCGDEFCONT: (list of supported <PDP_type>s)
```

#### Parameter

##### OK

```
Read Command
AT+QCGDEFCONT?
```
```
Response
+QCGDEFCONT: <PDP_type>,[[[[<APN>],<user_name>],
<password>],<auth_type>]
```
```
OK
Write Command
AT+QCGDEFCONT=<PDP_type>[,<A
PN>[,<user_name>,<password>[,<au
th_type>]]]
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect after the module is rebooted.
Remain valid after deep-sleep wakeup.
The configurations are saved to NVRAM automatically.
```
<PDP_type> String type. Specify the type of packet data protocol:
"IP" Internet Protocol (IETF STD 5)
"IPV6" Internet Protocol version 6 (IETF RFC 2460)
"IPV4V6" Dual IP stack (see 3GPP TS 24.301)
"Non-IP" Transfer of Non-IP data to external packet network (see 3GPP TS 24.301)
<APN> String type. A logical name that is used to select the GGSN or the external packet data
network. The maximum configurable APN length is 99 bytes. If the value is null or
omitted, then the subscription value will be requested.
<user_name> String type. The user name for accessing the IP network. The maximum configurable
APN length is 19 bytes.
<password> String type. The password for accessing the IP network. The maximum configurable
APN length is 19 bytes.
<auth_type> Integer type. The authentication type of the APN. Range: 0 – 2.
0 None. If <user_name> and <password> are omitted, the <auth_type> is None
by default. It should not be set by AT commands.
1 PAP. If this parameter is omitted, but <user_name> and <password> exist. The
default value of <auth_type> is “PAP".
2 CHAP. Not support currently. Please do not set <auth_type> to this value lest the
<PDP_type> and <APN> be changed correspondingly.
<err> Error code. See Chapter 15 for details.


#### Example

##### AT+QCGDEFCONT=?

+QCGDEFCONT: ("IP","IPV6","IPV4V6","Non-IP")

OK


## 6 3GPP R14 Protocol Commands

The 3GPP R14 protocol extends the capabilities of the UE. That means switching between R13 and R14
protocol versions with AT commands may change some default configurations or make some
configuration items automatically adapts to the configurations supported by the R13 protocol. Therefore, it
is recommended to check and confirm the configuration items after configuring all items with the Write
Commands in this Chapter.

### 6.1. AT+CNMPSD Trigger R14 RAI

This command notifies the network that no application is expected to exchange data. If RAI in AS is
enabled, this command triggers the RAI in the AS to release RRC connection quickly.

#### Parameter

#### AT+CNMPSD Trigger R14 RAI

```
Test Command
AT+CNMPSD=?
```
```
Response
OK
Execution Command
AT+CNMPSD
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics /
```
```
<err> Error code. See Chapter 15 for details.
```

### 6.2. AT+QR14FEATURE Query Status of R14 Features

This command queries whether the current network supports R14 protocol and what features are
supported. If the module stays in idle staus, some of the features that can only be queried in connected
status are unable to be checked. Thus, it is recommended to execute the command in connected status.

#### Parameter

#### AT+QR14FEATURE Query Status of R14 Features

```
Test Command
AT+QR14FEATURE=?
```
```
Response
OK
Execution Command
AT+QR14FEATURE
```
```
Response
+QR14FEATURE: <UE_rel>,<UE_MAC_RAI>
+QR14FEATURE: <net_feature>
+QR14FEATURE: <2-harq>,<net_MAC_RAI>,<N_NPRAC
H>,<N_paging>,<cp_reest>
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics /
```
```
<UE_rel> Integer type. Protocol supported by UE.
14 UE supports R14 protocol and enables the features by default
13 UE supports R13 protocol only
<UE_MAC_RAI> Integer type. Whether MAC RAI is enabled. MAC RAI can only be used when the
module is working in R14 mode.
0 RAI in AS is disabled
1 RAI in AS is enabled. If RAI is enabled by both network and UE, you can
trigger a quick release of RRC connection with AT+CNMPSD
<net_feature> Integer type. Whether the R14 features listed below are enabled by the network.
The value is 1 if any one of the features is enabled.
0 None of the features listed below is enabled by the network
1 At least one of the features is enabled
<net_MAC_RAI> Integer type. MAC RAI status of UE returned by network.
0 RAI in AS is disabled by RAU
```

#### Example

AT+QR14FEATURE //Query the current status of R14 features.
+QR14FEATURE: 13,0
+QR14FEATURE: 0
+QR14FEATURE: 0,0,0,0,0

OK

### 6.3. AT+QCFG Configure System

This command configures the system parameters of UE. This Write Command can only be used when
AT+CFUN=0.

```
1 RAI in AS is enabled. If RAI is enabled by both network and UE, you can
trigger a quick release of RRC connection with AT+CNMPSD
<2-harq> Integer type. Whether 2 - HARQ is enabled by the network.
0 2 - HARQ is not enabled
1 2 - HARQ is enabled
<N_NPRACH> Integer type. Whether the network supports random access on non-anchor carrier.
0 Not support
1 Support
<N_paging> Integer type. Whether the network supports paging on non-anchor carrier.
0 Not support
1 Support
<cp_reest> Integer type. Whether the network supports re-establishing with CP-CIOT.
0 Not support
1 Support
<err> Error code. See Chapter 15 for details.
```
#### AT+QCFG Configure System

```
Test Command
AT+QCFG=?
```
```
Response
List of
+QCFG: <function>,(list of supported <value>s)
...
```
```
OK
Write Command
AT+QCFG=<function>[,<value>]
```
```
Response
If the optional parameter is omitted, query the current
configurations:
+QCFG: <function>,<value>
```

#### Parameter

##### OK

```
If the optional parameter is specified, configure the
corresponding feature:
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Read Command
AT+QCFG?
```
```
Response
List of
+QCFG: <function>, <value>
...
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect after the module is rebooted.
Remain valid after deep-sleep wakeup.
The configurations are saved to NVRAM automatically.
```
```
<function> String type. Features to be configured.
"MacRAI" RAI mechanism in AS
"relversion" Protocol version supported by UE
"NBcategory" UE-Category
<value> Integer.
<function> <value> Description
"MacRAI" 0 Disable RAI in AS
1 Enable RAI in AS
"relversion" 13 R13 protocol
14 R14 protocol
"NBcategory" 1 Cat NB1 with R13 default configurations
2 Cat NB2 with R14 default configurations
<err> Error code. See Chapter 15 for details.
```

## 7 Other Network Commands................................................................................................................

### 7.1. AT+CCIOTOPT CloT Optimization Configuration

This Write Command controls which CIoT EPS optimizations the UE indicates as supported and preferred
in the ATTACH REQUEST and TRACKING AREA UPDATE REQUEST messages. The command also
allows reporting of the CIoT EPS optimizations that are supported by the network. UE supporting CIoT
functionality supports control plane CIoT EPS optimization or user plane CIoT EPS optimization or both
(see 3GPP TS 24.301 subclause 9.9.3.34). Based on the application characteristics the UE may prefer to
be registered for control plane CIoT EPS optimization or for user plane CIoT EPS optimization (see 3GPP
TS 24.301 subclause 9.9.3.0B).

Further, the network may support control plane CIoT EPS optimization or user plane CIoT EPS
optimization or both (see 3GPP TS 24.301 subclause 9.9.3.12A).

This Write Command controls the URC +CCIOTOPTI. The URC +CCIOTOPTI:
<supported_network_opt> indicates the supported CIoT EPS optimization by the network.

This Read Command returns the current settings for supported and preferred CIoT EPS optimization and
the current status of unsolicited result code +CCIOTOPTI.

#### AT+CCIOTOPT CloT Optimization Configuration

```
Test Command
AT+CCIOTOPT=?
```
```
Response
+CCIOTOPT: (range of supported <n>s),(list of supported
<supported_UE_opt>s),(range of supported <preferred_
UE_opt>s)
```
```
OK
Read Command
AT+CCIOTOPT?
```
```
Response
+CCIOTOPT: <n>,<supported_UE_opt>,<preferred_UE_o
pt>
```
```
OK
Write Command
AT+CCIOTOPT=<n>[,<supported_UE
_opt>[,<preferred_UE_opt>]]
```
```
Response
OK
```

#### Parameter

### 7.2. AT+COPS Operator Selection

This Write Command forces an attempt to select and register the EPS network operator using the USIM
card installed in the currently selected card slot. <mode> is used to select whether the selection is done
automatically by the MT or is forced by this command to operator <oper> (it shall be given in format
<format>) to a certain access technology, indicated in <AcT>. If the selected operator is not available, no
other operator shall be selected (except <mode>=4). If the selected access technology is not available,
then the same operator shall be selected in other access technologies. The selected operator name
format shall also apply to the read command (AT+COPS?). <mode>=2 forces an attempt to deregister

```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect immediately.
Remain valid after deep-sleep wakeup.
The configurations are saved to NVRAM automatically.
```
```
<n> Integer type. Enable/disable reporting of URC +CCIOTOPTI.
0 Disable reporting
1 Enable reporting, +CCIOTOPTI: <supported_network_opt>
3 Disable reporting and reset the parameters for CIoT EPS
optimization to the default values
<supported_UE_opt> Integer type. Indicates the UE’s support for CIoT EPS optimizations.
1 Support control plane CIoT EPS optimization
3 Support both control plane and user plane CIoT EPS optimizations
<preferred_UE_opt> Integer type. Indicates the UE’s preference for CIoT EPS optimizations.
0 No preference
1 Preference for control plane CIoT EPS optimization
2 Preference for user plane CIoT EPS optimization
<supported_network_opt> Integer type. Indicates the network’s support for CIoT EPS
optimizations.
0 Not support
1 Support control plane CIoT EPS optimization
2 Support user plane CIoT EPS optimization
3 Support both control plane and user plane CIoT EPS optimizations
<err> Error code. See Chapter 15 for details.
```

from the network. The selected mode affects all further network registration (e.g. after <mode>=2, MT
shall be unregistered until <mode>=0 or 1 is selected). This command should be abortable when a
registration/deregistration attempt is made.

This Read Command returns the current mode, the currently selected operator and the current access
technology. If no operator is selected, <format>, <oper> and <AcT> are omitted.

This Test Command returns a set of five parameters, each representing an operator present in the
network. A set consists of an integer indicating the availability of the operator <stat>, long and short
alphanumeric format of the operator’s name, numeric format representation of the operator and access
technology. Any of the formats may be unavailable and should then be an empty field. The list of
operators shall be in the order of: home network, networks referenced in USIM or active application in the
UICC (USIM) in the following order: HPLMN selector, user controlled PLMN selector, operator controlled
PLMN selector and PLMN selector (in the USIM), and other networks.

The <AcT> access technology selected parameters should only be used in terminals capable to register
to more than one access technology. Selection of <AcT> does not limit the capability to cell reselections,
even though an attempt is made to select an access technology, the phone may still re-select a cell in
another access technology.

#### AT+COPS Operator Selection

```
Test Command
AT+COPS=?
```
```
Response
+COPS: list of supported (<stat>,long alphanumeric <ope
r>,short alphanumeric <oper>,numeric <oper>[,<AcT>])s]
[,,(range of supported <mode>s),(range of supported <fo
rmat>s)
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Read Command
AT+COPS?
```
```
Response
+COPS: <mode>[,<format>,<oper>][,<AcT>]
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Write Command
AT+COPS=<mode>[,<format>[,<oper
```
```
Response
OK
```

#### Parameter

1. This Test Command interrupts the data sending if the data transmitting is ongoing.
2. This Write Command can be executed only when the module is in the idle state or de-registered state
    with an USIM card inserted, otherwise an error is returned.

```
>[,<AcT>]]
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 305 s
```
```
Characteristics
```
```
The command takes effect immediately.
Remain valid after deep-sleep wakeup.
Only when <mode>=0/1/4, the configurations are to NVRAM
automatically.
```
<mode> Integer type.
0 Automatic mode (<oper> field is ignored)
1 Manual operator selection (<oper> field shall be present)
2 Manually deregister from network
3 Set <format> not shown in read command response
4 Manual/automatic selected. If manual selection fails, automatic mode
(<mode>=0) is entered
<format> Integer type.
0 Long format alphanumeric <oper>
1 Short format alphanumeric <oper>
2 Numeric <oper>. Only valid when <mode>=1 or <mode>= 4
<oper> String type. <format> indicates if the form at is numeric. Numeric format is the NB-IoT
network location area identification number which consists of a three BCD digit ITU-T
country code, plus a two or three BCD digit network code, which is administration specific.
<oper> field could not be present when <mode>=0.
<stat> Integer type.
0 Unknown
1 Operator available
2 Operator currently selected
3 Operator forbidden to be selected
<AcT> Integer type. Access technology selected.
9 E-UTRAN (NB-S1 mode)
<err> Error code. See Chapter 15 for details.

##### NOTE


#### Example

##### AT+COPS=0

##### OK

##### AT+COPS?

##### +COPS: 0,2,"46000", 9

##### OK

##### AT+COPS=?

##### +COPS: (2,"CHINA MOBILE","CMCC","46000",9),(3,"CHINA UNICOMM","CUCC","46001",9),(1,"",

##### "","21405",9),(1,"CHINA TELECOM","CTCC","46011",9),,(0-4),(0-2)

##### OK

### 7.3. AT+CRTDCP Reporting of Terminating Data via the Control Plane

The Write Command enables or disables reporting of data from the network to the MT that is transmitted
via the control plane in downlink direction. If the reporting is enabled, the MT returns the unsolicited result
code +CRTDCP: <cid>,<cpdata_length>,<cpdata> when data is received from the network.

#### AT+CRTDCP Reporting of Terminating Data via the Control Plane

```
Test Command
AT+CRTDCP=?
```
```
Response
+CRTDCP: (list of supported <reporting>s),(range of
supported <cid>s),(maximum number of octets of user data
indicated by <cpdata_length>)
```
```
OK
Read Command
AT+CRTDCP?
```
```
Response
+CRTDCP: <reporting>
```
```
OK
Write Command
AT+CRTDCP=<reporting>
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
Characteristics /
```

#### Parameter

### 7.4. AT+CSODCP Sending of Originating Data via Control Plane

The Write Command is used by the TE to transmit data over control plane to network via MT. Context
identifier <cid> is used to link the data to particular context.

This command optionally indicates that the application on the MT expects that the exchange of data:
⚫ will be completed with this uplink data transfer;
⚫ will be completed with the next received downlink data.

This command also optionally indicates whether or not the data to be transmitted is exception data. This
command causes transmission of an ESM DATA TRANSPORT message, as defined in 3GPP TS 24.301.

```
<cid> Integer type. A numeric parameter which specifies a particular PDP context or
EPS bearer context definition. The <cid> parameter is local to the TE-MT
interface and identifies the PDP or EPS bearer contexts configured via
AT+CGDCONT. Range: 0–10.
<cpdata_length> Integer type. The number of octets of the <cpdata> information element. Range:
0 – 1600. Unit: byte. When there is no data to transmit, the value will be set to 0.
<cpdata> String of octets. Contains the user data container contents (refer 3GPP TS
24.301 subclause 9.9.4.24). When there is no data to transmit, the <cpdata>
shall be an empty string (""). It supports "HEX" character format.
<reporting> Integer type. Controls reporting of mobile terminated control plane data events.
0 Disable reporting of MT control plane data
1 Enable reporting of MT control plane data by the unsolicited result code
+CRTDCP: <cid>,<cpdata_length>,<cpdata>
<err> Error code. See Chapter 15 for details.
```
#### AT+CSODCP Send Originating Data via Control Plane

```
Test Command
AT+CSODCP=?
```
```
Response
+CSODCP: (range of supported <cid>s),(maximum number
of octets of user data indicated by <cpdata_length>),(range
of supported <RAI>s),(list of supported
<type_of_user_data>s)
```
```
OK
Write Command
AT+CSODCP=<cid>,<cpdata_length>
,<cpdata>,[<RAI>[,<type_of_user_dat
a>]]
```
```
Response
OK
```
```
If there is any error:
ERROR
```

#### Parameter

### 7.5. AT+QBAND Get and Set Mobile Operation Band

This command gets the currently registered band or sets the bands to be locked.

```
Or
+CME ERROR: <err>
Maximum Response Time 5 s
Characteristics /
```
<cid> Integer type. Specifies a particular PDP context definition. Range: 0–10.
<cpdata_length> Integer type. The number of octets of the <cpdata> information element.
Range: 0– 950. Unit: byte.
<cpdata> String type. The data to be sent. Contains the user data container contents
(refer 3GPP TS 24.301 subclause 9.9.4.24). When there is no data to
transmit, the <cpdata> shall be an empty string (""). The maximum length of
<cpdata> are implementation specific.
<RAI> Integer type. Indicates the value of the release assistance indication.
0 No information available
1 The MT expects that exchange of data will be completed with the
transmission of the ESM DATA TRANSPORT message
2 The MT expects that exchange of data will be completed with the receipt
of an ESM DATA TRANSPORT message
<type_of_user_data> Integer type. Indicates whether the user data that is transmitted is regular or
exceptional.
0 Regular data
1 Exception data
<err> Error code. See Chapter 15 for details.

#### AT+QBAND Get and Set Mobile Operation Band

```
Test Command
AT+QBAND=?
```
```
Response
+QBAND: (range of supported <band_number>s),(list of
supported <operating_band>s)
```
```
OK
Read Command
AT+QBAND?
```
```
Response
+QBAND: <operating_band>
```
```
OK
```

#### Parameter

#### Example

AT+QBAND=? //Query the list of supported bands.
+QBAND: (0- 17 ),(1,2,3,4,5,8,12,13,17,18,19,20,25,28,66,70,85)

OK
AT+QBAND=1,4 //Set the band to be used.
OK
AT+QBAND? //Query the band that has been set earlier.
+QBAND: 4

OK

```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Write Command
AT+QBAND=<band_number>[,<ban
d>[,<band>[,...]]]
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 900 s
```
```
Characteristics
```
```
The command takes effect immediately.
Remain valid after deep-sleep wakeup.
The configurations are saved to NVRAM automatically.
```
<band_number> Integer type. Preferred band number to be searched for.
0 All bands
1 – 17 Number of bands
<band> Integer type. Currently preferred NB-IoT bands to be searched for.
Valid values: 1, 2, 3, 4, 5, 8, 12, 13, 17, 18, 19, 20, 25, 28, 66, 70, 85.
<operating_band> Integer type. The band(s) that has been set earlier.
Valid values: 1, 2, 3, 4, 5, 8, 12, 13, 17, 18, 19, 20, 25, 28, 66, 70, 85.
<err> Error code. See Chapter 15 for details.


The Write Command will trigger a detachment and re-attachment procedure.

### 7.6. AT+QCSEARFCN Clear Stored NB-IoT EARFCN List

This command clears the stored EARFCN list for the UE.

#### Parameter

#### Example

AT+QCSEARFCN //Clear stored EARFCN list for the UE.
OK

#### AT+QCSEARFCN Clear Stored NB-IoT EARFCN List

```
Execution Command
AT+QCSEARFCN
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
Only can be executed when AT+CFUN=0, and takes effect
after switching to AT+CFUN=1. For details on AT+CFUN, see
Chapter 0.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM automatically.
```
<err>^ Error code. See^ Chapter^15 for details.^

##### NOTE


### 7.7. AT+QLOCKF Lock NB-IoT Frequency and PCI

This command locks the UE to a specific frequency and an optional cell ID. The value of <pci> greater
than 503 causes error returned; and if <pci> is smaller than 0, or a non-integer value, it is ignored.

#### AT+QLOCKF Lock NB-IoT Frequency and PCI

```
Test Command
AT+QLOCKF=?
```
```
Response
+QLOCKF: (list of supported <mode>s)
```
```
OK
Read Command
AT+QLOCKF?
```
```
Response
[+QLOCKF: [1,<EARFCN>[,<pci>]]]
[+QLOCKF: [2,<EARFCN1>,[<EARFCN 2>,...]]]
```
```
OK
Write Command
Unlock NB-IoT Frequency(<mode>= 0 )
AT+QLOCKF=<mode>
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Write Command
Lock NB-IoT Frequency (<mode>= 1 )
AT+QLOCKF=<mode>,<EARFCN>[,,<
pci>]]
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Write Command
Set priority frequency (<mode>= 2 )
AT+QLCOKF=<mode>,,<numofEARF
CN>,<EARFCN 1 >[,<EARFCN 2 > ]...
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
Only can be executed when AT+CFUN=0, and takes effect
after switching to AT+CFUN=1. For details on AT+CFUN, see
Chapter 9.3.
Remain valid after deep-sleep wakeup.
The configurations are saved to NVRAM automatically.
```

#### Parameter

1. This Write Command should be conducted after you execute AT+CFUN=0.
2. <mode>=2 is only applicable to valid downlink carrier frequency setting.

#### Example

##### AT+QLOCKF=1,2508

##### OK

### 7.8. AT+QNBPARA Query Timing Advance Value

The command queries Timing Advance value. It returns - 1 when the module is in idle status.

<mode> Integer type. Activate/remove the lock.
0 Remove lock
1 Activate lock
2 Set the preferred frequency
<EARFCNx> Integer type. The requested EARFCN on which to lock. Range: 0 – 262143. Value
0 indicates to remove any lock of EARFCN and cell. The maximum number of
EARFCNs that can be prioritized is 8.
<pci> Integer type. The physical cell ID. Range: 0– 503.
<numofEARFCN> Integer type. The number of EARFCNs prioritized. Range: 1 – 8.
<err> Error code. See Chapter 15 for details.

#### AT+QNBPARA Query Timing Advance Value

```
Test Command
AT+QNBPARA=?
```
```
Response
+QNBPARA: "TA",(list of supported <TAvalue>s)
```
```
OK
Read Command
AT+QNBPARA?
```
```
Response
+QNBPARA: "TA",<TAvalue>
```
```
OK
Write Command
AT+QNBPARA="TA"
```
```
Response
+QNBPARA: "TA",<TAvalue>
```
```
OK
```
##### NOTE


#### Parameter

#### Example

##### AT+QNBPARA=?

##### +QNBPARA: "TA",(- 1 - 1282)

##### OK

##### AT+QNBPARA?

##### +QNBPARA: "TA",0

##### OK

##### AT+QNBPARA="TA"

##### +QNBPARA: "TA",0

##### OK

### 7.9. AT+QPLMNS Search PLMN

The Write Command starts searching PLMN when UE is out of service. If UE is in service status, the
command returns +CME ERROR: <err>.

The Read Command returns the current PLMN search status and the remaining time of PLMN search
timer.

```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
Characteristics /
```
<TAvalue> Integer type.

- 1 RRC is not connected
0 - 1282 Value of Timing Advance
<err> Integer type. Error code. See Chapter 15 for details.

#### AT+QPLMNS Search PLMN

```
Test Command
AT+QPLMNS=?
```
```
Response
OK
```

#### Parameter

### 7.10. AT+QRHPLMNS Enable or Disable HPLMN and Higher Priority PLMN Searching

This command enables or disables HPLMN and Higher Priority PLMN searching.

```
Read Command
AT+QPLMNS?
```
```
Response
+QPLMNS: <state>[,<OOS_time_step>]
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Execution Command
AT+QPLMNS
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
Characteristics /
```
<state> Integer type. PLMN status in NAS.
0 PLMN searching is inactivated. PLMN is not searched
1 PLMN is being searched
2 PLMN is selected
3 UE is in OOS status. The PLMN search timer is started
<OOS_time_step> Integer type. Remaining time of PLMN search timer. Unit: second. Only valid
when <state>= 3.
<err> Integer type. Error code. See Chapter 15 for details.

#### AT+QRHPLMNS Enable or Disable HPLMN and Higher Priority PLMN Searching

```
Test Command
AT+QRHPLMNS=?
```
```
Response
+QRHPLMNS: (list of supported <overrideLrplmnsi>s),(list of
supported <HPPlmnSearch>s)
```

#### Parameter

#### Example

##### AT+QRHPLMNS=1,1

##### OK

##### AT+QRHPLMNS?

##### +QRHPLMNS: 1,1

##### OK

##### OK

```
Read Command
AT+QRHPLMNS?
```
```
Response
+QRHPLMNS: <overrideLrplmnsi>,<HPPlmnSearch>
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Write Command
AT+QRHPLMNS=<overrideLrplmns
i>,<HPPlmnSearch>
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect after reboot.
Remains valid after deep-sleep wakeup.
The configurations are automatically saved to NVRAM.
```
```
<overrideLrplmnsi> Integer type. Enable/disable overriding Lrplmnsi file.
0 Disable
1 Enable. UE will not attempt to register on the HPLMN at switch-on or
recovery from out-of-coverage
<HPPlmnSearch> Integer type. Enable/disable higher priority PLMN searching.
0 Disable
1 Enable
<err> Integer type. Error code. See Chapter 15 for details.
```

### 7.11. AT+QLAPI Enable or Disable the NAS Low Access Priority Indicator

This command configures or queries the low access priority indicator in device properties. Only when
there is no EFNASCONFIG on the USIM card will the command take effect.

#### Parameter

#### AT+QLAPI Enable or Disable the NAS Low Access Priority Indicator

```
Test Command
AT+QLAPI=?
```
```
Response
+QLAPI: (list of supported <Lapi>s)
```
```
OK
Read Command
AT+QLAPI?
```
```
Response
+QLAPI: <Lapi>
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Write Command
AT+QLAPI=<Lapi>
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect after the module is rebooted.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM automatically.
```
```
<Lapi> Integer type.
0 Disable
1 Enable
```

#### Example

##### AT+QLAPI=0

##### OK

This command can only be used when the inserted USIM card belongs to KT carrier.

### 7.12. AT+QLEDMODE Set NETLIGHT Mode................................................................................

This command configures or queries NETLIGHT LED mode.

#### AT+QLEDMODE Set NETLIGHT Mode

```
Test Command
AT+QLEDMODE=?
```
```
Response
+QLEDMODE: (list of supported <LED_mode>s)
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Read Command
AT+QLEDMODE?
```
```
Response
+QLEDMODE: <LED_mode>
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Write Command
AT+QLEDMODE=<LED_mode>
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
##### NOTE


#### Parameter

If the NETLIGHT level is always low (LED OFF), then the module is not working or in Idle/PSM state.

#### Example

##### AT+QLEDMODE=1

##### OK

##### AT+QLEDMODE?

##### +QLEDMODE: 1

##### OK

##### AT+QLEDMODE=?

##### +QLEDMODE: (0,1)

##### OK

### 7.13. AT+QIPERF Throughput Test

This command is used for throughput test.

```
Characteristics
```
```
This command takes effect after the module is rebooted.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM automatically.
```
<LED_mode> Integer type. NETLIGHT LED indicator mode.
0 Disable NETLIGHT LED function. NETLIGHT pin outputs low level
1 Enable NETLIGHT LED function. NETLIGHT pin outputs PWM signals. The
different duration of low level and high level indicates different network status
Network Status High Level Duration Low Level Duration
Network Searching 64 ms 800 ms
Connecting 64 ms 2000 ms
<err> Error code. See Chapter 15 for details.

#### AT+QIPERF Throughput Test

Test Command
AT+QIPERF=?

```
Response
+QIPERF: (range of supported <action>s),(list of supported
<protcol>s),(range of supported <port>s),<ipaddr>,(range
```
##### NOTE


#### Parameter

```
of supported <tpt>s),(range of supported
<payload_size>s),(range of supported
<pkg_num>s),(range of supported <duration>s),(range of
supported <report_interval>s)
```
OK
Write Command
AT+QIPERF=<action>[,<protocol>[,<p
ort>[,<ipaddr>[,<tpt>[,payload_size[,<p
acket_number>[,<duration>[,<report_i
nterval>]]]]]]]]

```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
```
Maximum Response Time 5 s

Characteristics /

<action> Integer type. IPERF command.
0 Terminate all IPERF services
1 Start IPERF client
2 Stop IPERF client
3 Start IPERF server
4 Start IPERF UDP NAT server. In this mode, UE sends a UDP packet to
the remote server to set a UDP connection. Then the UE waits to receive DL
UDP packets and starts the DL UDP IPERF server
5 Stop IPERF server
<protocol> Integer type. Protocol type.
0 UDP
1 TCP
<port> Integer type. UDP/TCP port number. Range: 1– 65535. Default value: 5001.
If <action>=1/4, <port> represents target server port number
If <action>=3, <port> represents local IPERF server port number
<ipaddr> Integer type. IP address.
If <action>=1/4, <ipaddr> is mandatory and indicates the target server address.
If <action>=3 and the test domain is IPv6, <ipaddr> is mandatory, and it shall be
the local IPv6 address of UE.
<tpt> Integer type. Throughput. Range: 1– 1200000. Default value: 20000. Unit: bps.
<payload_size> Integer type. The payload size of UL UDP/TCP IPERF packets, used in client
mode. Range: 36–1472. Default value: 1350. Unit: byte.
<packet_number> Integer type. In client mode, it indicates the number of packets sent by UE.
Range: 1–65000. Default value: 100.


1. When the service from IPERF client completes (terminate/expires), UE sends this URC:
+QIPERF: Client END, pkg sent total bytes: <bytes>, average UL through put: <tpt> bps.
2. When the service from IPERF server completes (terminate/expires), UE sends this URC:
+QIPERF: Server END, pkg recv total bytes: <bytes>, average DL through put: <tpt> bps.
3. If an error disrupts the IPERF service, UE sends the following URC:
+QIPERF: Client FAIL, <err>; or +QIPERF: Server FAIL, <err>.

#### Example

##### AT+QIPERF=1,0,5001,"180.101.147.115",10000

##### OK

+QIPERF: Client SUCC, pkg sent bytes: 15158, UL through put: 12126 bps

+QIPERF: Client SUCC, pkg sent bytes: 12402, UL through put: 9921 bps

+QIPERF: Client SUCC, pkg sent bytes: 12402, UL through put: 9921 bps

+QIPERF: Client SUCC, pkg sent bytes: 13780, UL through put: 11024 bps

+QIPERF: Client SUCC, pkg sent bytes: 12402, UL through put: 9921 bps
AT+QIPERF=0
OK

+QIPERF: Client END, pkg sent total bytes: 74412, average UL through put: 10263 bps
AT+QIPERF=?
+QIPERF: (0-5),(0,1),(1-65535),<ipaddr>,(1-1200000),(36-1472),(1-65000),(1-65000),(1-65000)

OK

<duration> Integer type. IPERF service duration. If it is not specified, IPERF will not end until
error occurs or the termination command is received. Range: 1 – 65000. Unit:
second.
<report_interval> Integer type. IPERF's internal service results report. Unit: second. Default value:
10. The following URCs will be provided periodically within the interval. Range:
1 – 65000.
If <action>=1, UE sends URC +QIPERF: Client SUCC, pkg sent
bytes:<bytes>, UL through put: <tpt> bps
If <action>=3/4, UE sends URC +QIPERF: Server SUCC, pkg sent
bytes:<bytes>, UL through put: <tpt> bps
<err> Error code. See Chapter 15 for details.

##### NOTE


### 7.14. AT+QBANDSCAN Speed Up First Roaming Search

This command configures the speed up first roaming search function.

#### Parameter

#### AT+QBANDSCAN Speed Up First Roaming Search

```
Test Command
AT+QBANDSCAN=?
```
```
Response
+QBANDSCAN: (list of supported <scan_mode>s)
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Read Command
AT+QBANDSCAN?
```
```
Response
+QBANDSCAN: <scan_mode>
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Write Command
AT+QBANDSCAN=<scan_mode>
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
This command takes effect after the module is rebooted.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM automatically.
```
<scan_mode> Integer type. Enable/disable the speed up first roaming search function.
0 Disable
The default configuration is the original network search strategy: the band scan
will start when the module fails to find a suitable cell in the EARFCN list scan and
score list scan phase.


#### Example

##### AT+QBANDSCAN=1

##### OK

##### AT+QBANDSCAN?

##### +QBANDSCAN: 1

##### OK

##### AT+QBANDSCAN=?

##### +QBANDSCAN: (0,1)

##### OK

### 7.15. +RECVNONIP Incoming Downlink Non-IP Data

This is an unsolicited code message which indicates incoming downlink non-IP data.

#### Parameter

1 Enable
After completing the EARFCN list scan and score list scan, if the requested
PLMN or its equivalent PLMN is not found, skip the band scan, and then VPLMN
will be chosen and camping will be initiated.
<err> Error code. See Chapter 15 for details.

#### +RECVNONIP: Incoming Downlink Non-IP Data

```
+RECVNONIP: <cid>,<data_length>,<
data>
Notify the incoming of downlink non-IP data.
```
<cid> Integer type. Specifies a particular PDP context. Range: 0–10.
<data_length> Integer type. Indicates the number of octets of the <cpdata> information element.
<data> String octets. Data received.
<err> Error code. See Chapter 15 for details.


## 8 USIM Related Commands

### 8.1. AT+CCHO Open Logical Channel

This command causes the MT to return <sessionid> to allow the TE to identify a channel that is being
allocated by the currently selected UICC, which is attached to ME. The currently selected UICC opens a
new logical channel; select the application identified by the <dfname> received with this command and
return a session Id as the response. The ME restricts the communication between the TE and the UICC to
this logical channel.

This <sessionid> is to be used when sending commands with Restricted UICC Logical Channel access
AT+CRLA or Generic UICC Logical Channel access AT+CGLA.

#### Parameter

#### AT+CCHO Open Logical Channel

```
Test Command
AT+CCHO=?
```
```
Response
OK
Write Command
AT+CCHO=<dfname>
```
```
Response
<sessionid>
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
Characteristics /
```
<dfname> String type. DF name. All selectable applications in the UICC are referenced by a DF
name coded on 1 to 16 bytes.
<sessionid> Integer type. Session ID to be used in order to target a specific application on the
smart card (e.g. USIM) using logical channels mechanism.
<err> Error code. See Chapter 15 for details.


#### Example

##### AT+CCHO="A00000004374506173732E496F54"

##### 1

##### OK

### 8.2. AT+CCHC Close Logical Channel

This command asks the ME to close a communication session with the active UICC. The ME shall close
the previously opened logical channel. The TE no longer be able to send commands on this logical
channel.

#### Parameter

#### Example

##### AT+CCHC=1

##### +CCHC

##### OK

#### AT+CCHC Close Logical Channel

```
Test Command
AT+CCHC=?
```
```
Response
OK
Write Command
AT+CCHC=<sessionid>
```
```
Response
+CCHC
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
Characteristics /
```
<sessionid> Integer type. Session ID to be used in order to target a specific application on the
smart card (e.g. USIM) using logical channels mechanism.
<err> Error code. See Chapter 15 for details.


### 8.3. AT+CGLA Generic UICC Logical Channel Access

This Write Command transmits to the MT the <command> it then shall send as it is to the selected UICC.
In the same manner the UICC <response> shall be sent back by the MT to the TA as it is.

This command allows a direct control of the currently selected UICC by a distant application on the TE.
The TE then shall take care of processing UICC information within the frame specified by GSM/UMTS.

Although the command allows TE to take control over the UICC-MT interface, there are some functions of
the UICC-MT interface that logically do not need to be accessed from outside the TA/MT.

#### Parameter

#### AT+CGLA Generic UICC Logical Channel Access

```
Test Command
AT+CGLA=?
```
```
Response
OK
Write Command
AT+CGLA=<sessionid>,<length>,<co
mmand>
```
```
Response
+CGLA: <length>,<response>
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
Characteristics /
```
<sessionid> Integer type. The identifier of the session to be used in order to send the APDU
commands to the UICC. It is mandatory to send commands to the UICC when
targeting applications on the smart card using a logical channel other than the default
channel (channel "0").
<length> Integer type. Length of the characters that are sent to TE in <command> or
<response> (two times the actual length of the command or response).
<command> String type in hex format. Command passed on by the MT to the UICC. For details,
see 3GPP TS 31.101.
<response> String type in hex format. Response to the command passed on by the UICC to the
MT. For details, see 3GPP TS 31.101.
<err> Error code. See Chapter 15 for details.


### 8.4. AT+CIMI Request International Mobile Subscriber Identity

This command returns International Mobile Subscriber Identity (a string without double quotes).

This Execution Command causes the TA to return <IMSI>, which is intended to permit the TE to identify
the USIM which is attached to MT.

#### Parameter

#### Example

##### AT+CIMI

##### 460001357924680

##### OK

### 8.5. AT+CLCK Facility Lock

This command locks/unlocks or interrogates a MT or a network facility <fac>. A password is normally
needed to do such actions. When querying the status of a network service (<mode>=2) the response line
for 'not active' case (<status>=0) should be returned only if the service is not active for any <class>. This

#### AT+CIMI Request International Mobile Subscriber Identity

```
Test Command
AT+CIMI=?
```
```
Response
OK
Execution Command
AT+CIMI
```
```
Response
<IMSI>
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
Characteristics /
```
```
<IMSI> String type without double quotes. International Mobile Subscriber Identity.
<err> Error code. See Chapter 15 for details.
```

command should be abortable when network facilities are set or interrogated.

This Test Command returns facility values supported as a compound value.

#### Parameter

#### AT+CLCK Facility Lock

```
Test Command
AT+CLCK=?
```
```
Response
+CLCK: (list of supported <fac>s)
```
```
OK
Write Command
AT+CLCK=<fac>,<mode>[,<passwd>[
,<class>]]
```
```
Response
when <mode>=0 or 1 and the command is executed
successfully:
OK
```
```
when <mode>=2 and the command is executed successfully:
+CLCK: <status>[,<class>]
[+CLCK: <status>,<class>
[...]]
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect after the module is rebooted.
Remain valid after deep-sleep wakeup.
The configurations are saved to NVRAM automatically.
```
```
<fac> String type. Network facility.
"SC" SIM (lock USIM card installed in the currently selected card slot) (USIM
asks password in MT power-up and when this lock command is issued)
<mode> Integer type. Lock operation.
0 Unlock
1 Lock
2 Query status
<passwd> String type. It shall be the same as the password specified for the facility from the MT
user interface or as the password set with AT+CPWD.
<class> Integer type. Sum of integers each representing a class of information.
1 Voice (telephony)
```

#### Example

##### AT+CLCK="SC",2

##### +CLCK: 0

##### OK

### 8.6. AT+CPIN Enter PIN

This Write Command sends to the MT a password which is necessary before it can be operated (SIM PIN,
SIM PUK, PH SIM PIN, etc.). If the PIN is to be entered twice, the TA shall automatically repeat the PIN. If
no PIN request is pending, no action is taken towards MT and an error message, +CME ERROR, is
returned to TE. If the PIN required is SIM PUK, the second pin is required. This second pin, <newpin>, is
used to replace the old pin in the SIM.

```
2 Data (refers to all bearer services; with <mode>=2 this may refer only to some
bearer service if TA does not support values 16, 32, 64 and 128)
4 Fax (facsimile services)
8 Short message service
16 Data circuit sync
32 Data circuit async
64 Dedicated packet access
128 Dedicated PAD access
<status> Integer type. Status of facility.
0 Not active
1 Active
<err> Error code. See Chapter 15 for details.
```
#### AT+CPIN Enter PIN

```
Test Command
AT+CPIN=?
```
```
Response
OK
Read Command
AT+CPIN?
```
```
Response
+CPIN: <code>
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Write Command Response
```

#### Parameter

#### Example

##### AT+CPIN?

##### +CPIN: READY

##### OK

### 8.7. AT+CPINR Remaining PIN Retries

This command causes the MT to return the number of remaining PIN retries for the MT passwords with
intermediate result code +CPINR: <code>,<retries>[,<default_retries>].

When the command is issued without the optional parameter <sel_code>, intermediate result codes are
returned for all <code>s. In the intermediate result codes, <default_retries> is an optional parameter, per
<code>.

```
AT+CPIN=<pin>[,<newpin>][,<newpin
>]
```
##### OK

```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect immediately.
Whether the configurations are saved to the USIM card
depends on the USIM card in use.
The configuration is not saved to NVRAM.
```
```
<code> String type. Type of password required.
READY No further entry needed
SIM PIN MT is waiting for USIM PIN
SIM PUK MT is waiting for USIM PUK
<pin> String type. Password.
<newpin> String type. If the PIN required is "SIM PUK", it is the new password.
<err> Error code. See Chapter 15 for details.
```
#### AT+CPINR Remaining PIN Retries

```
Test Command Response
```

#### Parameter

#### Example

##### AT+CPINR

##### +CPINR: "SIM PIN",3,3

##### +CPINR: "SIM PUK",10,10

##### OK

##### AT+CPINR=? OK

```
Write/Execution Command
AT+CPINR[=<sel_code>]
```
```
Response
[+CPINR: <code>,<retries>[,<default_retries>]]
[+CPINR: <code>,<retries>[,<default_retries>]]
[...]
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
Characteristics /
```
```
<sel_code> String type. Selected type of PIN.
"SIM PIN"
"SIM PUK"
<retries> Integer type. Number of remaining retries per PIN.
<default_retries> Integer type. Number of default retries per PIN.
<code> String type. Type of PIN. All values listed under the description of <code> in
AT+CPIN, except "READY".
<err> Error code. See Chapter 15 for details.
```

### 8.8. AT+CPWD Change Password

This command sets a new password for the facility lock function defined by AT+CLCK.

This Test Command returns a list of pairs which present the available facilities and the maximum length of
their passwords.

#### Parameter

#### AT+CPWD Change Password

```
Test Command
AT+CPWD=?
```
```
Response
+CPWD: (list of supported <fac>,<pwdlength>s)
```
```
OK
Write Command
AT+CPWD=<fac>,<oldpwd>,<newpw
d>
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect immediately.
Whether the configurations are saved to the USIM card
depends on the USIM card in use.
The configurations are not saved to NVRAM.
```
```
<fac> String type. Network facility.
"SC" SIM (lock USIM card installed in the currently selected card slot)
(USIM asks password on MT power-up and when this lock command
is issued)
<oldpwd>,<newpwd> String type. Old password/new password. The maximum length of password
can be determined with <pwdlength>.
Old password <oldpwd> shall be the same as the password specified for the
facility from the MT user interface or with that set in AT+CPWD.
<newpwd> is the new password.
<pwdlength> Integer type. The maximum length of the password for the facility. Unit: Byte.
<err> Error code. See Chapter 15 for details.
```

### 8.9. AT+CRSM Restricted USIM Access

This command provides easy but limited access to the USIM database. It transmits the USIM
<command> and its required parameters.

#### Parameter

#### AT+CRSM Restricted USIM Access

```
Test Command
AT+CRSM=?
```
```
Response
OK
Write Command
AT+CRSM=<command>[,<fileID>[,<P1>,<P2>,<
P3>[,<data>][,<pathID>]]]
```
```
Response
+CRSM: <sw1>,<sw2>[,<response>]
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect immediately.
Whether the configurations are saved to the USIM
card depends on the USIM card in use.
The configurations are not saved to NVRAM.
```
```
<command> Integer type. Command passed on by the MT to the USIM.
176 READ BINARY
178 READ RECORD
192 GET RESPONSE
214 UPDATE BINARY
220 UPDATE RECORD
242 STATUS
<fileID> Integer type. The identifier of an elementary data file on USIM. Mandatory for
every command except STATUS.
<P1>,<P2>,<P3> Integer type. Parameters passed on by the MT to the USIM. These parameters
are mandatory for every command, except GET RESPONSE and STATUS. The
values are described in 3GPP TS 51.011.
<data> String type. Information (in hexadecimal format) which shall be written to the
USIM.
<pathlD> String type. It contains the path of an elementary file on the UICC in hexadecimal
format.
<sw1>,<sw2> Integer type. Information from the USIM about the actual command execution
```

#### Example

##### AT+CRSM=176,28512,0,0,0

##### +CRSM: 144,0,"FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFF

##### F0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000FFF

##### FFF0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000F

##### FFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF000

##### 0FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0

##### 000FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFF

##### F0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000FFFFFF0000FF"

##### OK

1. If the USIM card is not allowed to hibernate, the whole system cannot enter the hibernation mode,
    and thus the module’s power consumption will not be reduced.
2. It is needed to execute AT+QSIMSLEEP to disable USIM hibernation before executing
    AT+CRSM/AT+CSIM.

```
result. These parameters are delivered to the TE in both cases of successful or
failed execution of the command.
<response> String type. Response of a successful completion of the command
previously issued in hexadecimal format. STATUS and GET RESPONSE return
data, which gives information about the current elementary data field. This
information includes the type of file and its size (see 3GPP TS
51.011/102.221/31.102). After READ BINARY or READ RECORD command the
requested data will be returned. <response> is not returned after a successful
UPDATE BINARY or UPDATE RECORD command.
<err> Error code. See Chapter 15 for details.
```
##### NOTE


### 8.10. AT+CSIM Generic USIM Access

This Write Command transmits to the MT the <command> it then shall send as it is to the USIM. In the
same manner, the USIM <response> shall be sent back by the MT to the TA as it is.

This command allows a direct control of the USIM that is installed in the selected card slot, by a distant
application on the TE. The TE shall then take care of processing USIM information within the frame
specified by GSM/UMTS.

#### Parameter

1. If the USIM card is not allowed to hibernate, the whole system cannot enter the hibernation mode,
    and thus the module’s power consumption will not be reduced.
2. It is needed to execute AT+QSIMSLEEP to disable USIM hibernation before executing AT+CRSM or
    AT+CSIM.

#### AT+CSIM Generic USIM Access

```
Write Command
AT+CSIM=<length>,<command>
```
```
Response
+CSIM: <length>,<response>
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect immediately.
Whether the configurations are saved to the USIM card
depends on the USIM card in use.
The configurations are not saved to NVRAM.
```
<length> Integer type. Length of the characters that are sent to TE in <command> or
<response> (two times the actual length of the command or response).
<command> String type in hexadecimal format. Command passed on by the MT to the USIM card.
For details, see 3GPP TS 51.011.
<response> String type in hexadecimal format. Response to the command passed on by the USIM
card to the MT.
<err> Error code. See Chapter 15 for details.

##### NOTE


### 8.11. AT+QCCID USIM Card Identification

This command reads ICCID of the USIM card. If no USIM card is present, or the USIM card is unreadable,
no data will be returned.

#### Parameter

#### Example

##### AT+QCCID

##### +QCCID: 898 60446091891372008

##### OK

### 8.12. AT+QSIMPOLL USIM Card Polling.......................................................................................

This command enables or disables the polling of USIM card. If USIM card polling is enabled, the module
detects USIM card periodically and sends status to get USIM card status. If USIM card polling is disabled,
UE interacts with USIM card only in the situation that the card is required, and tries to temporarily store
some information to avoid unnecessarily frequent interactions so as to lower the power consumption.

#### AT+QCCID USIM Card Identification

```
Execution Command
AT+QCCID
```
```
Response
+QCCID: <ICCID>
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
Characteristics /
```
<ICCID> String type. USIM card identification number (integrated circuit card identity).

#### AT+QSIMPOLL USIM Card Polling

```
Test Command Response
```

#### Parameter

#### Example

##### AT+QSIMPOLL=?

##### +QSIMPOLL: (0,1)

##### OK

##### AT+QSIMPOLL=1

##### OK

##### AT+QSIMPOLL?

##### +QSIMPOLL: 1

##### OK

```
The module cannot detect USIM card when the card is powered off even if USIM card polling is enabled,
and the polling timer will be discarded in such case.
```
```
AT+QSIMPOLL=? +QSIMPOLL: (list of supported <mode>s)
```
```
OK
Read Command
AT+QSIMPOLL?
```
```
Response
+QSIMPOLL: <mode>
```
```
OK
Write Command
AT+QSIMPOLL=<mode>
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect immediately.
Remain valid after deep-sleep wakeup.
The configurations is saved to NVRAM automatically.
```
<mode> Integer type. Enable/disable USIM card polling.
0 Disable
1 Enable

##### NOTE


### 8.13. AT+QSIMSLEEP USIM Sleep Control

```
This command configures whether to allow USIM card to sleep. When USIM card is not allowed to sleep,
USIM card will prevent the whole system from going to sleep. In this case, the power consumption of the
module will increase. Therefore, it is recommended to enable USIM card sleep when using the module.
```
#### Parameter

#### AT+QSIMSLEEP USIM Sleep Control

```
Test Command
AT+QSIMSLEEP=?
```
```
Response
+QSIMSLEEP: (list of supported <mode>s)
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Read Command
AT+QSIMSLEEP?
```
```
Response
+QSIMSLEEP: <mode>
```
```
OK
Write Command
AT+QSIMSLEEP=<mode>
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect immediately.
Remain valid after deep-sleep wakeup.
The configurations is not saved to NVRAM automatically.
```
<mode> Integer type.
0 Disable USIM card sleep
1 Enable USIM card sleep


1. When USIM card sleep is disabled, the whole module cannot enter sleep mode, resulting in the
    increase of power consumption.
2. Before AT+CRSM or AT+CSIM is executed, it is necessary to execute this command to disable USIM
    card sleep.

#### Example

##### AT+QSIMSLEEP?

##### +QSIMSLEEP: 1

##### OK

##### NOTE


## 9 Power Consumption Commands

### 9.1. AT+CEDRXS eDRX Setting

This Write Command controls the setting of the UE’s eDRX parameters. It controls whether the UE wants
to apply eDRX or not, as well as the requested eDRX value for each specified type of access technology.

This Write Command also controls the presentation of an unsolicited result code +CEDRXP:
<AcT_type>[,<requested_eDRX_value>[,<NW_provided_eDRX_value>[,<paging_time_window>]]]
when <mode>=2 and there is a change in the eDRX parameters provided by the network.

A special form of the command can be given as AT+CEDRXS=3. In this form, eDRX will be disabled and
data for all parameters in AT+CEDRXS will be removed or, if available, set to the default values.

This Read Command returns the current settings for each defined value of <AcT_type>.

This Test Command returns the supported <mode>s and the value ranges for the access technology and
the requested eDRX value as a compound value.

#### AT+CEDRXS eDRX Setting

```
Test Command
AT+CEDRXS=?
```
```
Response
+CEDRXS: (range of supported <mode>s),(list of supported
<AcT_type>s),(range of supported <requested_eDRX_valu
e>s)
```
```
OK
Read Command
AT+CEDRXS?
```
```
Response
+CEDRXS: <AcT_type>,<requested_eDRX_value>
```
```
OK
Write Command
AT+CEDRXS=<mode>[,<AcT_type
>[,<requested_eDRX_value>]]
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
```

#### Parameter

```
+CME ERROR: <err>
```
```
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect immediately.
Remain valid after deep-sleep wakeup.
The configurations are saved to NVRAM automatically.
```
```
<mode> Integer type. Disable or enable the use of eDRX in the UE. This
parameter is applicable to all specified types of access
technologies, i.e. the most recent setting of <mode> takes effect for
all specified values of <AcT_type>.
0 Disable the use of eDRX
1 Enable the use of eDRX
2 Enable the use of eDRX and enable URC +CEDRXP: <A
cT_type>[,<requested_eDRX_value>[, <NW_provided_eDR
X_value>[,<paging_time_window>]]]
3 Disable the use of eDRX and discard all parameters for eDRX
or, if available, reset to default values
<AcT_type> Integer type. The type of access technology. AT+CEDRXS?
specifies the relationship between the type of access technology
and the requested eDRX value.
5 E-UTRAN (NB-S1 mode)
<requested_eDRX_value> String type. Half a byte in a 4-bit format. NB-S1 mode.
Bits
4 3 2 1 E-UTRAN eDRX cycle length duration
0 0 1 0 20.48 seconds
0 0 1 1 40.96 seconds
0 1 0 1 81.92 seconds
1 0 0 1 163.84 seconds
1 0 1 0 327.68 seconds
1 0 1 1 655.36 seconds
1 1 0 0 1310.72 seconds
1 1 0 1 2621.44 seconds
1 1 1 0 5242.88 seconds
1 1 1 1 10485.76 seconds
<NW_provided_eDRX_value> String type. Half a byte in a 4-bit format. NB-S1 mode.
Bits
4 3 2 1 E-UTRAN eDRX cycle length duration
0 0 1 0 20.48 seconds
0 0 1 1 40.96 seconds
0 1 0 1 81.92 seconds
```

#### Example

##### AT+CEDRXS=1,5,"0101"

##### OK

##### AT+CEDRXS?

##### +CEDRXS: 5,"0 011 "

##### OK

##### AT+CEDRXS=?

##### +CEDRXS: (0-3),(5),("0000"-"1111")

##### OK

```
1 0 0 1 163.84 seconds
1 0 1 0 327.68 seconds
1 0 1 1 655.36 seconds
1 1 0 0 1310.72 seconds
1 1 0 1 2 621.44 seconds
1 1 1 0 5242.88 seconds
1 1 1 1 10485.76 seconds
<paging_time_window> String type. Half a byte in a 4-bit format. NB-S1 mode.
Bits
4 3 2 1 Paging Time Window length
0 0 0 0 2.56 seconds
0 0 0 1 5.12 seconds
0 0 1 0 7.68 seconds
0 0 1 1 10 .24 seconds
0 1 0 0 12.8 seconds
0 1 0 1 15.36 seconds
0 1 1 0 17.92 seconds
0 1 1 1 20.48 seconds
1 0 0 0 23.04 seconds
1 0 0 1 25.6 seconds
1 0 1 0 28.16 seconds
1 0 1 1 30.72 seconds
1 1 0 0 33.28 seconds
1 1 0 1 35.84 seconds
1 1 1 0 38.4 seconds
1 1 1 1 40.96 seconds
<err> Error code. See Chapter 15 for details.
```

### 9.2. AT+CEDRXRDP eDRX Read Dynamic Parameters

This Execution Command returns the values of <AcT_type>, <requested_eDRX_value>,
<NW_provided_eDRX_value> and <paging_time_window> if eDRX is used for the cell that the MS is
currently registered to.

If the cell to which the MS is currently registered is not using eDRX, <AcT_type>=0 is returned.

#### Parameter

#### AT+CEDRXRDP eDRX Read Dynamic Parameters

```
Test Command
AT+CEDRXRDP=?
```
```
Response
OK
Execution Command
AT+CEDRXRDP
```
```
Response
+CEDRXRDP: <AcT_type>[,<requested_eDRX_value>[,<
NW_provided_eDRX_value>[,<paging_time_window>]]]
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
Characteristics /
```
```
<AcT_type> Integer type. The type of access technology. AT+CEDRXS?
specifies the relationship between the type of access technology
and the requested eDRX value.
0 Access technology not supporting eDRX.
5 E-UTRAN (NB-S1 mode)
<requested_eDRX_value> String type. Half a byte in a 4-bit format.
Bits
4 3 2 1 E-UTRAN eDRX cycle length duration
0 0 1 0 20.48 seconds
0 0 1 1 40.96 seconds
0 1 0 1 8 1.92 seconds
1 0 0 1 163.84 seconds
1 0 1 0 327.68 seconds
1 0 1 1 655.36 seconds
1 1 0 0 1310.72 seconds
```

#### Example

##### AT+CEDRXRDP

##### +CEDRXRDP: 5,"0011","0011","0011"

##### OK

##### AT+CEDRXRDP=?

```
1 1 0 1 2621.44 seconds
1 1 1 0 5242.88 seconds
1 1 1 1 10485.76 seconds
<NW_provided_eDRX_value> String type. Half a byte in a 4-bit format.
Bits
4 3 2 1 E-UTRAN eDRX cycle length duration
0 0 1 0 20.48 seconds
0 0 1 1 40.96 seconds
0 1 0 1 81.92 seconds
1 0 0 1 163.84 seconds
1 0 1 0 327.68 seconds
1 0 1 1 655.36 seconds
1 1 0 0 1310.72 seconds
1 1 0 1 2621.44 seconds
1 1 1 0 5242.88 seconds
1 1 1 1 10485.76 seconds
<paging_time_window> String type. Half a byte in a 4-bit format.
Bits
4 3 2 1 Paging Time Window length
0 0 0 0 2.56 seconds
0 0 0 1 5.12 seconds
0 0 1 0 7.68 seconds
0 0 1 1 10.24 seconds
0 1 0 0 12.8 seconds
0 1 0 1 15.36 seconds
0 1 1 0 17.92 seconds
0 1 1 1 20.48 seconds
1 0 0 0 23.04 seconds
1 0 0 1 25.6 seconds
1 0 1 0 28.16 seconds
1 0 1 1 30.72 seconds
1 1 0 0 33.28 seconds
1 1 0 1 35.84 seconds
1 1 1 0 38.4 seconds
1 1 1 1 40.96 seconds
<err> Error code. See Chapter 15 for details.
```

##### OK

### 9.3. AT+CFUN Set UE Functionality

The Write Command selects the level of functionality in the MT. "full functionality" level consumes the
highest amount of power, while the "minimum functionality" level consumes the minimum power.

The Read Command returns the current setting of <fun>.

The Test Command returns values supported by the MT as a compound value.

#### Parameter

#### AT+CFUN Set UE Functionality

```
Test Command
AT+CFUN=?
```
```
Response
+CFUN: (list of supported <fun>s),(list of supported <rst>s)
```
```
OK
Read Command
AT+CFUN?
```
```
Response
+CFUN: <fun>
```
```
OK
Write Command
AT+CFUN=<fun>[,<rst>]
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 25 s, determined by network.
Characteristics See parameters description.
```
```
<fun> Integer type. UE functionality level.
0 Minimum functionality
1 Full functionality
4 Disable RF transmitting and receiving
<rst> Integer type. UE resetting.
0 No reset required for setting the UE to a functionality level.
1 Reset required for setting the UE to a functionality level.
<err> Integer type. Error code. See Chapter 15 for details.
```

#### Example

##### AT+CFUN=?

##### +CFUN: (0,1,4,),(0,1)

##### OK

##### AT+CFUN=1

##### OK

##### AT+CFUN?

##### +CFUN: 1

##### OK

##### AT+CFUN=0, 1

##### OK

##### RDY

##### AT+CFUN?

##### +CFUN: 0

##### OK

### 9.4. AT+CPSMS Power Saving Mode Setting

This Write Command controls the setting of the UE's power saving mode (PSM) parameters. It controls
whether the UE wants to apply PSM or not, as well as the requested extended periodic TAU value in
E-UTRAN and the requested Active Time value. See the unsolicited result codes provided by AT+CEREG
for the Active Time value and the extended periodic TAU value allocated to the UE by the network in
E-UTRAN.

A special form of the command can be given as AT+CPSMS=2. In this form the use of PSM will be
disabled and data for all parameters in AT+CPSMS will be removed or, if available, set to the default
values.

This Read Command returns the current parameter values.

This Test Command returns the supported <mode>s and the value ranges for the requested extended
periodic TAU value in E-UTRAN and the requested Active Time value as a compound value.

#### AT+CPSMS Power Saving Mode Setting

```
Test Command
AT+CPSMS=?
```
```
Response
+CPSMS: (range of supported <mode>s),,,(range of
supported <requested_periodic_TAU>s),(range of
```

#### Parameter

```
supported <requested_active_time>s)
```
```
OK
Read Command
AT+CPSMS?
```
```
Response
+CPSMS: <mode>,,,<requested_periodic_TAU>,<request
ed_active_time>
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Write Command
AT+CPSMS=<mode>[,,,<requested_p
eriodic_TAU>[,<requested_active_ti
me>]]
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect immediately.
Remain valid after deep-sleep wakeup.
The configurations are saved to NVRAM automatically.
```
```
<mode> Integer type. Disable or enable the use of PSM in the UE.
0 Disable the use of PSM
1 Enable the use of PSM
2 Disable the use of PSM and discard all parameters for PSM or, if
available, reset to the default values
<requested_periodic_TAU> String type. One byte in an 8-bit format. Requested extended periodic
TAU value (T3412) to be allocated to the UE in E-UTRAN. (e.g.
"01000111" equals 70 hours).
Bits 5 to 1 represents the binary coded timer value.
Bits 8 to 6 defines the timer value unit as follows:
Bits
8 7 6
0 0 0 value is incremented in multiples of 10 minutes
0 0 1 value is incremented in multiples of 1 hour
0 1 0 value is incremented in multiples of 10 hours
0 1 1 value is incremented in multiples of 2 seconds
```

1. This timer value unit is only applicable to the T3412 extended value IE. If it is received in an integrity
    protected message, the value shall be interpreted as multiples of 320 hours. Otherwise, the value
    shall be interpreted as multiples of 1 hour.
2. The timer value is not applicable to the T3412 extended value IE. If this timer value is received, the
    T3412 extended value IE shall be considered as not included in this message.

#### Example

##### AT+CPSMS=1,,," 01000011 "," 01000011 "

##### OK

##### AT+CPSMS?

##### +CPSMS: 1,,," 01000011 "," 01000011 "

##### OK

##### AT+CPSMS=?

##### +CPSMS: (0-2),,,(" 00000000 "-" 11111111 "),(" 00000000 "-" 11111111 ")

##### OK

```
1 0 0 value is incremented in multiples of 30 seconds
1 0 1 value is incremented in multiples of 1 minute
1 1 0 value is incremented in multiples of 320 hours (Note 1)
1 1 1 value indicates that the timer is deactivated (Note 2)
<requested_active_time> String type. One byte in an 8-bit format. Requested Active Time value
(T3324) to be allocated to the UE (e.g., "00100100" equals 4 minutes).
Bits 5 to 1 represent the binary coded timer value.
Bits 8 to 6 defines the timer value unit for the GPRS timer as follows:
Bits
8 7 6
0 0 0 value is incremented in multiples of 2 seconds
0 0 1 value is incremented in multiples of 1 minute
0 1 0 value is incremented in multiples of 6 minutes
1 1 1 value indicates that the timer is deactivated
<err> Error code. See Chapter 15 for details.
```
##### NOTE


### 9.5. AT+QDRX Query DRX Status

This Read Command queries the DRX status.

#### Parameter

#### AT+QDRX Query DRX Status

```
Test Command
AT+QDRX=?
```
```
Response
OK
Read Command
AT+QDRX?
```
```
Response
When the module is not in connected mode:
+QDRX: <mode>[,<drxcycle_IDLE>]
```
```
OK
```
```
When the module is in connected mode:
+QDRX: <mode>,<drxInactivityTimer>,<drxRetransmissi
onTimer>,<drxStartOffset>,<drxULRetransmissionTime
r>,<longdrxCycle>,<onDurationTimer>
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics /
```
```
<mode> Integer type. The mode of RRC connection.
1 Idle mode
2 Connected mode
3 RRC connection is neither in idle mode nor in connected mode,
e.g., PSM/Deregistered
<drxcycle_IDLE> Integer type. Indicates DRX cycle in idle mode. Unit: ms.
```
```
<drxInactivityTimer>
Integer type. Indicates the duration of the drx-InactivityTimer. Unit:
PDCCH Period. Value: 0,1,2,3,4,8,16,32. See 3GPP TS 36.321.
<drxRetransmissionTimer> Integer type. Indicates the duration of the drx-RetransmissionTimer.
Unit: PDCCH Period. See 3GPP TS 36.321.
<longdrxCycle> Integer type. Indicates the duration of the DRX cycle in connected
```

#### Example

##### AT+QDRX?

##### +QDRX: 1, 1280

##### OK

### 9.6. AT+QEDRXCFG Configure eDRX and PTW

This Write Command controls the setting of UE’s eDRX parameters. The command controls whether or
not UE applies eDRX, the requested eDRX value and requested paging time window value for each
specified type of access technology.

```
mode. Unit: sub-frame. See 3GPP TS 36.321.
<drxStartOffset> Integer type. Indicates the value of drxStartOffset, represented by the
number of sub-frames obtained by the operation of (<longdrxCycle>
/ 256). Range: 0– 255.
<drxULRetransmissionTimer> Integer type. Indicates the duration of the
drx-ULRetransmissionTimer. Unit: PDCCH period. See 3GPP TS
36.321.
<onDurationTimer> Integer type. Indicates the duration of the onDurationTimer. Unit:
PDCCH Period. See 3GPP TS 36.321.
```
#### AT+QEDRXCFG Configure eDRX and PTW

```
Test Command
AT+QEDRXCFG=?
```
```
Response
+QEDRXCFG: (range of supported <mode>s),(list of
supported <AcT_type>s),(range of supported
<requested_eDRX_value>s),(range of supported
<requested_paging_time_window_value>s)
```
```
OK
Read Command
AT+QEDRXCFG?
```
```
Response
+QEDRXCFG: <AcT_type>,<requested_eDRX_value>,<r
equested_paging_time_window_value>
```
```
OK
Write Command
AT+QEDRXCFG=<mode>[,<AcT_type
>[,<requested_eDRX_value>[,<reque
sted_paging_time_window_value>]]]
```
```
Response
OK
```
```
If there is any error:
ERROR
```

#### Parameter

```
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect immediately.
Remain valid after deep-sleep wakeup.
The configurations are saved to NVRAM automatically.
```
```
<mode> Integer type. Disable or enable the use of eDRX in the UE. This
parameter is applicable to all specified types of access technologies,
i.e. the most recent setting of <mode> will take effect for all specified
values of <AcT_type>.
0 Disable the use of eDRX
1 Enable the use of eDRX
2 Enable the use of eDRX and enable URC +CEDRXP: <AcT
_type>[,<requested_eDRX_value>[,<NW_provided_eDRX_v
alue>[,<paging_time_window>]]]
3 Disable the use of eDRX and discard all parameters for eDRX or,
if available, reset to default values
<AcT_type> Integer type. The type of access technology. AT+CEDRXS? specifies
the relationship between the type of access technology and the
requested eDRX value.
0 Access technology not supporting eDRX. This parameter value
is only used in URC
5 E-UTRAN (NB-S1 mode)
<requested_eDRX_value> String type. Half a byte in a 4-bit format. NB-S1 mode.
Bits
4 3 2 1 E-UTRAN eDRX cycle
0 0 1 0 20.48 seconds
0 0 1 1 40.96 seconds
0 1 0 1 81.92 seconds
1 0 0 1 163.84 seconds
1 0 1 0 327.68 seconds
1 0 1 1 655.36 seconds
1 1 0 0 1310.72 seconds
1 1 0 1 2621.44 seconds
1 1 1 0 5242.88 seconds
1 1 1 1 10485.76 seconds
<requested_paging_time_window_value> String type. Half a byte in a 4-bit format. NB-S1 mode.
Bits
4 3 2 1 Paging Time Window
0 0 0 0 2.56 seconds
```

0 0 0 1 5.12 seconds
0 0 1 0 7.68 seconds
0 0 1 1 10.24 seconds
0 1 0 0 12.8 seconds
0 1 0 1 15.36 seconds
0 1 1 0 17.92 seconds
0 1 1 1 20.48 seconds
1 0 0 0 23.04 seconds
1 0 0 1 25.6 seconds
1 0 1 0 28.16 seconds
1 0 1 1 30.72 seconds
1 1 0 0 33.28 seconds
1 1 0 1 35.84 seconds
1 1 1 0 38.4 seconds
1 1 1 1 40.96 seconds
<NW_provided_eDRX_value> String type. Half a byte in a 4-bit format. NB-S1 mode.
Bits
4 3 2 1 E-UTRAN eDRX cycle
0 0 1 0 20.48 seconds
0 0 1 1 40.96 seconds
0 1 0 1 81.92 seconds
1 0 0 1 163.84 seconds
1 0 1 0 327.68 seconds
1 0 1 1 655.36 seconds
1 1 0 0 1310.72 seconds
1 1 0 1 2621.44 seconds
1 1 1 0 5242.88 seconds
1 1 1 1 10485.76 seconds
<paging_time_window> String type. Half a byte in a 4-bit format. NB-S1 mode.
Bits
4 3 2 1 Paging Time Window
0 0 0 0 2.56 seconds
0 0 0 1 5.12 seconds
0 0 1 0 7.68 seconds
0 0 1 1 10.24 seconds
0 1 0 0 12.8 seconds
0 1 0 1 15.36 seconds
0 1 1 0 17.92 seconds
0 1 1 1 20.48 seconds
1 0 0 0 23.04 seconds
1 0 0 1 25.6 seconds
1 0 1 0 28.16 seconds
1 0 1 1 30.72 seconds
1 1 0 0 33.28 seconds


#### Example

##### AT+QEDRXCFG=1,5,"0101"

##### OK

##### AT+QEDRXCFG?

##### +QEDRXCFG: 5,"0011","0011"

##### OK

##### AT+QEDRXCFG=?

##### +QEDRXCFG: (0-3),(5),("0000"-"1111"),("0000"-"1111")

##### OK

### 9.7. AT+QNBIOTRAI NB-IoT Release Assistance Indication

This command sets the NB-IoT release assistance indications.

```
1 1 0 1 35.84 seconds
1 1 1 0 38.4 seconds
1 1 1 1 40.96 seconds
<err> Error code. See Chapter 15 for details.
```
#### AT+QNBIOTRAI NB-IoT Release Assistance Indication

```
Test Command
AT+QNBIOTRAI=?
```
```
Response
+QNBIOTRAI: (list of supported <rai_mode>s)
```
```
OK
Write Command
AT+QNBIOTRAI=<rai_mode>
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
Only can be set when RRC is in connected state. The
command takes effect immediately.
```

#### Parameter

### 9.8. AT+QNBIOTEVENT Enable/Disable NB-IoT Related Event Report

This command enables/disables an NB-IoT related event report.

#### Parameter

```
<rai_mode> Integer type. Specifies release assistance information.
0 TE sends a single UL data packet without the RAI mark to the network.
1 TE informs the network to release the RRC connection by sending it a single
UL packet with RAI flag.
<err> Error code. See Chapter 15 for details.
```
#### AT+QNBIOTEVENT Enable/Disable NB-IoT Related Event Report

```
Test Command
AT+QNBIOTEVENT=?
```
```
Response
OK
Read Command
AT+QNBIOTEVENT?
```
```
Response
+QNBIOTEVENT: <enable>,<event>
```
```
OK
Write Command
AT+QNBIOTEVENT=<enable>,<event>
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect immediately.
Remain valid after deep-sleep wakeup.
The configurations are saved to NVRAM automatically.
```
```
<enable> Integer type. Enable/disable a specific event report.
0 Disable the indication of the specific event
1 Enable the indication of the specific event by URC +QNBIOTEVENT:
<event_value>
<event> Integer type. The reported event.
1 PSM state
<event_value> String type. When the reported event is PSM:
```

#### Example

##### AT+QNBIOTEVENT?

##### +QNBIOTEVENT: 1,1

##### OK

### 9.9. AT+QPSMS Power Saving Mode Setting

This command sets and gets PSM related timer value in seconds. And <N_T2> is always the period TAU
timer. This is convenient for customer to use.

Whatever the timer value is, PSM will be enabled automatically upon the execution of this command. If
the requested value of T3324 or extended T3412 is not available, the module will choose the greatest
available value that is not greater than the requested one.

<T1> is the value of T3324. In Write Command, the value will be set to T3324 and requested in TAU or
ATTACH_REQUEST message. In Read Command, <N_T1> is the value of T3324 provided by the
network.

<T2> is the value of T_PTAU. In Write Command, the value will be set to extend T3412. In Read
Command, when extended T3412 is enabled, the value of <N_T2> is extended T3412; when extended
T3412 is disabled, the value is T3412.

To disable PSM, use AT+CPMS command.

##### ENTER PSM

##### EXIT PSM

```
<err> Error code. See Chapter 15 for details.
```
#### AT+QPSMS Power Saving Mode Setting

```
Test Command
AT+QPSMS=?
```
```
Response
+QPSMS: (range of supported <T1>s),(range of supported
<T2>s)
```
```
OK
Read Command
AT+QPSMS?
```
```
Response
+QPSMS: <N_T1>,<N_T2>
```
```
OK
Write Command
AT+QSCLK=<T1>,<T2>
```
```
Response
OK
```

#### Parameter

### 9.10. AT+QSCLK Configure Sleep Mode

This command configures the TE’s sleep modes.

```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect immediately.
Remain valid after deep-sleep wakeup.
The configurations are not saved to NVRAM.
```
```
<T1> Integer type. The value of T3324. Unit: seconds. Range: 0 – 11160.
<T2> Integer type. The value of extended T3412. Unit: seconds. Range: 0 – 35712000.
<N_T1> Integer type. The value of T3324 provided by the network. Unit: seconds. Range: 0 – 11160.
If the value is 1, T3324 is disabled.
<N_T2> Integer type. The value of extended T3412 provided by the network if the value of extended
T3412 exists. The value of T3412 if the extended T3412 value does not exist. Unit:
seconds. Range: 0 – 35712000. If the value is 1, the value of extended T3412 and value of
T3412 are disabled.
<err> Error code. See Chapter 15 for details.
```
#### AT+QSCLK Configure Sleep Mode

```
Test Command
AT+QSCLK=?
```
```
Response
+QSCLK: (range of supported <n>s)
```
```
OK
Read Command
AT+QSCLK?
```
```
Response
+QSCLK: <n>
```
```
OK
Write Command
AT+QSCLK=<n>
```
```
Response
OK
```
```
If there is any error:
ERROR
```

#### Parameter

1. UART does not work during the light sleep mode. Therefore, when AT+QSCLK=1 or
    AT+QSCLK=2, send AT before each command to make sure the UART is woken up.
2. When AT+QSCLK=0, UART is always working. To make the module enter sleep modes, send
    AT+QSCLK=1 or AT+QSCLK=2.
3. Before data communication, it is recommended to execute AT+QSCLK=0 to disable sleep modes.
    After data communication is completed, it is recommended to execute AT+QSCLK=1 to enable
    sleep mode again to save power.
4. When the module is woken up from light sleep mode by PSM_EINT, the module will enter the light
    sleep mode again immediately. It is recommended to wake up the module through sending AT
    commands and then follow the suggestion in Note 3.

#### Example

##### AT+QSCLK= 0

##### OK

```
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect immediately.
Remain valid after deep-sleep wakeup.
The configuration is not saved to NVRAM.
```
```
<n> Integer type.
0 Disable sleep modes
1 Enable light sleep and deep sleep, wakeup by PSM_EINT (at falling edge) and the Main
UART
2 Enable light sleep only, wakeup by the Main UART or PSM_EINT
<err> Error code. See Chapter 15 for details.
```
##### NOTE


## 10 Platform Related Commands

### 10.1. AT+CBC Query Power Supply Voltage

This command queries the voltage value of power supply.

#### Parameter

#### Example

##### AT+CBC

##### +CBC: 3369

##### OK

#### AT+CBC Query Power Supply Voltage

```
Test Command
AT+CBC=?
```
```
Response
OK
Execution Command
AT+CBC
```
```
Response
+CBC: <voltage>
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
Characteristics /
```
<voltage> Integer type. Battery voltage. Unit: mV.
<err> Error code. See Chapter 15 for details.


### 10.2. AT+CMEE Report Mobile Termination Error

This Write Command disables or enables the use of final result code +CME ERROR: <err> as an
indication of an error relating to the functionality of MT. When the report of the final result code +CME
ERROR: <err> is enabled, MT-related errors cause +CME ERROR: <err> as the final result code instead
of the regular ERROR as the final result code. ERROR is returned normally when there is an error related
to syntax, invalid parameters or TA functionality.

This Read Command returns the current setting of <n>.

The Test Command returns values supported as a compound value.

#### Parameter

#### Example

##### AT+CMEE?

##### +CMEE: 1

##### OK

#### AT+CMEE Report Mobile Termination Error

```
Test Command
AT+CMEE=?
```
```
Response
+CMEE: (range of supported <n>s)
```
```
OK
Read Command
AT+CMEE?
```
```
Response
+CMEE: <n>
```
```
OK
Write Command
AT+CMEE=<n>
```
```
Response
OK
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect immediately.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM.
```
<n> Integer type. Enable/disable the use of result code +CME ERROR: <err>.
0 Disable result code
1 Enable result code and use numeric values
2 Enable result code and use verbose values
<err> Error code. See Chapter 15 for details.


##### AT+CMEE=?

##### +CMEE: (0-2)

##### OK

### 10.3. AT+QADC Query the Input Voltage of Dedicated ADC Channel

This command queries the input voltage of a dedicated ADC channel.

#### Parameter

#### AT+QADC Query the Input Voltage of Dedicated ADC Channel

```
Test Command
AT+QADC=?
```
```
Response
+QADC: (list of supported <channel>s)
```
```
OK
Read Command
AT+QADC?
```
```
Response
+QADC: <channel>,<voltage>
```
```
OK
Write Command
AT+QADC=<channel>
```
```
Response
+QADC: <channel>,<voltage>
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics /
```
```
<channel> Integer type. ADC conversion channel. Currently only channel 0 (ADC0) is valid.
<voltage> Integer type. Sample voltage value or the average value of sample voltages.
Range: 0– 12 00. Unit: mV.
```

1. AT+QADC queries the input voltage value of the ADC0 channel.
2. Detection results between 0.1–1.1 V are fine in accuracy, while detection results between 0–0.1 V or
    1.1–1.2 V are less accurate.

#### Example

##### AT+QADC?

##### +QADC: 0 ,796

##### OK

### 10.4. AT+QRST Module Reset

This command resets the module immediately.

#### Parameter

#### AT+QRST Module Reset

```
Test Command
AT+QRST=?
```
```
Response
+QRST: (list of supported <mode>s)
```
```
OK
Write Command
AT+QRST=<mode>
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
Characteristics /
```
<mode> Integer type.
1 The module resets immediately after OK is returned without detaching from the
network.
<err> Error code. See Chapter 15 for details.

##### NOTE


### 10.5. AT+QRFSTAT Query RF Status

This command is used to query RF Status.

#### Parameter

#### AT+QRFSTAT Query RF Status

```
Test Command
AT+QRFSTAT=?
```
```
Response
OK
Execution Command
AT+QRFSTAT
```
```
Response
+QRFSTAT: <status>
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
Characteristics /
```
<status> String type. RF calibration status.
CALIBRATE RF has been calibrated
NOT CALIBRATE RF has not been calibrated. The module cannot be used
<err> Error code. See Chapter 15 for details.


## 11 General Configuration Commands

### 11.1. AT+QCFG System Configuration

This command configures the system.

#### Parameter

#### AT+QCFG System Configuration

```
Test Command
AT+QCFG=?
```
```
Response
List of
+QCFG: <function>,(list of supported <value>s)
...
```
```
OK
Read Command
AT+QCFG?
```
```
Response
List of
+QCFG: <function>,<value>
...
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
Characteristics /
```
<function> String type. Functions to be configured.
"EPCO" Configure the extended protocol configuration options (EPCO)
"DataInactTimer" Configure inactivity timer
"OOSScheme" Configure network searching mechanism in OOS
"logbaudrate" Configure baud rate
"slplocktimes" Configure sleep duration


For some special requirements from mobile network operators, the configuration may not take effect.

#### 11.1.1. AT+QCFG="EPCO" Enable/Disable EPCO

This command enables or disables extended protocol configuration options. This Write Command can
only be used when AT+CFUN=0.

"dsevent" Configure whether to enable the URC ENTER DEEPSLEEP of
deep sleep event or not
"statisr" Configure the report interval of statistics URC
"MacRAI" Enable or disable RAI in MAC layer
"relversion" Configure protocol release version
"NBcategory" Configure UE category
"wakeupRXD" Determine whether the UE can be woken up by RXD
"faultaction" Set the action performed by UE after an error occurs
"GPIO" Configure GPIO status
"NcellMeas" Enable or disable neighbor cell measurement
"SimBip" Enable or disable SIMBIP
"activetimer" Configure active timer value.
"simpsm" Configure USIM power saving mode.
<value> Integer type/String type. See Chapter 11.1.1–Chapter 11.1.17 for details.
<err> Integer type. Error code. See Chapter 15 for details.

#### AT+QCFG="EPCO" Enable/Disable EPCO

```
Write Command
AT+QCFG="EPCO"[,<value>]
```
```
Response
If the optional parameter is omitted, query the current
configuration:
+QCFG: "EPCO",<value>
```
```
OK
```
```
If the optional parameter is specified, enable or disable
EPCO:
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
##### NOTE


#### Parameter

#### 11.1.2. AT+QCFG="DataInactTimer" Configure Inactivity Timer

This command configures the data inactivity timer of UE. This Write Command can only be used when
AT+CFUN=0. The inactivity timer, after being enabled, starts when there is neither UL data nor DL data
being sent or received, including RRC and NAS signaling, and restarts every time a UL or DL
transmission begins. After the timer expires, the module will release the RRC connection.

```
Characteristics
```
```
The command takes effect after the module is rebooted.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM automatically.
```
<value> Integer type
0 Disable EPCO
1 Enable EPCO
<err> Error code. See Chapter 15 for details.

#### AT+QCFG="DataInactTimer" Configure Inactivity Timer

```
Write Command
AT+QCFG="DataInactTimer"[,<value>
]
```
```
Response
If the optional parameter is omitted, query the current
configuration:
+QCFG: "DataInactTimer",<value>
```
```
OK
```
```
If the optional parameter is specified, configure the inactivity
timer of UE:
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command can only be used in CFUN0 mode, and takes
effect after the mode changes into CFUN1.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM automatically.
```

#### Parameter

#### 11.1.3. AT+QCFG="OOSScheme" Configure Network Searching Mechanism in OOS

This command configures the network searching mechanism of UE in OOS.

#### Parameter

<value> Integer type. Configure time of the inactivity timer. Unit: second. Default value: 60.
0 Disable inactivity timer
15 – 255 Enable inactivity timer and set the timer
<err> Error code. See Chapter 15 for details.

#### AT+QCFG="OOSScheme" Configure Network Searching Mechanism in OOS

```
Write Command
AT+QCFG="OOSScheme"[,<value>]
```
```
Response
If the optional parameter is omitted, query the current
configuration:
+QCFG: "OOSScheme",<value>
```
```
OK
```
```
If the optional parameter is specified, configure the network
searching mechanism in OOS:
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect after the module is rebooted.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM automatically.
```
<value> Integer type. Network searching mechanism in OOS.
0 Search PLMN at the interval of 30 secs, 1 min, 2 min
1 Search PLMN at the interval of 5 min, 10 min, 15 min
2 Search PLMN at the interval of 10 min, 30 min, 1 hour
3 Search PLMN at the interval of 30 secs, then stop searching PLMN till AT+QPLMNS
is executed (see Chapter 7.9).
4 Never search PLMN till AT+QPLMNS is executed (see Chapter 7.9).


#### 11.1.4. AT+QCFG="logbaudrate" Configure Baud Rate.......................................................

This command configures the baud rate for log capture. The default baud rate is 6000000 bps. If your
serial chip does not support 6000000 bps, you can configure it to 3000000 bps or lower. The lower the
baud rate, the more log information is likely to be lost. The baud rate configured here should be the same
as the baud rate selected by the log tool. Otherwise, the log cannot be captured.

#### Parameter

#### 11.1.5. AT+QCFG="slplocktimes" Configure Countdown to Entering Sleep Mode

This command configures the countdown for the UE to enter sleep mode.

<err> Error code. See Chapter 15 for details.

#### AT+QCFG="logbaudrate" Configure Baud Rate

```
Write Command
AT+QCFG="logbaudrate"[,<value>]
```
```
Response
If the optional parameter is omitted, query the current
configuration:
+QCFG: "logbaudrate",<value>
```
```
OK
```
```
If the optional parameter is specified, configure baud rate:
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect after the module is rebooted.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM automatically.
```
<value> Integer type. Baud rate of the port for log capture. Unit: bps. Range: 921600– 6000000.
Unit: bps. Default value: 6000000.
<err> Error code. See Chapter 15 for details.

#### AT+QCFG="slplocktimes" Configure Countdown to Entering Sleep Mode

```
Write Command
AT+QCFG="slplocktimes"[,<value>]
```
```
Response
If the optional parameter is omitted, query the current
```

#### Parameter

#### 11.1.6. AT+QCFG="dsevent" Control the Reporting of URC Indicating Deep Sleep

This command disables or enables the report of URC that indicates deep sleep. If the URC is enabled, an
URC will be reported when the module enters or exits from the deep sleep mode.

```
configuration:
+QCFG: "slplocktimes",<value>
```
```
OK
```
```
If the optional parameter is specified, configure the sleep
duration of UE:
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect after the module is rebooted.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM automatically.
```
<value> Integer type. The countdown for the module to enter sleep mode. Range: 0–30. Unit:
second. Default value: 10.
<err> Error code. See Chapter 15 for details.

#### AT+QCFG="dsevent" Control the Reporting of URC Indicating Deep Sleep

```
Write Command
AT+QCFG="dsevent"[,<value>]
```
```
Response
If the optional parameter is omitted, query the current
configuration:
+QCFG: "dsevent",<value>
```
```
OK
```
```
If the optional parameter is specified, control the reporting of
the deep sleep URC:
OK
```
```
If there is any error:
```

#### Parameter

#### 11.1.7. AT+QCFG="statisr" Configure Report Interval of Statistics URC

This command configures the report interval of the URC reporting statistics. After the interval is set, it can
only be modified after enabling the URC reporting again.

The URC formats are listed as below:

+STATISR: PHY DL, AvgRSRP: -77, AvgSnr: 14, DlBler: 0%, PhyDlTpt: 0 bps, AvgTBS: 0, AvgItbs: 0,
AvgNRep: 0, AvgSbfrmNum: 0, Harq2Ratio: 0%

+STATISR: PHY UL, UlBler: 0%, PhyUlTpt: 0 bps, AvgTBS: 0, AvgItbs: 0, AvgNRep: 0,
AvgSbfrmNum: 0, Harq2Ratio: 0%, AvgScNum: 0

+STATISR: MAC, MacUlBytes:0, MacUlPadBytes:0, MacDlBytes: 0, MacDlPadBytes: 0, MacUlTpt: 0
bps, MacDlTpt: 0 bps

+STATISR: RLC, RlcUlPduBytes:0, RlcUlRetxBytes:0, RlcDlPduBytes: 0, RlcUlTpt: 0 bps, RlcDlTpt:
0 bps

+STATISR: PDCP, PdcpUlPduBytes: 0, PdcpDlPduBytes: 0, PdcpULDiscardBytes: 0, PdcpUlTpt: 0
bps, PdcpDlTpt: 0 bps

##### ERROR

```
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect after the module is rebooted.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM automatically.
```
<value> Integer type. Disable/enable the reporting of deep sleep event URC.
0 Disable
1 Enable
<err> Error code. See Chapter 15 for details.

#### AT+QCFG="statisr" Configure Report Interval of Statistics URC

```
Write Command
AT+QCFG="statisr"[,<value>]
```
```
Response
If the optional parameter is omitted, query the current
configuration:
+QCFG: "statisr",<value>
```

#### Parameter

#### 11.1.8. AT+QCFG="MacRAI" Enable/Disable RAI in MAC Layer

This command enables or disables RAI in MAC layer. It can only be used when AT+CFUN=0. This feature
can only be available when the AT+QCFG="relversion" is set to R14.

##### OK

```
If the optional parameter is specified, configure the report
interval:
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect immediately.
Remain valid after deep-sleep wakeup.
The configuration is not saved to NVRAM.
```
<value> Integer type. Report interval of statistics URC. Default value: 0.
0 Disable the reporting of statistics URC
5 – 600 Enable the reporting of statistics URC and set the report interval. Unit: second
<err> Error code. See Chapter 15 for details.

#### AT+QCFG="MacRAI" Enable/Disable RAI in MAC Layer

```
Write Command
AT+QCFG="MacRAI"[,<value>]
```
```
Response
If the optional parameter is omitted, query the current
configuration:
+QCFG: "MacRAI",<value>
```
```
OK
```
```
If the optional parameter is specified, enable or disable RAI in
MAC layer:
OK
```
```
If there is any error:
ERROR
```

#### Parameter

AT+QCFG="MacRAI" only applies to networks supporting the 3GPP R14 protocol.

#### 11.1.9. AT+QCFG="relversion" Configure Protocol Release Version

This command configures protocol release version. It can only be used when AT+CFUN=0.

Some features, such as MACRAI and 2-HARQ, eTBs, are supported only in R14 protocol. If the release
version is changed to R14 from R13, the AT+QCFG="NBcategory" (see Chapter 11.1.10) is set to 2
automatically.

```
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect after the module is rebooted.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM automatically.
```
<value> Integer type. Enable or disable MAC RAI feature.
0 Disable RAI in AS
1 Enable RAI in AS
<err> Error code. See Chapter 15 for details.

#### AT+QCFG="relversion" Configure Protocol Release Version

```
Write Command
AT+QCFG="relversion"[,<value>]
```
```
Response
If the optional parameter is omitted, query the current
configuration:
+QCFG: "relversion",<value>
```
```
OK
```
```
If the optional parameter is specified, cofigure the protocol
release version:
OK
```
```
If there is any error:
ERROR
Or
```
##### NOTE


#### Parameter

AT+QCFG="relversion" only applies to networks supporting the 3GPP R14 Protocol.

#### 11.1.10. AT+QCFG="NBcategory" Configure UE Category

This command configures UE category. It can only be used when AT+CFUN=0. Only when the category
is set to NB2, the module can use extended features such as TBs and 2 - HARQ.The maximum TBs in Cat
NB2 is 2536 bits in both DL and UL, while the maximum TBs in Cat NB1 is only 1000 bits in UL and
680 bits in DL.

```
+CME ERROR: <err>
```
```
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect after the module is rebooted.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM automatically.
```
<value> Integer type. Protocol release version.
13 Release 13
14 Release 14
<err> Error code. See Chapter 15 for details.

#### AT+QCFG="NBcategory" Configure UE Category

```
Write Command
AT+QCFG="NBcategory"[,<value>]
```
```
Response
If the optional parameter is omitted, query the current
configuration:
+QCFG: "NBcategory",<value>
```
```
OK
```
```
If the optional parameter is specified, set UE category:
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
##### NOTE


#### Parameter

1. AT+QCFG="NBcategory" only applies to networks supporting the 3GPP R14 Protocol.
2. When protocol release version is set to 14 through AT+QCFG="relversion", UE-category value will
    automatically change to 2 (category NB2).

#### 11.1.11. AT+QCFG="wakeupRXD" Enable/Disable RXD to Wake Up UE

This command determines whether the UE can be woken up by RXD.

```
Characteristics
```
```
The command takes effect after the module is rebooted.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM automatically.
```
<value> Integer type. UE-Category.
1 Category NB1
2 Category NB2, only valid when AT+QCFG="relversion" is set to 14
<err> Integer type. Error code. See Chapter 15 for details.

#### AT+QCFG="wakeupRXD" Enable/Disable RXD to Wake Up UE

```
Write Command
AT+QCFG="wakeupRXD"[,<value>]
```
```
Response
If the optional parameter is omitted, query the current
configuration:
+QCFG: "wakeupRXD",<value>
```
```
OK
```
```
If the optional parameter is specifed, determines whether the
UE can be woken up by RXD:
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect after the module is rebooted.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM automatically.
```
##### NOTE


#### Parameter

#### 11.1.12. AT+QCFG="faultaction" Configure UE Reaction to System Crash

This command sets the action performed by UE after a crash.

#### Parameter

```
<value> Integer type. Enable/disable RXD to wake up UE.
0 Disable
1 Enable
<err> Error code. See Chapter 15 for details.
```
#### AT+QCFG="faultaction" Configure UE Reaction to System Crash

```
Write Command
AT+QCFG="faultaction"[,<value>]
```
```
Response
If the optional parameter is omitted, query the current
conifguraion:
+QCFG: "faultaction",<value>
```
```
OK
```
```
If the optional parameter is specified, configure UE action:
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect after the module is rebooted.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM automatically.
```
<value> Integer type. Action performed by UE after a crash.
0 Dump full exception info to flash and EPAT tool and then get trapped in endless loop
1 Print necessary exception info then reset
2 Dump full exception info to flash then reset
3 Dump full exception info to flash and EPAT tool then reset
4 Reset directly
<err> Error code. See Chapter 15 for details.


#### 11.1.13. AT+QCFG="GPIO" Configure GPIO Status

The command queries and configures the GPIO status. If <mode> is omitted, the default value 2 is used.
If <pin> is omitted, the module returns status of all GPIOs in ascending order of GPIO serial number; if
<pin> is specified, the module returns the status of the specific GPIO only. If <mode> is 1 or 3, <pin>
should be specified, and the returned value is only for the specific GPIO.

#### Parameter

#### AT+QCFG="GPIO" Configure GPIO Status

```
Write Command
AT+QCFG="GPIO"[,<mode>[,<pin>
[,<dir>[,<pullsel>[, <level>]]]]]
```
```
Response:
when <mode>=1, no parameter shall be omitted:
OK
```
```
when <mode>= 2 or is omitted:
+QCFG: "GPIO",<level>[,<level>,<level>,<level>]
```
```
OK
```
```
If <mode>=3, only and must set value of a specified GPIO.
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5s
Characteristics /
```
```
<mode> Integer type. Operation type.
1 Initialize GPIO status
2 Query GPIO status
3 Configure GPIO status
<pin> Integer type. GPIO pin number.
Pin No. Pin Name
1 GPIO1
2 GPIO2
3 GPIO3
4 GPIO4
<dir> Integer type. GPIO pin direction.
0 Input
1 Output
```

#### Example

##### AT+QCFG="GPIO"

##### +QCFG: "GPIO",1,1,1,1

##### OK

##### AT+QCFG="GPIO",2

##### +QCFG: "GPIO",1,1,1,1

##### OK

##### AT+QCFG="GPIO",2,1

##### +QCFG: "GPIO",1

##### OK

#### 11.1.14. AT+QCFG="NcellMeas" Enable or Disable Neighbor Cell Measurement

This command disables or enables the neighbor cell measurement. Disabled neighbor cell measurement
helps decrease the power consumption. This Write Command can only be used when AT+CFUN=0.

```
<pullsel> Integer type. GPIO pin pull type.
0 Pull the GPIO up
1 Pull the GPIO down
2 Leave the GPIO as it is
<level> Integer type. GPIO logic level.
0 Low
1 High
<err> Error code. See Chapter 15 for details.
```
#### AT+QCFG="NcellMeas" Enable or Disable Neighbor Cell Measurement

```
Write Command
AT+QCFG="NcellMeas"[,<value>]
```
```
Response
If the optional parameter is omitted, query the current
configuration:
+QCFG: "NcellMeas",<value>
```
```
OK
```
```
If the optional parameter is specified, enable or disable the
neighbor cell measurement:
OK
```
```
If there is any error:
ERROR
Or
```

#### Parameter

#### 11.1.15. AT+QCFG="SimBip" Enable or Disable SIMBIP

This command enables or disables SIMBIP.

```
+CME ERROR: <err>
```
```
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command can only be used in CFUN0 mode, and takes
effect after the mode changes into CFUN1.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM automatically.
```
<value> Integer type. Enable or disable the neighbor cell measurement.
0 Disable the neighbor cell measurement
1 Enable the neighbor cell measurement
<err> Error code. See Chapter 15 for details.

#### AT+QCFG="SimBip" Enable or Disable SIMBIP

```
Write Command
AT+QCFG="SimBip"[,<value>]
```
```
Response
If the optional parameter is omitted, query the current
configuration:
+QCFG: "SimBip",<value>
```
```
OK
```
```
If the optional parameter is specified, enable or disable
SIMBIP:
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect after the module is rebooted.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM automatically.
```

#### Parameter

#### 11.1.16. AT+QCFG="activetimer" Configure Active Timer Value............................................

This command configures active timer value.

#### Parameter

```
<value> Integer type
0 Disable SIMBIP
1 Enable SIMBIP
```
<err>^ Error code. See^ Chapter^15 for details.^

#### AT+QCFG="activetimer" Configure Active Timer Value

```
Write Command
AT+QCFG="activetimer"[,<value>]
```
```
Response
If the optional parameter is omitted, query the current
configuration:
+QCFG: "activetimer",<value>
```
```
OK
```
```
If the optional parameter is specified, set active timer value:
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect after the module is rebooted.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM automatically.
```
```
<value> Integer type
0 Set the value of active timer to 0
1 Set the value of active timer to the value received from core network
```
<err>^ Error code. See^ Chapter^15 for details.^


#### 11.1.17. AT+QCFG="simpsm" Configure USIM Power Saving Mode

This command enables or disables USIM power saving mode.

#### Parameter

#### AT+QCFG="simpsm" Configure USIM power saving mode

```
Write Command
AT+QCFG="simpsm"[,<value>]
```
```
Response
If the optional parameter is omitted, query the current
configuration:
+QCFG: "simpsm",<value>
```
```
OK
```
```
If the optional parameter is specified, enable or disable USIM
power saving mode:
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect after the module is rebooted.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM automatically.
```
```
<value> Integer type
0 Disable USIM power saving mode
1 Enable USIM power saving mode
```
<err>^ Error code. See^ Chapter^15 for details.^


## 12 Time Related Commands

### 12.1. AT+CCLK Set and Get Current Date and Time

This Write Command sets the real-time clock. RTC is automatically synchronized once UE has received
EMM INFORMATION signaling.

This Read Command returns the current setting of the clock.

#### Parameter

#### AT+CCLK Set and Get Current Date and Time

```
Test Command
AT+CCLK=?
```
```
Response
OK
Read Command
AT+CCLK?
```
```
Response
+CCLK: <time>
```
```
OK
Write Command
AT+CCLK=<time>
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect immediately.
Remain valid after deep-sleep wakeup.
The configuration is not saved to NVRAM
```
<time> String type. The format is "YY/MM/DD,hh:mm:ss±zz", where characters indicate
year (two last digits), month, day, hour, minute, second and time zone (indicates
the difference, expressed in quarters of an hour, between the local time and GMT;
the range is - 96 to +96.) For instance, 6th of May 2014, 22:10:00 GMT+2 hours
equals "14/05/06,22:10:00+08".


#### Example

AT+CCLK? //Query the current setting of the clock.
+CCLK: 20/11/03,06:25:06+32

OK
AT+CCLK="20/02/27,01:30:48+23"
OK

### 12.2. AT+CTZR Time Zone Reporting

This Write Command controls the time zone change event reporting. If reporting is enabled, the MT
returns the unsolicited result code +CTZV: <tz>, +CTZE:<tz>,<dst>,[<time>], or +CTZEU:
<tz>,<dst>,[<utime>] whenever the time zone is changed. The MT also provides the time zone upon
network registration if provided by the network. If setting fails in an MT error, +CME ERROR: <err> is
returned.

This Read Command returns the current reporting settings in the MT.

<err> Error code. See Chapter 15 for details.

#### AT+CTZR Time Zone Reporting

```
Test Command
AT+CTZR=?
```
```
Response
+CTZR: (range of supported <reporting>s)
```
```
OK
Read Command
AT+CTZR?
```
```
Response
+CTZR: <reporting>
```
```
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
Write Command
AT+CTZR=<reporting>
```
```
Response
OK
```
```
If there is any error:
ERROR
Or
+CME ERROR: <err>
```

#### Parameter

```
This command needs to be set before the module camps on a cell.
```
```
Maximum Response Time 5 s
```
```
Characteristics
```
```
The command takes effect immediately.
Remain valid after deep-sleep wakeup.
The configuration is saved to NVRAM automatically.
```
```
<reporting> Integer type.
0 Disable time zone change event reporting
1 Enable time zone change event reporting by URC +CTZV: <tz>
2 Enable extended time zone and local time reporting by unsolicited result code
+CTZE: <tz>,<dst>,[<time>]
3 Enable extended time zone and universal time reporting by unsolicited result code
+CTZEU: <tz>,<dst>[,<utime>]
<tz> String type. Sum of the local time zone (difference between the local time and GMT
expressed in quarters of an hour) plus daylight saving time. The format is “±zz",
expressed as a fixed width, two digits integer with the range of - 47 to +48. To maintain a
fixed width, numbers in the range of - 9 to +9 are expressed with a leading zero, e.g.
“- 09 ", “+00", and “+09".
<dst> Integer type. Whether <tz> includes daylight savings adjustment or not.
0 <tz> includes no adjustment for Daylight Saving Time
1 <tz> includes +1 hour (equals 4 quarters in <tz>) adjustment for daylight saving
time
2 <tz> includes +2 hours (equals 8 quarters in <tz>) adjustment for daylight saving
time
<time> String Type. Local time. The format is "YYYY/MM/DD,hh:mm:ss" expressed as integers
representing year (YYYY), month (MM), date (DD), hour (hh), minute (mm) and second
(ss). The local time can be derived by the MT from information provided by the network
at the time of delivering time zone information and is present in the unsolicited result
code for extended time zone and local time reporting if the universal time is provided by
the network.
<utime> String Type. Universal time. The format is "YYYY/MM/DD,hh:mm:ss", expressed as
integers representing year (YYYY), month (MM), date (DD), hour (hh), minute (mm) and
second (ss). The universal time can be provided by the network at the time of delivering
time zone information and is present in the unsolicited result code for extended time
zone and universal time reporting if provided by the network.
<err> Error code. See Chapter 15 for details.
```
##### NOTE


#### Example

##### AT+CTZR=?

##### +CTZR: (0- 3 )

##### OK

AT+CTZR= 1 //Enable time zone change event reporting by URC +CTZV: <tz>
OK
AT+CTZR? //Query the current configuration.
+CTZR: 1

OK


## 13 SMS-Related Commands

### 13.1. AT+CMGF Configure Message Format

This command tells the TA the input and output format of messages to be used.

#### Parameter

#### AT+CMGF Configure Message Format

Test Command
AT+CMGF=?

```
Response
+CMGF: (list of supported <mode>s)
```
OK
Read Command
AT+CMGF?

```
Response
+CMGF: <mode>
```
OK
Write Command
AT+CMGF=<mode>

```
Response
OK
```
```
If there is any error:
ERROR
Or
+CMS ERROR: <err>
```
Maximum Response Time 300 ms

Characteristics

The command takes effect immediately.
Remain valid after deep-sleep wakeup.
The configuration is not saved to NVRAM.
Reference
3GPP 27.005

<mode> Integer type. Message format.
1 Text mode
<err> Integer type. Error code. See Chapter 15 for details.


### 13.2. AT+CSCA Update SMSC Address

This command updates the SMSC address, through which mobile originated SMS are transmitted.

#### Parameter

### ⚫

1. The SMSC address should be entered in the format specified by the corresponding service provider.
2. It is strongly recommended not to rewrite the SMSC address of the USIM card while in use.

#### AT+CSCA Update SMSC Address

Test Command
AT+CSCA=?

Response
OK
Read Command
AT+CSCA?

```
Response
+CSCA: <sca>,<tosca>
```
OK
Write Command
AT+CSCA=<sca>[,<tosca>]

```
Response
OK
```
```
If there is any error:
ERROR
Or
+CMS ERROR: <err>
```
Maximum Response Time 300 ms

Characteristics

The command takes effect immediately.
Remain valid after deep-sleep wakeup.
The configurations are saved to NVRAM automatically.
Reference
3GPP 27.005

<sca> String type. SMSC address. 3GPP TS 24.011 RP SC address Address-Value field. BCD
numbers (or GSM default alphabet characters) are converted to characters of the currently
selected TE character set. Type of address is given by <tosca>.
<tosca> Integer type. Type of SMSC address. 3GPP TS 24.011 RP SC address Type-of-Address
octet (default refer to <toda>).
145 International number type (ISDN format)
129 Unknown number type (ISDN format)
<err> Integer type. Error code. See Chapter 15 for details.

##### NOTE


#### Example

AT+CSCA="+8613800210500",145 //Configure SMSC address.
OK
AT+CSCA? //Query SMSC address.
+CSCA: "+8613800210500",145

OK

### 13.3. AT+CMGS Send Message

This command sends a message (SMS-SUBMIT) from TE to the network. Message reference value <mr>
will be returned to the TE on successful message delivery. The value can be used to identify the message
upon receiving an unsolicited delivery status report result code.

#### Parameter

#### AT+CMGS Send Message

Test Command
AT+CMGS=?

Response
OK
Write Command
If in text mode (AT+CMGF=1):
AT+CMGS=<da>[,<toda>]<CR>
>
After the response >, input the data to
be sent. Tap Ctrl and Z to send, and tap
Esc to cancel the operation.

```
Response
If the message is sent successfully:
+CMGS: <mr>
```
```
OK
```
```
If there is any error:
ERROR
Or
+CMS ERROR: <err>
```
Maximum Response Time 120 s, determined by network.

Characteristics /

Reference
3GPP 27.005

<da> String type. Destination Address. 3GPP 23.040 TP-Destination-Address Address-Value
field.
<toda> Integer type. 3GPP 24.011 TP-Destination-Address Type-of-Address octet (when the first
character of <da> is + (IRA 43), the default value is 145; otherwise the default value is
129).
<mr> Integer type. TP-Message-Reference.


#### Example

AT+CMGF=1 //Set message format to text mode.
OK
AT+CMGS="15021012496"
>This is a test from Quectel //Enter the message. Tap Ctrl and Z to send.

+CMGS: 247

OK

### 13.4. +CMT Receive New Message

SMS-DELIVERs are routed directly to the TE by using this unsolicited result code.

#### Parameter

#### Example

##### +CMT: "50501443",,"22/12/07,15:23:02 +44"1234

<err> Integer type. Error code. See Chapter 15 for details.

#### +CMT Receive New Message

+CMT: <oa>,,<scts><data>
(Text mode is enabled)
Route SMS-DELIVERs directly to the TE.

<oa> String type. Source address of deliver message (text mode is enabled).
<scts> String type. TP-Discharge-Time in time-string format: "yy/MM/dd,hh:mm:ss±zz". E.g. 6th of
May 1994, 22:10:00 GMT+2 hours equals to "94/05/06,22:10:00+08".
<data> String type. Content of delivered message in HEX string format.


## 14 Other Commands

### 14.1. TCP/IP Related Commands

## Table 2 : List of TCP/IP Related AT Commands

For more details, see document [1].

```
SN AT Command Description
```
```
[1] AT+QIOPEN Open a Socket Service
```
```
[2] AT+QICLOSE Close a Socket Service
```
```
[3] AT+QISTATE Query Socket Service Status
```
```
[4] AT+QISEND Send Hex/Text String Data
```
```
[8] AT+QPING Ping a Remote Server
```
```
[ 9 ] AT+QNTP Synchronize Local Time through NTP Server
```
```
[ 10 ] AT+QIDNSGIP Get IP Address by Domain Name
```
```
[ 11 ] AT+QIDNSCFG Configure DNS Server Address
```
```
[ 12 ] AT+QICFG Configure Optional Parameters
```

### 14.2. MQTT Related Commands

## Table 3 : List of MQTT Related AT Commands

For more details, see document [2].

### 14.3. DFOTA Related Commands

## Table 4 : List of DFOTA Related AT Commands

For more details, see document [3].

```
SN AT Command Description
```
```
[1] AT+QMTCFG Configure Optional Parameters of MQTT
```
```
[2] AT+QMTOPEN Open a Network for MQTT Client
```
```
[3] AT+QMTCLOSE Close a Network for MQTT Client
```
```
[4] AT+QMTCONN Connect a Client to MQTT Server
```
```
[5] AT+QMTDISC Disconnect a Client from MQTT Server
```
```
[6] AT+QMTSUB Subscribe to Topics
```
```
[7] AT+QMTUNS Unsubscribe from Topics
```
```
[8] AT+QMTPUB Publish Messages
```
```
SN AT Command Description
```
```
[1] AT+QFOTADL Trigger Automatic DFOTA over HTTP
```

## 15 Summary of Error Codes

This chapter introduces the <err> codes related to the BC660K-GL and BC950K-GL modules.

The error codes listed in the following tables are compliant with 3GPP specifications.

## Table 5 : CME ERROR: <err>

```
<err> Description
```
```
1 MT not connected
```
```
2 MT link reserved
```
```
3 Operation not allowed
```
```
4 Operation not supported
```
```
5 PH-SIM PIN required
```
```
6 PH-FSIM PIN required
```
```
7 PH-FSIM PUK required
```
```
10 USIM not inserted
```
```
11 USIM PIN required
```
```
12 USIM PUK required
```
```
13 USIM failure
```
```
14 USIM busy
```
```
15 USIM wrong
```
```
16 Incorrect password
```
```
17 USIM PIN2 required
```
```
18 USIM PUK2 required
```

20 Memory full

21 Invalid index

22 Not found

23 Memory failure

24 Text string too long

25 Invalid characters in text string

26 Dial string too long

27 Invalid characters in dial string

30 No network service

31 Network timeout

32 Network not allowed - emergency call only

40 Network personalization PIN required

41 Network personalization PUK required

42 Network subset personalization PIN required

43 Network subset personalization PUK required

44 Service provider personalization PIN required

45 Service provider personalization PUK required

46 Corporate personalization PIN required

47 Corporate personalization PUK required

48 Hidden key required

49 EAP method not support

50 Incorrect Parameters

51 Command implemented but currently disabled

52 Command aborted by user

53 Not attached to network due to MT functionality restrictions


54 Modem not allowed - MT restricted to emergency calls only

55 Operation not allowed because of MT functionality restrictions

56 Fixed dialing allowed only - dialed number is not a telephone number

57 Temporarily out of service due to other MT usage

58 Language/alphabet not supported

59 Data value out of range

60 System failure

61 Data missing

62 Call barred

63 Message waiting indication subscription failure

100 Unknown

103 Illegal MS

106 Illegal ME

107 GPRS services not allowed

108 GPRS services and non GPRS services not allowed

111 PLMN not allowed

112 Location area not allowed

113 Roaming not allowed in this location area

114 GPRS services not allowed in this PLMN

115 No suitable cells in location area

122 Congestion

126 Insufficient resources

127 Mission or unknown APN

128 Unknown PDP address or PDP type

129 User authentication failed


130 Activation of PDN rejected by GGSN services GW or PDN GW

131 Activation of PDN rejected for unknown cause

132 Service option not supported

133 Requested service option not subscribed

134 Service option temporarily out of order

140 Feature not supported

141 Semantic errors in the TFT operation

142 Syntactical errors in the TFT operation

143 Unknown PDP context

144 Semantic errors in packet filters

145 Syntactical errors in packet filters

146 PDP context without TFT already activated

148 Unspecified GPRS error

149 PDP authentication failure

150 Invalid mobile class

171 Last PDN disconnection not allowed

172 Semantically incorrect message

173 Mandatory information element error

174 Information element not existent or not implemented

175 Conditional IE error

176 Protocol error unspecified

177 Operator determined barring

178 Reaching max number of PDP contexts

179 Requested APN not supported in current RAT and PLMN combination

180 Request rejected, Bearer control mode violation


```
181 Unsupported QCI value
```
```
182 User data transmission via control plane is congested
```
```
301 Internal error base
```
```
302 UE busy
```
```
303 Not powered on
```
```
304 PDN not active
```
```
305 PDN not valid
```
```
306 PDN invalid type
```
```
307 PDN no parameter
```
```
308 UE failure
```
```
309 PDN type and APN duplicate used
```
```
312 USIM PIN already enabled
```
```
602 No RRC connection
```
## Table 6 : CMS ERROR: <err>

```
<err> Description
```
```
0 – 127 3GPP TS 24.011 Clause E.2 values
```
```
128 – 255 3GPP TS 23.040 Clause 9.2.3.22 values
```
```
300 ME failure
```
```
301 SMS service of ME reserved
```
```
302 Operation not allowed
```
```
303 Operation not supported
```
```
304 Invalid PDU mode parameter
```
```
305 Invalid text mode parameter
```
```
310 USIM not inserted
```

311 USIM PIN required

312 PH-USIM PIN required

313 USIM failure

314 USIM busy

315 USIM wrong

316 USIM PUK required

317 USIM PIN2 required

318 USIM PUK2 required

320 Memory failure

321 Invalid memory index

322 Memory full

330 SMSC address unknown

331 No network service

332 Network timeout

340 No +CNMA acknowledgement expected

500 Unknown error

Other values in range
256 – 511
Reserved

512 and above Manufacturer specific


## 16 Appendix References

## Table 7: Related Documents

```
Document Name
```
```
[1] Quectel_BC660K-GL&BC950K-GL_TCP(IP)_Application_Note
```
```
[2] Quectel_BC660K-GL&BC950K-GL_MQTT_Application_Note
```
```
[3] Quectel_BC660K-GL&BC950K-GL_DFOTA_Application_Note
```
## Table 8 : Terms and Abbreviations

```
Abbreviation Description
```
```
3GPP 3rd Generation Partnership Project
```
```
ACK Acknowledgement
```
```
AM Acknowledgement Mode
```
```
APDU Application Protocol Data Unit
```
```
APN Access Point Name
```
```
AS Access Stratum
```
```
BCD Binary-Coded Decimal
```
```
CHAP Challenge-Handshake Authentication Protocol
```
```
CN Core Network
```
```
DCE Data Communications Equipment
```
```
DF Dedicated File
```
```
DHCP Dynamic Host Configuration Protocol
```

DL Downlink

DTE Data Terminal Equipment

EARFCN E-UTRA Absolute Radio Frequency Channel Number

ECL Enhanced Coverage Level

EMM EPS Mobility Management

EPS Evolved Packet System

E-UTRAN Evolved Universal Terrestrial Radio Access Network

eDRX Extended Discontinuous Reception

EF Elementary File

EGPRS Enhanced General Packet Radio Service

ePCO Extended Protocol Configuration Options

EPS Evolved Packet System

ESM EPS Session Management

GERAN GSM/EDGE Radio Access Network

GGSN Gateway GPRS Support Node

GMT Greenwich Mean Time

GPRS General Packet Radio Service

GSM Global System for Mobile Communications

HARQ Hybrid Automatic Repeat Request

HPLMN Home Public Land Mobile Network

ICCID Integrated Circuit Card Identity

ICMP Internet Control Messages Protocol

ITU-T
International Telecommunication Union - Telecommunication Standardization
Sector

IE Information Element

IM Intermodulation/IP Multimedia


IMEI International Mobile Equipment Identity

IMEISV International Mobile Equipment Identity and Software Version

IMSI International Mobile Subscriber Identity

MS Mobile Station

MT Mobile Termination

MTU Maximum Transfer Unit

NAS Non-Access Stratum

NASCONFIG Non-Access Stratum Configuration

NB-IoT Narrowband Internet of Things

NSLPI NAS Signaling Low Priority Indication

NVRAM Non-Volatile Random Access Memory

OOS Out of Service

OOSA Out of Service Area

OPLMN Operator Controlled PLMN

PAD Packet Assember/Disassembler

PAP Password Authentication Protocol

PCI Physical Cell Identification

PCO Protocol Configuration Options

P-CSCF Proxy Call Session Control Function

PDCCH Physical Downlink Control Channel

PDCP Packet Data Convergence Protocol

PDN Public Data Network

PDP Packet Data Protocol

PIN Personal Identification Number

PLMN Public Land Mobile Network


PSM Power Saving Mode

PSD Packet Switch Domain

PSK Pre-Shared key

PUK PIN Unlock Key

QCI Quality of Service Class Indication

RAI Release Assistance Indication

RFC Request for Comments

RLC Radio Link Control

ROHC Robust Head Compression

RRC Radio Resource Control

RSCP Received Signal Code Power

RSRP Received Signal Received Power

RSRQ Reference Signal Received Quality

RSSI Received Signal Strength Indicator

RTC Real Time Clock

SINR Signal-to-interference-plus-noise Ratio

SMSC Short Message Service Center

SNDCP Sub-Network Dependent Convergence Protocol

SNR Signal-to-Noise Ratio

SVN Software Version Number

TA Terminal Adapter (typically the module)

TAC Tracking Area Code

TCP Transmission Control Protocol

TE Terminal Equipment (typically the MCU/external processor)

TTL Time to Live


UDP User Datagram Protocol

UE User Equipment

UICC Universal Integrated Circuit Card

UL Uplink

UPLMN User Controlled PLMN

URC Unsolicited Result Code

UTC Universal Time Coordinated

UUID Universally Unique Identifier

VPLMN Visited Public Land Mobile Network


