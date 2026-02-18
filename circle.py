
var1="""SET progman TO $'''pbrush.exe'''
System.RunApplication.RunApplication ApplicationPath: progman WindowStyle: System.ProcessWindowStyle.Maximized ProcessId=> AppProcessId
Workstation.GetScreenResolution MonitorNumber: 1 MonitorWidth=> MonitorWidth MonitorHeight=> MonitorHeight
SET varx TO MonitorWidth / 2
SET vary TO MonitorHeight / 2 + 62
WAIT 3
MouseAndKeyboard.MoveMouse X: varx + 20 Y: vary + 20 RelativeTo: MouseAndKeyboard.PositionRelativeTo.ActiveWindow MovementStyle: MouseAndKeyboard.MovementStyle.Instant
MouseAndKeyboard.SendMouseClick.Click ClickType: MouseAndKeyboard.MouseClickType.LeftClick MillisecondsDelay: 0
MouseAndKeyboard.MoveMouse X: varx + 20 Y: vary + 20 RelativeTo: MouseAndKeyboard.PositionRelativeTo.ActiveWindow MovementStyle: MouseAndKeyboard.MovementStyle.Instant
MouseAndKeyboard.SendMouseClick.Click ClickType: MouseAndKeyboard.MouseClickType.LeftClick MillisecondsDelay: 0
MouseAndKeyboard.MoveMouse X: varx + 20 Y: vary - 20 RelativeTo: MouseAndKeyboard.PositionRelativeTo.ActiveWindow MovementStyle: MouseAndKeyboard.MovementStyle.Instant
MouseAndKeyboard.SendMouseClick.Click ClickType: MouseAndKeyboard.MouseClickType.LeftClick MillisecondsDelay: 0
MouseAndKeyboard.MoveMouse X: varx - 20 Y: vary + 20 RelativeTo: MouseAndKeyboard.PositionRelativeTo.ActiveWindow MovementStyle: MouseAndKeyboard.MovementStyle.Instant
MouseAndKeyboard.SendMouseClick.Click ClickType: MouseAndKeyboard.MouseClickType.LeftClick MillisecondsDelay: 0
MouseAndKeyboard.MoveMouse X: varx - 20 Y: vary - 20 RelativeTo: MouseAndKeyboard.PositionRelativeTo.ActiveWindow MovementStyle: MouseAndKeyboard.MovementStyle.Instant
MouseAndKeyboard.SendMouseClick.Click ClickType: MouseAndKeyboard.MouseClickType.LeftClick MillisecondsDelay: 0
MouseAndKeyboard.MoveMouse X: varx - 30 Y: vary RelativeTo: MouseAndKeyboard.PositionRelativeTo.ActiveWindow MovementStyle: MouseAndKeyboard.MovementStyle.Instant
MouseAndKeyboard.SendMouseClick.Click ClickType: MouseAndKeyboard.MouseClickType.LeftClick MillisecondsDelay: 0
MouseAndKeyboard.MoveMouse X: varx + 30 Y: vary RelativeTo: MouseAndKeyboard.PositionRelativeTo.ActiveWindow MovementStyle: MouseAndKeyboard.MovementStyle.Instant
MouseAndKeyboard.SendMouseClick.Click ClickType: MouseAndKeyboard.MouseClickType.LeftClick MillisecondsDelay: 0
MouseAndKeyboard.MoveMouse X: varx Y: vary + 30 RelativeTo: MouseAndKeyboard.PositionRelativeTo.ActiveWindow MovementStyle: MouseAndKeyboard.MovementStyle.Instant
MouseAndKeyboard.SendMouseClick.Click ClickType: MouseAndKeyboard.MouseClickType.LeftClick MillisecondsDelay: 0
MouseAndKeyboard.MoveMouse X: varx Y: vary - 30 RelativeTo: MouseAndKeyboard.PositionRelativeTo.ActiveWindow MovementStyle: MouseAndKeyboard.MovementStyle.Instant
MouseAndKeyboard.SendMouseClick.Click ClickType: MouseAndKeyboard.MouseClickType.LeftClick MillisecondsDelay: 0
"""
print("\033c\033[40;37m\n ")
print("\n"+"-"*80 +"\n")
print(var1)