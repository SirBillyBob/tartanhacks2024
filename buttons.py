"""Module with classes of buttons."""


from typing import *
from vector2 import *
from cmu_graphics import *
import warnings


class Button:
    """A class of objects representing rectangular buttons on the screen.

    Attributes
    ----------
    text: str
        The text shown on the button.

    color: str
        The background color of the button.
    
    highlight: str
        The background color of the button when the button is highlighted.
    
    centerX: float
        The x position of the center of the button on the screen.
    
    centerY: float
        The y position of the center of the button on the screen.
    
    key: str
        The key which can be pressed to click the button.
    
    clickHandler: Optional[Callable]
        The function which is called when the button is clicked. If `None`,
        clicking the button does nothing and the button is essentially just a
        rectangular label.
    
    width: float
        The width of the button.
    
    height: float
        The height of the button.
    
    textSize: int
        The size of the text on the button.
    
    textBold: bool
        If `True`, the text on the button will be bold.
    
    Methods
    -------
    draw(highlight: bool) -> None
        Draws the button on the screen. If `highlight` is `True`, the highlight
        color is used.
    
    hitsPoint(x: float, y: float) -> bool
        Returns `True` if the point (x, y) on the screen is inside the button.
        Used to detect if a mouse click happened on the button.
    
    click() -> None
        Calls `clickHandler`.
    """

    def __init__(
            self,
            text: str,
            centerX: float,
            centerY: float,
            key: str = '',
            clickHandler: Optional[Callable] = None,
            width: float = 500,
            height: float = 100,
            textSize: int = 30,
            textBold: bool = True,
        ) -> None:
        """Creates a new Button object."""
        if clickHandler is None:
            self.text = text
            self.color = 'gray'
            self.highlight = rgb(0.75, 0.25, 0.25)
        else:
            self.text = text + f' [{key}]'
            self.color = 'salmon'
            self.highlight = 'yellow'

        self.centerX = centerX
        self.centerY = centerY
        self.key = key
        self.clickHandler = clickHandler
        self.width = width
        self.height = height
        self.textSize = textSize
        self.textBold = textBold

    def draw(self, highlight: bool = False) -> None:
        """Draws the button on the screen."""
        if highlight:
            color = self.highlight
        else:
            color = self.color

        drawRect(
            self.centerX,
            self.centerY,
            self.width,
            self.height,
            fill=color,
            border='black',
            borderWidth=5,
            align='center'
        )
        drawLabel(
            self.text,
            self.centerX,
            self.centerY,
            size=self.textSize,
            bold=self.textBold
        )

    def hitsPoint(self, x: float, y: float) -> bool:
        """Returns `True` if the point (x, y) is inside the button."""
        minX = self.centerX - self.width / 2
        maxX = self.centerX + self.width / 2
        minY = self.centerY - self.height / 2
        maxY = self.centerY + self.height / 2
        if minX <= x <= maxX and minY <= y <= maxY:
            return True
        else:
            return False

    def click(self) -> None:
        """Calls `clickHandler`."""
        self.clickHandler()


class ConfigButtonABC(Button):
    """An abstract base class (ABC) for configuration buttons.

    A configuration button is some button which controls a setting or
    configuration. This class extends `Button`.

    Attributes
    ----------
    configName: str
        The name of the configuration or setting (e.g. "frameRate").
    
    value: float | bool | str
        The current value of the configuration (e.g. "30").
    
    listening: bool
        If `True`, the button is currently "listening" for inputs.
    
    Other attributes (text, clickHandler, ...) inherited from `Button` class.

    Methods
    -------
    setValue(newValue: str) -> None
        Sets the value of the configuration to `newValue` (must be a string).

    draw() -> None:
        Draws the button, with `highlight=True` if the button is listening.
    """

    def __init__(
            self,
            configName: str,
            value: Union[float, bool, str],
            centerX: float,
            centerY: float,
            key: str = '',
            clickHandler: Callable[..., Any] | None = None,
            width: float = 450,
            height: float = 50,
            textSize: int = 20,
            textBold: bool = False,
        ) -> None:
        self.configName = configName
        self.value = value
        text = self.configName + ': ' + str(self.value)
        super().__init__(
            text, centerX, centerY, key, clickHandler, width, height, textSize,
            textBold
        )

        self.listening = False

    def setValue(self, newValue: str) -> None:
        """Sets the value of the configuration to `newValue`.
        
        The configuration files are text based, so `newValue` must be a string.
        """
        try:
            if isinstance(self.value, float):
                self.value = float(newValue)
            elif isinstance(self.value, int):
                self.value = int(newValue)
            else:
                self.value = newValue

            self.text = (self.configName + ': ' + str(self.value) +
                         f' [{self.key}]')
            self.listening = False

        except ValueError:
            warnings.warn("Invalid type for configuration " + 
                          f"'{self.configName}': '{type(newValue)}'")

    def draw(self) -> None:
        return super().draw(highlight=self.listening)


