# The PEP 484 type hints stub file for the QtSerialPort module.
#
# Generated by SIP 4.19.3
#
# Copyright (c) 2017 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt5.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing
import sip

from PyQt5 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]


class QSerialPort(QtCore.QIODevice):

    class SerialPortError(int): ...
    NoError = ... # type: 'QSerialPort.SerialPortError'
    DeviceNotFoundError = ... # type: 'QSerialPort.SerialPortError'
    PermissionError = ... # type: 'QSerialPort.SerialPortError'
    OpenError = ... # type: 'QSerialPort.SerialPortError'
    ParityError = ... # type: 'QSerialPort.SerialPortError'
    FramingError = ... # type: 'QSerialPort.SerialPortError'
    BreakConditionError = ... # type: 'QSerialPort.SerialPortError'
    WriteError = ... # type: 'QSerialPort.SerialPortError'
    ReadError = ... # type: 'QSerialPort.SerialPortError'
    ResourceError = ... # type: 'QSerialPort.SerialPortError'
    UnsupportedOperationError = ... # type: 'QSerialPort.SerialPortError'
    TimeoutError = ... # type: 'QSerialPort.SerialPortError'
    NotOpenError = ... # type: 'QSerialPort.SerialPortError'
    UnknownError = ... # type: 'QSerialPort.SerialPortError'

    class DataErrorPolicy(int): ...
    SkipPolicy = ... # type: 'QSerialPort.DataErrorPolicy'
    PassZeroPolicy = ... # type: 'QSerialPort.DataErrorPolicy'
    IgnorePolicy = ... # type: 'QSerialPort.DataErrorPolicy'
    StopReceivingPolicy = ... # type: 'QSerialPort.DataErrorPolicy'
    UnknownPolicy = ... # type: 'QSerialPort.DataErrorPolicy'

    class PinoutSignal(int): ...
    NoSignal = ... # type: 'QSerialPort.PinoutSignal'
    TransmittedDataSignal = ... # type: 'QSerialPort.PinoutSignal'
    ReceivedDataSignal = ... # type: 'QSerialPort.PinoutSignal'
    DataTerminalReadySignal = ... # type: 'QSerialPort.PinoutSignal'
    DataCarrierDetectSignal = ... # type: 'QSerialPort.PinoutSignal'
    DataSetReadySignal = ... # type: 'QSerialPort.PinoutSignal'
    RingIndicatorSignal = ... # type: 'QSerialPort.PinoutSignal'
    RequestToSendSignal = ... # type: 'QSerialPort.PinoutSignal'
    ClearToSendSignal = ... # type: 'QSerialPort.PinoutSignal'
    SecondaryTransmittedDataSignal = ... # type: 'QSerialPort.PinoutSignal'
    SecondaryReceivedDataSignal = ... # type: 'QSerialPort.PinoutSignal'

    class FlowControl(int): ...
    NoFlowControl = ... # type: 'QSerialPort.FlowControl'
    HardwareControl = ... # type: 'QSerialPort.FlowControl'
    SoftwareControl = ... # type: 'QSerialPort.FlowControl'
    UnknownFlowControl = ... # type: 'QSerialPort.FlowControl'

    class StopBits(int): ...
    OneStop = ... # type: 'QSerialPort.StopBits'
    OneAndHalfStop = ... # type: 'QSerialPort.StopBits'
    TwoStop = ... # type: 'QSerialPort.StopBits'
    UnknownStopBits = ... # type: 'QSerialPort.StopBits'

    class Parity(int): ...
    NoParity = ... # type: 'QSerialPort.Parity'
    EvenParity = ... # type: 'QSerialPort.Parity'
    OddParity = ... # type: 'QSerialPort.Parity'
    SpaceParity = ... # type: 'QSerialPort.Parity'
    MarkParity = ... # type: 'QSerialPort.Parity'
    UnknownParity = ... # type: 'QSerialPort.Parity'

    class DataBits(int): ...
    Data5 = ... # type: 'QSerialPort.DataBits'
    Data6 = ... # type: 'QSerialPort.DataBits'
    Data7 = ... # type: 'QSerialPort.DataBits'
    Data8 = ... # type: 'QSerialPort.DataBits'
    UnknownDataBits = ... # type: 'QSerialPort.DataBits'

    class BaudRate(int): ...
    Baud1200 = ... # type: 'QSerialPort.BaudRate'
    Baud2400 = ... # type: 'QSerialPort.BaudRate'
    Baud4800 = ... # type: 'QSerialPort.BaudRate'
    Baud9600 = ... # type: 'QSerialPort.BaudRate'
    Baud19200 = ... # type: 'QSerialPort.BaudRate'
    Baud38400 = ... # type: 'QSerialPort.BaudRate'
    Baud57600 = ... # type: 'QSerialPort.BaudRate'
    Baud115200 = ... # type: 'QSerialPort.BaudRate'
    UnknownBaud = ... # type: 'QSerialPort.BaudRate'

    class Direction(int): ...
    Input = ... # type: 'QSerialPort.Direction'
    Output = ... # type: 'QSerialPort.Direction'
    AllDirections = ... # type: 'QSerialPort.Direction'

    class Directions(sip.simplewrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, f: typing.Union['QSerialPort.Directions', 'QSerialPort.Direction']) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QSerialPort.Directions') -> None: ...

        def __hash__(self) -> int: ...
        def __bool__(self) -> int: ...
        def __invert__(self) -> 'QSerialPort.Directions': ...
        def __int__(self) -> int: ...

    class PinoutSignals(sip.simplewrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, f: typing.Union['QSerialPort.PinoutSignals', 'QSerialPort.PinoutSignal']) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QSerialPort.PinoutSignals') -> None: ...

        def __hash__(self) -> int: ...
        def __bool__(self) -> int: ...
        def __invert__(self) -> 'QSerialPort.PinoutSignals': ...
        def __int__(self) -> int: ...

    @typing.overload
    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, name: str, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, info: 'QSerialPortInfo', parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def errorOccurred(self, error: 'QSerialPort.SerialPortError') -> None: ...
    def breakEnabledChanged(self, set: bool) -> None: ...
    def isBreakEnabled(self) -> bool: ...
    def handle(self) -> sip.voidptr: ...
    def writeData(self, data: bytes) -> int: ...
    def readLineData(self, maxlen: int) -> bytes: ...
    def readData(self, maxlen: int) -> bytes: ...
    def settingsRestoredOnCloseChanged(self, restore: bool) -> None: ...
    def requestToSendChanged(self, set: bool) -> None: ...
    def dataTerminalReadyChanged(self, set: bool) -> None: ...
    def dataErrorPolicyChanged(self, policy: 'QSerialPort.DataErrorPolicy') -> None: ...
    def flowControlChanged(self, flow: 'QSerialPort.FlowControl') -> None: ...
    def stopBitsChanged(self, stopBits: 'QSerialPort.StopBits') -> None: ...
    def parityChanged(self, parity: 'QSerialPort.Parity') -> None: ...
    def dataBitsChanged(self, dataBits: 'QSerialPort.DataBits') -> None: ...
    def baudRateChanged(self, baudRate: int, directions: typing.Union['QSerialPort.Directions', 'QSerialPort.Direction']) -> None: ...
    def setBreakEnabled(self, enabled: bool = ...) -> bool: ...
    def sendBreak(self, duration: int = ...) -> bool: ...
    def waitForBytesWritten(self, msecs: int) -> bool: ...
    def waitForReadyRead(self, msecs: int) -> bool: ...
    def canReadLine(self) -> bool: ...
    def bytesToWrite(self) -> int: ...
    def bytesAvailable(self) -> int: ...
    def isSequential(self) -> bool: ...
    def setReadBufferSize(self, size: int) -> None: ...
    def readBufferSize(self) -> int: ...
    def clearError(self) -> None: ...
    @typing.overload
    def error(self) -> 'QSerialPort.SerialPortError': ...
    @typing.overload
    def error(self, serialPortError: 'QSerialPort.SerialPortError') -> None: ...
    def dataErrorPolicy(self) -> 'QSerialPort.DataErrorPolicy': ...
    def setDataErrorPolicy(self, policy: 'QSerialPort.DataErrorPolicy' = ...) -> bool: ...
    def atEnd(self) -> bool: ...
    def clear(self, dir: typing.Union['QSerialPort.Directions', 'QSerialPort.Direction'] = ...) -> bool: ...
    def flush(self) -> bool: ...
    def pinoutSignals(self) -> 'QSerialPort.PinoutSignals': ...
    def isRequestToSend(self) -> bool: ...
    def setRequestToSend(self, set: bool) -> bool: ...
    def isDataTerminalReady(self) -> bool: ...
    def setDataTerminalReady(self, set: bool) -> bool: ...
    def flowControl(self) -> 'QSerialPort.FlowControl': ...
    def setFlowControl(self, flow: 'QSerialPort.FlowControl') -> bool: ...
    def stopBits(self) -> 'QSerialPort.StopBits': ...
    def setStopBits(self, stopBits: 'QSerialPort.StopBits') -> bool: ...
    def parity(self) -> 'QSerialPort.Parity': ...
    def setParity(self, parity: 'QSerialPort.Parity') -> bool: ...
    def dataBits(self) -> 'QSerialPort.DataBits': ...
    def setDataBits(self, dataBits: 'QSerialPort.DataBits') -> bool: ...
    def baudRate(self, dir: typing.Union['QSerialPort.Directions', 'QSerialPort.Direction'] = ...) -> int: ...
    def setBaudRate(self, baudRate: int, dir: typing.Union['QSerialPort.Directions', 'QSerialPort.Direction'] = ...) -> bool: ...
    def settingsRestoredOnClose(self) -> bool: ...
    def setSettingsRestoredOnClose(self, restore: bool) -> None: ...
    def close(self) -> None: ...
    def open(self, mode: typing.Union[QtCore.QIODevice.OpenMode, QtCore.QIODevice.OpenModeFlag]) -> bool: ...
    def setPort(self, info: 'QSerialPortInfo') -> None: ...
    def portName(self) -> str: ...
    def setPortName(self, name: str) -> None: ...


class QSerialPortInfo(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, port: QSerialPort) -> None: ...
    @typing.overload
    def __init__(self, name: str) -> None: ...
    @typing.overload
    def __init__(self, other: 'QSerialPortInfo') -> None: ...

    def serialNumber(self) -> str: ...
    def isNull(self) -> bool: ...
    @staticmethod
    def availablePorts() -> typing.Any: ...
    @staticmethod
    def standardBaudRates() -> typing.List[int]: ...
    def isValid(self) -> bool: ...
    def isBusy(self) -> bool: ...
    def hasProductIdentifier(self) -> bool: ...
    def hasVendorIdentifier(self) -> bool: ...
    def productIdentifier(self) -> int: ...
    def vendorIdentifier(self) -> int: ...
    def manufacturer(self) -> str: ...
    def description(self) -> str: ...
    def systemLocation(self) -> str: ...
    def portName(self) -> str: ...
    def swap(self, other: 'QSerialPortInfo') -> None: ...
