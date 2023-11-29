def get_url_conf(host):
    mapping = {
        "www.example-a.dev": "firstApp.urls",
        "Www.example-b.dev": "secondApp.urls",
        "www.example-c.dev": "thirdApp.urls"
    }

    return mapping.get(host, "Sorry, no match")

print(get_url_conf("www.example-a.dev"))
# firstApp.urls

print(get_url_conf("www.example.dev"))
# Sorry, no match
