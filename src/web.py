from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from config import HTML_DIR

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""
        with open(os.path.join(HTML_DIR, "contacts.html"), encoding="utf-8") as f:
            data = f.read()
            self.send_response(200)  # Отправка кода ответа
            self.send_header(
                "Content-type", "text/html"
            )  # Отправка типа данных, который будет передаваться
            self.end_headers()  # Завершение формирования заголовков ответа
            self.wfile.write(bytes(data, "utf-8"))  # Тело ответа

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)
        print(str(body))
        self.send_response(200)
        self.end_headers()


if __name__ == "__main__":

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
