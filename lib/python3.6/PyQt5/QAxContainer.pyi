# The PEP 484 type hints stub file for the QAxContainer module.
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

from PyQt5 import QtWidgets

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

# Convenient aliases for complicated OpenGL types.
PYQT_OPENGL_ARRAY = typing.Union[typing.Sequence[int], typing.Sequence[float],
        sip.Buffer, None]
PYQT_OPENGL_BOUND_ARRAY = typing.Union[typing.Sequence[int],
        typing.Sequence[float], sip.Buffer, int, None]


class QAxBase(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QAxBase') -> None: ...

    def disableEventSink(self) -> None: ...
    def disableClassInfo(self) -> None: ...
    def disableMetaObject(self) -> None: ...
    def setControl(self, a0: str) -> bool: ...
    def clear(self) -> None: ...
    def exception(self, a0: int, a1: str, a2: str, a3: str) -> None: ...
    def propertyChanged(self, a0: str) -> None: ...
    def signal(self, a0: str, a1: int, a2: sip.voidptr) -> None: ...
    def asVariant(self) -> typing.Any: ...
    def verbs(self) -> typing.List[str]: ...
    def isNull(self) -> bool: ...
    def setPropertyWritable(self, a0: str, a1: bool) -> None: ...
    def propertyWritable(self, a0: str) -> bool: ...
    def generateDocumentation(self) -> str: ...
    def setPropertyBag(self, a0: typing.Dict[str, typing.Any]) -> None: ...
    def propertyBag(self) -> typing.Dict[str, typing.Any]: ...
    @typing.overload
    def querySubObject(self, a0: str, a1: typing.Iterable[typing.Any]) -> 'QAxObject': ...
    @typing.overload
    def querySubObject(self, a0: str, value1: typing.Any = ..., value2: typing.Any = ..., value3: typing.Any = ..., value4: typing.Any = ..., value5: typing.Any = ..., value6: typing.Any = ..., value7: typing.Any = ..., value8: typing.Any = ...) -> 'QAxObject': ...
    @typing.overload
    def dynamicCall(self, a0: str, a1: typing.Iterable[typing.Any]) -> typing.Any: ...
    @typing.overload
    def dynamicCall(self, a0: str, value1: typing.Any = ..., value2: typing.Any = ..., value3: typing.Any = ..., value4: typing.Any = ..., value5: typing.Any = ..., value6: typing.Any = ..., value7: typing.Any = ..., value8: typing.Any = ...) -> typing.Any: ...
    def control(self) -> str: ...


class QAxObject(QtCore.QObject, QAxBase):

    @typing.overload
    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, a0: str, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def connectNotify(self, a0: QtCore.QMetaMethod) -> None: ...
    def doVerb(self, a0: str) -> bool: ...


class QAxWidget(QtWidgets.QWidget, QAxBase):

    @typing.overload
    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ..., flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType] = ...) -> None: ...
    @typing.overload
    def __init__(self, a0: str, parent: typing.Optional[QtWidgets.QWidget] = ..., flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType] = ...) -> None: ...

    def connectNotify(self, a0: QtCore.QMetaMethod) -> None: ...
    def translateKeyEvent(self, a0: int, a1: int) -> bool: ...
    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None: ...
    def changeEvent(self, a0: QtCore.QEvent) -> None: ...
    def createHostWindow(self, a0: bool) -> bool: ...
    def minimumSizeHint(self) -> QtCore.QSize: ...
    def sizeHint(self) -> QtCore.QSize: ...
    def doVerb(self, a0: str) -> bool: ...
    def clear(self) -> None: ...
