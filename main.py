import kivy
from kivy.app import App
from pyobjus import autoclass, objc_str, protocol
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.button import Button
from pyobjus.dylib_manager import load_framework, INCLUDE
from pyobjus.objc_py_types import NSRect, NSPoint, NSSize

load_framework(INCLUDE.WebKit)
load_framework(INCLUDE.CoreGraphics)



WebView = autoclass('WKWebView')
WebViewConfig = autoclass('WKWebViewConfiguration')
NSURL = autoclass('NSURL')
NSURLRequest = autoclass('NSURLRequest')
UIApp = autoclass('UIApplication')

import threading

class WK(Widget) :
    def __init__(self, **kwargs) :
        super(WK, self).__init__(**kwargs)
        Clock.schedule_once(self.create_wk, 0)
    
    def create_wk(self, *args) :
        self.view = UIApp.sharedApplication().keyWindow.rootViewController().view()
        config = WebViewConfig.alloc().init()
        frame = NSRect(NSPoint(0,0),NSSize(Window.size[0]/2.,Window.size[1]/2.))
        webView = WebView.alloc().initWithFrame_configuration_(frame, config)
        url = NSURL.URLWithString_(objc_str("http://intra-dot-research-repo-1.appspot.com/development"))
        request = NSURLRequest.requestWithURL_(url)
        _webView = WebView.alloc().initWithFrame_(frame) 
        _webView.loadRequest_(request)
        self.view.addSubview_(_webView)
        print('Sudah')

class serviceApp(App):
	def build(self) :
		return WK()

if __name__ == '__main__':                                                                      
    serviceApp().run()

