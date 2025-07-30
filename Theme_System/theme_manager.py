import tkinter as tk
from typing import Dict, Any

class ThemeManager:
    def __init__(self):
        self.is_dark_theme = False
        self.themes: Dict[str, Dict[str, Any]] = {
            'light': {
                'bg': "#F0F0F0",
                'frame_bg': "#FFFFFF",
                'button_bg': "#E0E0E0",
                'text_fg': "#000000",
                'button_fg': "#000000"
            },
            'dark': {
                'bg': "#2E2E2E",
                'frame_bg': "#3E3E3E",
                'button_bg': "#505050",
                'text_fg': "#FFFFFF",
                'button_fg': "#FFFFFF"
            }
        }
    
    def toggle_theme(self) -> bool:
        self.is_dark_theme = not self.is_dark_theme
        return self.is_dark_theme
    
    def get_current_theme(self) -> Dict[str, Any]:
        return self.themes['dark' if self.is_dark_theme else 'light']
    
    def apply_theme_to_window(self, window: tk.Tk | tk.Toplevel):
        theme = self.get_current_theme()
        window.config(bg=theme['bg'])
        
        for widget in window.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.config(bg=theme['frame_bg'])
            elif isinstance(widget, tk.Label):
                widget.config(bg=theme['frame_bg'], fg=theme['text_fg'])
            elif isinstance(widget, tk.Button):
                widget.config(bg=theme['button_bg'], fg=theme['button_fg'])