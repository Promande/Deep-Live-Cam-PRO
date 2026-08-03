import tkinter

def apply_patch():
    original_init = tkinter.Tk.__init__
    
    def patched_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        self.tk.eval("""
        if {[info commands ::tk::ScreenChanged] == ""} {
            proc ::tk::ScreenChanged {args} {
                return
            }
        }
        """)
    
    tkinter.Tk.__init__ = patched_init

apply_patch()