class ControlButton(ConfigButtonABC):
    """A class of buttons which can be used to customize controls."""

    def __init__(
            self,
            controlName: str,
            control: str,
            centerX: float,
            centerY: float,
            key: str = '',
            clickHandler: Callable[..., Any] | None = None,
            width: float = 450,
            height: float = 50,
            textSize: int = 20,
            textBold: bool = False
        ) -> None:

        super().__init__(
            controlName, control, centerX, centerY, key, clickHandler, width,
            height, textSize, textBold
        )


class SettingButton(ConfigButtonABC):
    """A class of buttons which can be used to customize settings.
    
    Attributes
    ----------
    tempValue: str
        The temporary value of the button, used when the button is listening for
        input. Instead of updating the actual value of the setting on every key
        press, a temporary value is stored in this attribute. When "enter" is
        pressed, the actual value is set to this temporary value.
    
    Methods
    -------
    updateTempValue(newKey: str) -> None
        Adds `newKey` to `tempValue`.
    
    setTempValue(newValue: float | bool | str) -> None
        Sets `tempValue` to the string representation of `newValue` and updates
        `text`.
    
    delTempValue() -> None
        Deletes the most recent key from `tempValue`.
    
    setValue() -> None:
        Sets the configuration value to whatever is stored in `tempValue`.
    
    resetTempValue() -> None:
        Resets `tempValue` to the actual stored configuration value.
    """

    def __init__(
            self,
            settingName: str,
            value: Union[float, bool, str],
            centerX: float,
            centerY: float,
            key: str = '',
            clickHandler: Callable[..., Any] | None = None,
            width: float = 450,
            height: float = 50,
            textSize: int = 20,
            textBold: bool = False,
        ) -> None:
        super().__init__(
            settingName, value, centerX, centerY, key, clickHandler, width,
            height, textSize, textBold
        )

        self.tempValue = str(value)

    def updateTempValue(self, newKey: str) -> None:
        """Adds `newKey` to `tempValue`."""
        if self.tempValue == '_':
            self.tempValue = str(newKey)
        else:
            self.tempValue += str(newKey)
        self.text = self.configName + ': ' + str(self.tempValue)

    def setTempValue(self, newValue: Union[float, bool, str]):
        """Sets `tempValue` to the string representation of `newValue`."""
        self.tempValue = str(newValue)
        self.text = self.configName + ': ' + self.tempValue

    def delTempValue(self):
        """Deletes the most recent key from `tempValue`."""
        self.tempValue = self.tempValue[:-1]
        if self.tempValue == '':
            self.tempValue = '_'
        self.text = self.configName + ': ' + str(self.tempValue)

    def setValue(self):
        """Sets the actual configuration value to `tempValue`."""
        try:
            if isinstance(self.value, float):
                self.value = float(self.tempValue)
            elif isinstance(self.value, int):
                self.value = int(self.tempValue)
            else:
                self.value = self.tempValue

            self.tempValue = str(self.value)
            self.text = self.configName + ': ' + self.tempValue + f' [{self.key}]'
            self.listening = False

        except ValueError:
            warnings.warn(f"Cannot convert input {self.tempValue} to " + 
                          f"{type(self.value)}")
            self.resetTempValue()
    
    def resetTempValue(self):
        """Resets `tempValue` to the actual configuration value."""
        self.tempValue = str(self.value)
        self.text = self.configName + ': ' + self.tempValue + f' [{self.key}]'
        self.listening = False


class ToggleSettingButton(ConfigButtonABC):
    """A class of buttons which represent settings which can be toggled."""
    
    def __init__(
            self,
            settingName: str,
            values: list[Union[int, float, str]],
            initValue: Union[int, float, str],
            centerX: float,
            centerY: float,
            key: str = '',
            clickHandler: Callable[..., Any] | None = None,
            width: float = 450,
            height: float = 50,
            textSize: int = 20,
            textBold: bool = False
        ) -> None:
        self.values = values
        self.valueIndex = self.values.index(initValue)

        super().__init__(settingName, self.values[self.valueIndex], centerX,
                         centerY, key, clickHandler, width, height, textSize,
                         textBold)
    
    def toggle(self):
        self.valueIndex += 1
        self.valueIndex %= len(self.values)
        self.value = self.values[self.valueIndex]
        self.text = f'{self.configName}: {self.value} [{self.key}]'
