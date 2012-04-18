#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import os

class Wizard:

    def __init__(self):
        
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL) # Create a new window
        self.window.set_title("Control Center") # Set the window title
        self.window.set_border_width(20)# Sets the border width of the window.
        self.window.connect("delete_event", self.delete_event) # Click on the X -> close window
        
        # Create vertical box
        self.vbox = gtk.VBox ()
        
        # EACH OPTION GETS ITS OWN HORIZONTAL BOX (wizard_option)
        
        # OPTION 1: Change Monitor Display Settings
        self.box_image = '/usr/share/icons/gTangish-2.0a1/32x32/apps/display-capplet.png'
        self.box_label = 'Change Monitor Display Settings'
        self.box = self.wizard_option (self.box_image, self.box_label, self.config_monitor)
        self.vbox.add (self.box)
        
        # Option 2: Hardware Wizard
        self.box_image = '/usr/share/icons/gTangish-2.0a1/32x32/categories/applications-system.png'
        self.box_label = 'Hardware Wizard'
        self.box = self.wizard_option (self.box_image, self.box_label, self.config_hardware)
        self.vbox.add (self.box)
        
        # Option 3: Information
        self.box_image = '/usr/share/icons/gTangish-2.0a1/32x32/status/dialog-information.png'
        self.box_label = 'System Information Wizard'
        self.box = self.wizard_option (self.box_image, self.box_label, self.config_info)
        self.vbox.add (self.box)
        
        # Option 4: Network
        self.box_image = '/usr/share/icons/gnome/32x32/categories/preferences-system-network.png'
        self.box_label = 'Network Wizard'
        self.box = self.wizard_option (self.box_image, self.box_label, self.config_network)
        self.vbox.add (self.box)
        
        # Option 5: Printer
        self.box_image = '/usr/share/icons/gTangish-2.0a1/32x32/actions/stock_print-setup.png'
        self.box_label = 'Printer Wizard'
        self.box = self.wizard_option (self.box_image, self.box_label, self.config_printer)
        self.vbox.add (self.box)
        
        # Option 6: Software
        self.box_image = '/usr/share/synaptic/pixmaps/synaptic_32x32.xpm'
        self.box_label = 'Software Wizard'
        self.box = self.wizard_option (self.box_image, self.box_label, self.config_software)
        self.vbox.add (self.box)
        
        # Option 7: System
        self.box_image = '/usr/share/icons/gnome/32x32/emblems/emblem-system.png'
        self.box_label = 'System Wizard'
        self.box = self.wizard_option (self.box_image, self.box_label, self.config_system)
        self.vbox.add (self.box)
        
        # Option 8: Wallpaper
        self.box_image = '/usr/share/icons/gnome/32x32/apps/preferences-desktop-wallpaper.png'
        self.box_label = 'Wallpaper Wizard'
        self.box = self.wizard_option (self.box_image, self.box_label, self.config_wallpaper)
        self.vbox.add (self.box)
        
        # Show everything
        #self.table.show()
        self.window.add (self.vbox)
        self.window.show ()
        self.window.show_all ()
        
        
        
    # This callback quits the program
    def delete_event (self, widget, event, data=None):
        gtk.main_quit()
        return False
        
    def config_monitor (self, widget, callback_data=None):
        os.system ('lxrandr &')
        
    def config_hardware (self, widget, callback_data=None):
        os.system ('python /usr/local/bin/config-hardware.py &')
        
    def config_info (self, widget, callback_data=None):
        os.system ('python /usr/local/bin/config-info.py &')
    
    def config_network (self, widget, callback_data=None):
        os.system ('python /usr/local/bin/config-network.py &')
        
    def config_printer (self, widget, callback_data=None):
        os.system ('python /usr/local/bin/config-printer.py &')
        
    def config_software (self, widget, callback_data=None):
        os.system ('python /usr/local/bin/config-software.py &')

    def config_system (self, widget, callback_data=None):
        os.system ('python /usr/local/bin/config-system.py &')

    def config_wallpaper (self, widget, callback_data=None):
        os.system ('python /usr/local/bin/config-wallpaper.py &')

    
    def wizard_option (self, filename_image, string_label, fctn_action):
        # Horizontal box
        self.hbox = gtk.HBox ()
        
        # Button icon
        self.image = gtk.Image ()
        self.image.set_from_file (filename_image)
        self.image.show ()
        
        # Button
        self.button = gtk.Button()
        self.button.set_size_request(48, 48)
        self.button.connect('clicked', fctn_action)
        self.button.add(self.image) # Add image to button
        self.button.show()
        self.hbox.pack_start(self.button, False, False, 0)
        
        # Label
        self.label = gtk.Label (' ' + string_label)
        self.label.set_alignment (0, .5)
        self.label.show ()
        
        self.hbox.pack_start(self.label, False, False, 0)
        self.hbox.show ()
        
        return self.hbox
    
def main():
    gtk.main()
    return 0       

if __name__ == "__main__":
    Wizard()
    main()
