#!/usr/bin/python3

import wx


def str_is_float(the_str: str) -> bool:
    try:
        float(the_str)
        return True
    except ValueError:
        return False


class LcalcFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)

        # make the main panel and increase system font 2 times for it
        self.the_panel = wx.Panel(self, wx.ID_ANY)
        systemfont = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        self.the_panel.SetFont(systemfont.Scale(2))

        self.status_bar = self.CreateStatusBar(1)
        # self.status_bar.SetStatusText('This goes in your statusbar')

        labelcm = wx.StaticText(self.the_panel, id=wx.ID_ANY, label=u'cm\u207b\u00b9')
        label_h_size, label_v_size = labelcm.GetTextExtent(labelcm.GetLabel())

        top_sizer = wx.BoxSizer(wx.VERTICAL)
        nm_sizer = wx.BoxSizer(wx.HORIZONTAL)
        cm_sizer = wx.BoxSizer(wx.HORIZONTAL)
        ev_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # the nm row:
        editnm = wx.TextCtrl(self.the_panel, style=wx.TE_RIGHT, size=(7 * label_v_size, label_v_size))
        labelnm = wx.StaticText(self.the_panel, id=wx.ID_ANY, label='nm', size=(label_h_size, label_v_size))
        nm_sizer.Add(editnm, 1, wx.ALL | wx.EXPAND, 3)
        nm_sizer.Add(labelnm, 0, wx.ALL, 3)

        # the cm-1 row:
        editcm = wx.TextCtrl(self.the_panel, style=wx.TE_RIGHT, size=(7 * label_v_size, label_v_size))
        cm_sizer.Add(editcm, 1, wx.ALL | wx.EXPAND, 3)
        cm_sizer.Add(labelcm, 0, wx.ALL, 3)

        # the eV row:
        editev = wx.TextCtrl(self.the_panel, style=wx.TE_RIGHT, size=(7 * label_v_size, label_v_size))
        labelev = wx.StaticText(self.the_panel, id=wx.ID_ANY, label='eV', size=(label_h_size, label_v_size))
        ev_sizer.Add(editev, 1, wx.ALL | wx.EXPAND, 3)
        ev_sizer.Add(labelev, 0, wx.ALL, 3)

        top_sizer.Add(nm_sizer, 0, wx.EXPAND)
        top_sizer.Add(cm_sizer, 0, wx.EXPAND)
        top_sizer.Add(ev_sizer, 0, wx.EXPAND)

        # set the size of the window
        self.the_panel.SetSizer(top_sizer)
        top_sizer.Fit(self)

        self.Bind(wx.EVT_CHAR_HOOK, self.on_escape)

        # filter out digits and dots
        editnm.Bind(wx.EVT_KEY_DOWN, self.filter_digits)
        editcm.Bind(wx.EVT_KEY_DOWN, self.filter_digits)
        editev.Bind(wx.EVT_KEY_DOWN, self.filter_digits)

        # check if we have a valid floats:
        editnm.Bind(wx.EVT_CHAR, self.filter_floats)
        editcm.Bind(wx.EVT_CHAR, self.filter_floats)
        editev.Bind(wx.EVT_CHAR, self.filter_floats)

    def on_escape(self, event):
        # quit application if ESC pressed
        key_code = event.GetKeyCode()
        if key_code == wx.WXK_ESCAPE:
            self.Close()
        event.Skip()

    def filter_digits(self, event):
        # one filter for all inputs:
        # only digits and decimal separators, no characters!
        key_code = event.GetKeyCode()

        # Allow ASCII numerics
        if ord('0') <= key_code <= ord('9'):
            event.Skip()
            return

        # Allow decimal points
        if key_code == ord('.'):
            event.Skip()
            return

        if key_code == ord(','):
            # substitute dot for comma so there would be no problems with calculations later
            keyinput = wx.UIActionSimulator()
            keyinput.Char(ord('.'))
            return

        # Block everything else
        return

    def filter_floats(self, event):
        # check for a valid float on input
        key_code = event.GetKeyCode()
        the_obj = event.GetEventObject()

        if str_is_float(the_obj.GetLineText(0) + chr(key_code)):
            event.Skip()
            return

        # Block everything else
        return


if __name__ == "__main__":
    app = wx.App()

    frame = LcalcFrame(None, "lcalc")
    frame.Show()

    app.MainLoop()
