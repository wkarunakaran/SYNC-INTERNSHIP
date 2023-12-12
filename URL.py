import tkinter as tk
import random
import string

class URLShortener:
    def __init__(self):
        self.url_mapping = {}
        self.short_url_length = 6

    def shorten_url(self, long_url):
        for short_url, stored_url in self.url_mapping.items():
            if stored_url == long_url:
                return short_url

        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(self.short_url_length))

        while short_url in self.url_mapping:
            short_url = ''.join(random.choice(characters) for _ in range(self.short_url_length))

        self.url_mapping[short_url] = long_url

        return short_url

    def expand_url(self, short_url):
        return self.url_mapping.get(short_url, None)

class URLShortenerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("URL Shortener")

        self.shortener = URLShortener()

        self.label = tk.Label(root, text="Enter a URL to shorten:")
        self.label.pack()

        self.url_entry = tk.Entry(root)
        self.url_entry.pack()

        self.shorten_button = tk.Button(root, text="Shorten URL", command=self.shorten_url)
        self.shorten_button.pack()

        self.short_url_label = tk.Label(root, text="")
        self.short_url_label.pack()

        self.expand_button = tk.Button(root, text="Expand URL", command=self.expand_url)
        self.expand_button.pack()

        self.long_url_label = tk.Label(root, text="")
        self.long_url_label.pack()

    def shorten_url(self):
        long_url = self.url_entry.get()
        short_url = self.shortener.shorten_url(long_url)
        self.short_url_label.config(text=f"Short URL: {short_url}")

    def expand_url(self):
        short_url = self.url_entry.get()
        long_url = self.shortener.expand_url(short_url)
        if long_url:
            self.long_url_label.config(text=f"Expanded URL: {long_url}")
        else:
            self.long_url_label.config(text="URL not found in mapping")

if __name__ == "__main__":
    root = tk.Tk()
    app = URLShortenerApp(root)
    root.mainloop()
