from PyQt6.QtWidgets import QApplication
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineProfile

class Core:
    @staticmethod
    def weblet(param):
        try:
            html_content = param.strip()
            app = QApplication(["Linea Weblet"])
            QWebEngineProfile.defaultProfile().setHttpCacheType(
                QWebEngineProfile.HttpCacheType.MemoryHttpCache
            )
            web_view = QWebEngineView()
            web_view.setHtml(html_content)
            web_view.setWindowTitle("Linea Weblet")
            web_view.show()
            app.exec()
        except Exception as e:
            print(f"Error in weblet: {e}")